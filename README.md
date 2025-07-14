# NEHU Wi-Fi Auto Login
A simple and lightweight tool that **automatically logs in to the NEHU Wi-Fi captive portal**, available for **Android**, **Windows PC**, **Linux**, and **macOS**.

This repository currently offers **APK and EXE builds only**. The source code is **closed** for now.

## 📥 Download
You can download the latest builds from the [Releases](../../releases) section.

## 📥 Download
You can download the latest builds from the [Releases](../../releases) section.

| Platform            | File                         | Version | Updated     | Browser Required             | Status              |
|---------------------|------------------------------|---------|-------------|------------------------------|----------------------|
| **Android**         | `.apk`                       | v1.0.0  | 05-07-2025  | Built-in WebView             | ✅ **Stable**         |
| **Windows – Edge**  | `NEHU_WiFi_Setup.exe`        | v1.0.0  | 05-07-2025  | Microsoft Edge (preinstalled) | ✅ **Stable**         |
| **Windows – Chrome**| `NEHU_WiFi_Setup_Chrome.exe` | v1.0.0  | 05-07-2025  | Google Chrome                | ✅ **Stable**         |
| **Linux**           | `linux.zip`                     | v0.9.0  | 05-07-2025  | Firefox / Chrome             | 🧪 **Under Testing**  |
| **macOS**           | `macos.zip`                     | v0.9.0  | 05-07-2025  | Safari / Chrome              | 🧪 **Under Testing**  |

> ⚠️ *Linux and macOS builds are located in their respective folders.*

## 🚀 Features
✅ **One-time credential setup** - Enter once, use forever  
✅ **Auto-login to NEHU Wi-Fi captive portal** - No more manual logins  
✅ **Secure credential storage** - Encrypted on PC, local on Android  
✅ **Cross-platform support** - Android, Windows, Linux & macOS compatibility  
✅ **Lightweight & fast** - Minimal resource usage  
✅ **NEHU-optimized** - Tailored specifically for campus network  

## 🔐 Security & Privacy
**Your credentials never leave your device:**
- 🔒 **PC (Windows)**: AES encrypted storage in `%LOCALAPPDATA%\NEHU_WiFi`
- 🔒 **Linux**: Encrypted storage in `~/.config/nehu-wifi/`
- 🔒 **macOS**: Keychain integration for secure credential storage
- 🔒 **Android**: Stored locally with Android security features
- 🚫 **No ads, no trackers, no data collection**
- 🌐 **No server interaction** - Everything works offline

## 🖥️ PC Version Details
**System Requirements:**
- Windows 10/11 (64-bit)
- Microsoft Edge (preinstalled) OR Google Chrome

**Installation:**
1. Download the appropriate `.exe` file
2. Run the installer
3. Enter your NEHU credentials once
4. The app will run and login whenever you need

**Storage Location:** `C:\Users\[YourName]\AppData\Local\NEHU_WiFi\`

## 🐧 Linux Version Details *(Under Testing)*
**System Requirements:**
- Ubuntu 20.04+ / Debian 11+ / Fedora 35+ / Arch Linux
- Firefox or Chrome browser
- `curl` and `bash` (usually pre-installed)

**Installation:**
- Follow instructions provided under folder

**Storage Location:** `~/.config/nehu-wifi/`

## 🍎 macOS Version Details *(Under Testing)*
**System Requirements:**
- macOS 11.0+ (Big Sur or later)
- Safari or Chrome browser
- Terminal access

**Installation:**
- Follow instructions provided under folder

**Storage Location:** Keychain (secure system storage)

## 📱 Android Version Details
**Requirements:**
- Android 6.0+ (API level 23+)
- ~5MB storage space

**Installation:**
1. Download the `.apk` file
2. Enable "Install from unknown sources" if prompted
3. Install and grant necessary permissions
4. Enter credentials once - you're set!

## 🔧 How It Works
1. **Detection**: App opens when you tap 
2. **Authentication**: Fills in your saved credentials
3. **Verification**: Confirms successful login

## ⚠️ Disclaimer
This tool is developed independently by **Shiva Sai Naluvala** and is **not affiliated with NEHU's IT department**. 
- Use at your own discretion
- Intended to help fellow students save time
- For personal use by NEHU students only
- **Linux/macOS versions are currently under testing** - report issues if encountered

## 💬 Support & Feedback
Having issues or suggestions? Reach out:
- 📧 **Email:** shivasainaluvala@gmail.com
- 🐛 **Bug Reports:** Create an issue in this repository
- 🧪 **Testing Feedback:** Especially welcomed for Linux/macOS versions

## ❤️ Support My Work
If this tool saves you time, consider supporting:
**UPI ID:** `chitticoc@ybl`

Your support helps keep student-built tools like this alive! 🙏

## 📝 Important Notes
- ⚠️ **Use latest version only** - Older builds may not work
- 🎓 **NEHU students only** - Respect the intended usage
- 🔄 **Check for updates** - New builds fix issues and add features
- 🧪 **Linux/macOS testers needed** - Help improve cross-platform compatibility

---
*Built with ❤️ for the NEHU community*
