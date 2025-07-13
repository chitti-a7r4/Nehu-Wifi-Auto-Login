#!/usr/bin/env python3
import sys
import os
import asyncio
import platform
import getpass
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from cryptography.fernet import Fernet
import time

# Function to get the correct path for GeckoDriver when bundled as an executable
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Function to safely get user input
def get_user_input(prompt):
    try:
        return input(prompt)
    except EOFError:
        print("Error: Unable to read input. Please run the script from a terminal.")
        sys.exit(1)

# Configure Firefox options to ignore SSL errors and insecure connections
firefox_options = Options()
firefox_options.add_argument('--ignore-certificate-errors')
firefox_options.add_argument('--ignore-ssl-errors')
firefox_options.add_argument('--allow-insecure-localhost')
firefox_options.add_argument('--allow-running-insecure-content')
firefox_options.add_argument('--disable-web-security')

# Firefox-specific preferences for handling insecure connections
firefox_options.set_preference('security.tls.insecure_fallback_hosts', '192.0.2.1')
firefox_options.set_preference('security.mixed_content.block_active_content', False)
firefox_options.set_preference('security.mixed_content.block_display_content', False)
firefox_options.set_preference('network.stricttransportsecurity.preloadlist', False)
firefox_options.set_preference('security.cert_pinning.enforcement_level', 0)
firefox_options.set_preference('security.tls.disable_insecure_fallback_hosts', False)

# Set file paths for Linux
def get_config_dir():
    # Use XDG_CONFIG_HOME if set, otherwise use ~/.config
    config_home = os.getenv("XDG_CONFIG_HOME", os.path.expanduser("~/.config"))
    return os.path.join(config_home, "nehu_wifi")

config_path = get_config_dir()
credentials_file = os.path.join(config_path, "credentials.enc")
key_file = os.path.join(config_path, "key.key")

# Ensure directory exists
os.makedirs(config_path, exist_ok=True)

# Generate and save encryption key if it doesn't exist
def ensure_key():
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, 'wb') as f:
            f.write(key)
        # Set secure permissions (readable only by user)
        os.chmod(key_file, 0o600)

# Load encryption key
def load_key():
    with open(key_file, 'rb') as f:
        return f.read()

# Save encrypted credentials
def save_credentials(username, password):
    key = load_key()
    fernet = Fernet(key)
    data = json.dumps({'username': username, 'password': password}).encode()
    encrypted = fernet.encrypt(data)
    with open(credentials_file, 'wb') as f:
        f.write(encrypted)
    # Set secure permissions (readable only by user)
    os.chmod(credentials_file, 0o600)

# Load and decrypt credentials
def load_credentials():
    if os.path.exists(credentials_file) and os.path.exists(key_file):
        try:
            key = load_key()
            fernet = Fernet(key)
            with open(credentials_file, 'rb') as f:
                decrypted_data = fernet.decrypt(f.read())
                data = json.loads(decrypted_data.decode())
                return data.get('username'), data.get('password')
        except Exception:
            pass
    return None, None

# Setup key and credentials
ensure_key()
username, password = load_credentials()
if not username or not password:
    print("Credentials not found. Please enter them.")
    print(f"They will be saved securely in: {config_path}")
    username = get_user_input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    save_credentials(username, password)

# Initialize Firefox browser with Service for GeckoDriver
def setup_firefox_driver():
    # Try to find GeckoDriver in common locations
    common_paths = [
        'geckodriver',  # System PATH
        '/usr/bin/geckodriver',
        '/usr/local/bin/geckodriver',
        './geckodriver',
        resource_path('geckodriver')
    ]
    
    for path in common_paths:
        try:
            if path == 'geckodriver':
                # Try system PATH first
                service = Service()
            else:
                # Try specific path if file exists
                if os.path.exists(path):
                    service = Service(executable_path=path)
                else:
                    continue
            
            driver = webdriver.Firefox(service=service, options=firefox_options)
            print(f"Firefox driver initialized successfully using: {path}")
            return driver
        except Exception as e:
            print(f"Failed to initialize Firefox with {path}: {e}")
            continue
    
    raise Exception("GeckoDriver not found. Please install it or place it in the script directory.")

driver = setup_firefox_driver()

async def main():
    try:
        # Open the Wi-Fi login page
        driver.get('http://192.0.2.1/login.html')  # Replace with actual login IP

        # Wait for the page to fully load
        await asyncio.sleep(2)

        # Find the username and password fields
        username_field = driver.find_element(By.NAME, 'username')
        password_field = driver.find_element(By.NAME, 'password')

        # Enter the credentials
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submit the form
        password_field.send_keys(Keys.RETURN)

        # Wait to complete login
        await asyncio.sleep(3)

        # Check if login succeeded
        if "Login Error" in driver.page_source:
            print("Login failed.")
        else:
            print("Login successful!")

    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        driver.quit()

if __name__ == "__main__":
    asyncio.run(main())