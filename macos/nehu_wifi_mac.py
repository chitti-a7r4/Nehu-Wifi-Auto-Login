import sys
import os
import asyncio
import platform
import getpass
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.safari.options import Options
from selenium.webdriver.safari.service import Service
from cryptography.fernet import Fernet
import time

# Function to safely get user input
def get_user_input(prompt):
    try:
        return input(prompt)
    except EOFError:
        print("Error: Unable to read input. Please run the script from a terminal.")
        sys.exit(1)

# Configure Safari options
safari_options = Options()
# Note: Safari has limited options compared to Chrome
# Most security-related options are not available in Safari WebDriver

# Set file paths for macOS
if platform.system() == "Darwin":  # macOS
    home_dir = os.path.expanduser("~")
    app_support_path = os.path.join(home_dir, "Library", "Application Support", "NEHU_WiFi")
else:
    # Fallback for other systems
    app_support_path = os.path.join(os.getenv("HOME", "."), ".nehu_wifi")

credentials_file = os.path.join(app_support_path, "credentials.enc")
key_file = os.path.join(app_support_path, "key.key")

# Ensure directory exists
os.makedirs(app_support_path, exist_ok=True)

# Generate and save encryption key if it doesn't exist
def ensure_key():
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, 'wb') as f:
            f.write(key)

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

# Check if Safari WebDriver is enabled
def check_safari_webdriver():
    try:
        # Try to create a Safari driver instance briefly
        test_driver = webdriver.Safari()
        test_driver.quit()
        return True
    except Exception as e:
        print("\nSafari WebDriver is not enabled or not available.")
        print("To enable Safari WebDriver:")
        print("1. Open Safari")
        print("2. Go to Safari > Preferences > Advanced")
        print("3. Check 'Show Develop menu in menu bar'")
        print("4. Go to Develop > Allow Remote Automation")
        print("5. Run this in Terminal: safaridriver --enable")
        print(f"\nError details: {str(e)}")
        return False

# Setup key and credentials
ensure_key()
username, password = load_credentials()
if not username or not password:
    print("Credentials not found. Please enter them. (They will be saved securely in ~/Library/Application Support/NEHU_WiFi)")
    username = get_user_input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    save_credentials(username, password)

# Check Safari WebDriver availability
if not check_safari_webdriver():
    sys.exit(1)

# Initialize Safari browser
service = Service()
driver = webdriver.Safari(service=service, options=safari_options)

async def main():
    try:
        print("Opening Wi-Fi login page...")
        # Open the Wi-Fi login page
        driver.get('http://192.0.2.1/login.html')  # Replace with actual login IP

        # Wait for the page to fully load
        await asyncio.sleep(3)

        print("Entering credentials...")
        # Find the username and password fields
        username_field = driver.find_element(By.NAME, 'username')
        password_field = driver.find_element(By.NAME, 'password')

        # Clear fields and enter the credentials
        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)

        # Submit the form
        password_field.send_keys(Keys.RETURN)

        # Wait to complete login
        await asyncio.sleep(3)

        # Check if login succeeded
        if "Login Error" in driver.page_source or "error" in driver.page_source.lower():
            print("Login failed. Please check your credentials.")
        else:
            print("Login successful!")

    except Exception as e:
        print("An error occurred:", str(e))
        print("Make sure Safari WebDriver is properly enabled.")
    finally:
        print("Closing browser...")
        driver.quit()

if __name__ == "__main__":
    if platform.system() != "Darwin":
        print("Warning: This script is designed for macOS. Some features may not work properly on other systems.")
    
    asyncio.run(main())