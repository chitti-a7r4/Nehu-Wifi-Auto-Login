# NEHU WiFi Auto-Login (Linux/Firefox)

An automated WiFi login script for Linux systems using Firefox and Selenium WebDriver. This script securely stores your credentials and automatically logs you into captive portal WiFi networks.

## Features

- 🔒 **Secure Credential Storage**: Encrypted credential storage using Fernet encryption
- 🦊 **Firefox Support**: Optimized for Firefox browser with GeckoDriver
- 🐧 **Linux Compatible**: Designed specifically for Linux distributions
- 🔧 **Auto-Detection**: Automatically finds GeckoDriver in common system locations
- 🛡️ **SSL Handling**: Properly configured to handle insecure captive portal connections
- 📁 **XDG Compliant**: Uses standard Linux config directories (`~/.config/nehu_wifi/`)

## Prerequisites

- Python 3.6 or higher
- Firefox browser installed
- Internet connection

## Installation

### 1. Install Python Dependencies

```bash
pip3 install selenium cryptography
```

### 2. Install GeckoDriver

Choose one of the following methods:

#### Method A: Using Package Manager (Recommended)

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install firefox-geckodriver
```

**Fedora/RHEL:**
```bash
sudo dnf install mozilla-geckodriver
```

**Arch Linux:**
```bash
sudo pacman -S geckodriver
```

#### Method B: Manual Installation

```bash
# Download latest GeckoDriver (check https://github.com/mozilla/geckodriver/releases for latest version)
wget https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz

# Extract and install system-wide
tar -xzf geckodriver-v0.33.0-linux64.tar.gz
sudo mv geckodriver /usr/local/bin/
sudo chmod +x /usr/local/bin/geckodriver
```

#### Method C: Local Installation

```bash
# Download and place in script directory
wget https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz
tar -xzf geckodriver-v0.33.0-linux64.tar.gz
chmod +x geckodriver
# Place geckodriver in the same directory as your script
```

### 3. Download and Setup Script

```bash
# Download the script
wget https://example.com/wifi_login.py  # Replace with actual download URL

# Make it executable
chmod +x wifi_login.py
```

## Configuration

### 1. Update Login URL

Edit the script and replace the placeholder URL with your actual WiFi login page:

```python
# Line ~130: Replace with your actual login URL
driver.get('http://192.0.2.1/login.html')  # Replace with actual login IP
```

Common WiFi login URLs:
- `http://192.168.1.1/login.html`
- `http://10.0.0.1/login`
- `http://captive.portal.com/login`

### 2. Update Form Field Names (if needed)

If your login form uses different field names, update these lines:

```python
# Line ~135-136: Update field names if different
username_field = driver.find_element(By.NAME, 'username')
password_field = driver.find_element(By.NAME, 'password')
```

Common alternatives:
- `user`, `login`, `userid` for username
- `pass`, `pwd`, `passphrase` for password

## Usage

### First Run

```bash
python3 wifi_login.py
```

On first run, you'll be prompted to enter your credentials:
```
Credentials not found. Please enter them.
They will be saved securely in: /home/username/.config/nehu_wifi
Enter username: your_username
Enter password: [hidden input]
```

### Subsequent Runs

```bash
python3 wifi_login.py
```

The script will automatically use saved credentials and attempt login.

### Direct Execution

```bash
./wifi_login.py
```

## File Structure

```
~/.config/nehu_wifi/
├── credentials.enc    # Encrypted credentials (600 permissions)
└── key.key           # Encryption key (600 permissions)
```

## Troubleshooting

### Common Issues

#### 1. GeckoDriver Not Found
```
GeckoDriver not found. Please install it or place it in the script directory.
```

**Solution**: Install GeckoDriver using one of the methods above.

#### 2. Firefox Not Found
```
selenium.common.exceptions.WebDriverException: Message: 'firefox' executable needs to be in PATH
```

**Solution**: Install Firefox:
```bash
# Ubuntu/Debian
sudo apt install firefox

# Fedora
sudo dnf install firefox

# Arch Linux
sudo pacman -S firefox
```

#### 3. Permission Denied
```
PermissionError: [Errno 13] Permission denied
```

**Solution**: Make script executable:
```bash
chmod +x wifi_login.py
```

#### 4. SSL Certificate Errors
The script is configured to handle SSL certificate errors common with captive portals. If you encounter issues, check that your login URL is correct.

#### 5. Login Failed
```
Login failed.
```

**Solutions**:
- Verify your username and password are correct
- Check that the login URL is correct
- Ensure the form field names match your login page
- Try accessing the login page manually in Firefox first

### Debug Mode

To see more detailed error messages, run with Python's verbose mode:

```bash
python3 -v wifi_login.py
```

### Reset Credentials

To reset saved credentials:

```bash
rm -rf ~/.config/nehu_wifi/
```

## Security Notes

- Credentials are encrypted using Fernet (AES 128) encryption
- Encryption key and credentials are stored with restricted permissions (600)
- Files are stored in user's config directory, not accessible by other users
- No credentials are transmitted over the network except to the login page

## Advanced Usage

### Running as a Service

Create a systemd service for automatic login:

```bash
# Create service file
sudo nano /etc/systemd/system/wifi-login.service
```

```ini
[Unit]
Description=WiFi Auto Login
After=network.target

[Service]
Type=oneshot
User=your_username
ExecStart=/path/to/wifi_login.py
WorkingDirectory=/path/to/script/directory

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable wifi-login.service
sudo systemctl start wifi-login.service
```

### Cron Job

Run automatically every 5 minutes:
```bash
crontab -e
```

Add:
```bash
*/5 * * * * /path/to/wifi_login.py >/dev/null 2>&1
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
- Check the troubleshooting section above
- Create an issue on the project repository
- Ensure you're using the latest version of the script

## Changelog

### v1.0.0
- Initial Linux release
- Firefox/GeckoDriver support
- Encrypted credential storage
- XDG directory compliance
- SSL error handling for captive portals