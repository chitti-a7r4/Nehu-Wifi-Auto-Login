# NEHU WiFi Auto-Login (macOS Safari)

A Python script that automatically logs into NEHU WiFi using Safari WebDriver on macOS. The script securely stores your credentials and handles the login process automatically.

## Features

- ✅ **Automatic WiFi Login** - Logs into NEHU WiFi portal automatically
- ✅ **Secure Credential Storage** - Encrypts and stores credentials locally
- ✅ **Native Safari Integration** - Uses built-in Safari WebDriver (no external drivers needed)
- ✅ **Cross-platform File Paths** - Follows macOS conventions for data storage
- ✅ **Error Handling** - Comprehensive error checking and user guidance

## Prerequisites

### System Requirements
- **macOS** (tested on macOS 10.14+)
- **Safari** (any recent version)
- **Python 3.7+**

### Python Dependencies
```bash
pip install selenium cryptography
```

### Safari WebDriver Setup
Safari WebDriver comes built-in with macOS, but needs to be enabled:

1. **Enable Developer Menu**:
   - Open Safari
   - Go to `Safari > Preferences > Advanced`
   - Check "Show Develop menu in menu bar"

2. **Enable Remote Automation**:
   - Go to `Develop > Allow Remote Automation`

3. **Enable safaridriver**:
   ```bash
   safaridriver --enable
   ```

## Installation

1. **Clone or download** the script
2. **Install dependencies**:
   ```bash
   pip install selenium cryptography
   ```
3. **Enable Safari WebDriver** (see prerequisites above)
4. **Update the login URL** in the script if needed

## Usage

### First Run
```bash
python nehu_wifi_login.py
```

On first run, you'll be prompted to enter your credentials:
```
Credentials not found. Please enter them. (They will be saved securely in ~/Library/Application Support/NEHU_WiFi)
Enter username: your_username
Enter password: [hidden input]
```

### Subsequent Runs
```bash
python nehu_wifi_login.py
```

The script will automatically use your saved credentials.

## Configuration

### Login URL
Update the login URL in the script if your network uses a different address:
```python
driver.get('http://192.0.2.1/login.html')  # Replace with actual login IP
```

### Form Field Names
If your login form uses different field names, update these:
```python
username_field = driver.find_element(By.NAME, 'username')
password_field = driver.find_element(By.NAME, 'password')
```

## File Locations

The script stores encrypted credentials in:
```
~/Library/Application Support/NEHU_WiFi/
├── credentials.enc  # Encrypted credentials
└── key.key         # Encryption key
```

## Security

- **Encryption**: Credentials are encrypted using Fernet (AES 128)
- **Local Storage**: All data stored locally on your machine
- **No Network Transmission**: Credentials never leave your device except for login
- **Secure Input**: Password input is hidden using `getpass`

## Troubleshooting

### "Safari WebDriver is not enabled"
```bash
# Run this command and restart Safari
safaridriver --enable
```

### "Unable to read input"
Make sure you're running the script from Terminal, not an IDE or other environment.

### "Login failed"
1. Check your credentials are correct
2. Verify the login URL is correct
3. Check if the form field names match your login page

### "An error occurred"
1. Ensure Safari WebDriver is enabled
2. Check that Safari is not running in Private Browsing mode
3. Verify network connectivity

## Advanced Usage

### Running at Startup
Add to your shell profile (`.zshrc`, `.bash_profile`):
```bash
alias wifi-login="python /path/to/nehu_wifi_login.py"
```

### Scheduled Execution
Use `cron` or `launchd` to run automatically:
```bash
# Run every 30 minutes
*/30 * * * * /usr/bin/python3 /path/to/nehu_wifi_login.py
```

## Limitations

- **Safari Only**: Designed specifically for Safari WebDriver
- **macOS Only**: Optimized for macOS (may work on other systems with modifications)
- **Limited Options**: Safari WebDriver has fewer configuration options than Chrome
- **Performance**: Safari WebDriver can be slower than Chrome WebDriver

## Contributing

Feel free to submit issues or pull requests for:
- Support for other browsers
- Additional error handling
- UI improvements
- Cross-platform compatibility

## License

This project is provided as-is for educational and personal use.

## Disclaimer

This script is for legitimate network access only. Ensure you have permission to access the network and comply with your institution's IT policies.