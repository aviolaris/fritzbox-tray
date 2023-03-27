# FritzBox Tray

### A system tray application for interacting with FRITZ!Box devices.

[![fritzbox-tray](https://user-images.githubusercontent.com/48277853/211208943-1cbb41fb-60a7-44d1-a697-5d0493bb167c.png)](https://github.com/aviolaris/fritzbox-tray)

![python-versions](https://img.shields.io/pypi/pyversions/fritzbox-tray)
![code-size](https://img.shields.io/github/languages/code-size/aviolaris/fritzbox-tray)
![repo-size](https://img.shields.io/github/repo-size/aviolaris/fritzbox-tray)

![status](https://img.shields.io/pypi/status/fritzbox-tray)
[![license](https://img.shields.io/pypi/l/fritzbox-tray?color=blueviolet)](https://github.com/aviolaris/fritzbox-tray/blob/master/LICENSE)
![format](https://img.shields.io/pypi/format/fritzbox-tray?color=blueviolet)
[![pypi-downloads](https://img.shields.io/pypi/dm/fritzbox-tray?color=brightgreen&label=pypi%20downloads)](https://pypistats.org/packages/fritzbox-tray)

## Features

- Display current external IP address
- Renew IP address

## Requirements

- Python 3.6 or higher

## Installation

To install FritzBox Tray, run the following command:

    pip install fritzbox-tray

## Usage

To launch FritzBox Tray:

 - **On Windows**, double-click the `fritzbox-tray.exe` (usually located in `%LOCALAPPDATA%\Programs\Python\Python##\Scripts` or run the `fritzbox-tray` command from the command prompt.


 - **On Linux**, double-click the `fritzbox-tray` (usually located in `~/.local/bin`) or run the `./fritzbox-tray` command from the terminal.

Once the program is running, an icon will be added to the system tray. By right-clicking on the icon, a menu will appear containing the following options:

 - **Display Current IP Address**: This option will trigger a notification displaying the current external IP address of the FRITZ!Box device.


 - **Reconnect**: This option allows you to instantly obtain a new IP address by terminating and re-establishing the Internet connection.


 - **Quit**: This option enables you to close the application.

## Common Issues

#### "ValueError: Namespace AppIndicator3 not available" (Linux Only)

This error message indicates that the `AppIndicator3` module, which the application uses to display tray icons on Linux, is not available on your system.

To resolve this issue, you will need to install the `libayatana-appindicator3-dev` package, which provides the necessary files and libraries for the `AppIndicator3` module. To install the package, use the following command:

    sudo apt-get install libayatana-appindicator3-dev


## Contribution

Pull requests and issues are welcome.

## License

This project is licensed under the GNU General Public License v3.0.

See the [LICENSE](https://github.com/aviolaris/fritzbox-tray/blob/master/LICENSE) file for details.


