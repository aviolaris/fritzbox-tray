# FritzBox Tray

### A system tray application for interacting with FRITZ!Box devices.

![fritzbox-tray](https://user-images.githubusercontent.com/48277853/211208943-1cbb41fb-60a7-44d1-a697-5d0493bb167c.png)

![python-versions](https://img.shields.io/pypi/pyversions/fritzbox-tray)

![status](https://img.shields.io/pypi/status/fritzbox-tray)
[![license](https://img.shields.io/pypi/l/fritzbox-tray?color=blueviolet)](https://github.com/aviolaris/fritzbox-tray/blob/master/LICENSE)
![format](https://img.shields.io/pypi/format/fritzbox-tray?color=blueviolet)
[![pypi-downloads](https://img.shields.io/pypi/dm/fritzbox-tray?color=brightgreen&label=pypi%20downloads)](https://pypistats.org/packages/fritzbox-tray)

## Features

- Display current external IP address
- Reconnect FRITZ!Box device
- Quit application

## Requirements

- Python 3.6 or higher

## Installation

To install FritzBox Tray, run the following command:

    pip install fritzbox-tray

## Usage

To start FritzBox Tray:

 - **On Windows**, the application can be run from any location. Simply double-click the `fritzbox-tray.exe` (usually located in `%LOCALAPPDATA%\Programs\Python\Python##\Scripts` or run the `fritzbox-tray` command from the command prompt.


 - **On Linux**, it is necessary to navigate to the application's folder path (usually located in `~/.local/bin`) before running the application, using the `./fritzbox-tray` command.

This will place an icon in the system tray. Right-clicking on the icon will display a menu with the following options:

 - **Display Current IP Address**: Display a notification with the current external IP address of the FRITZ!Box device


 - **Reconnect**: Terminate and re-establish the Internet connection of the FRITZ!Box device


 - **Quit**: Close the application

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


