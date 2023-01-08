"""
FritzBox Tray - A system tray application for interacting with FRITZ!Box devices.
Copyright (C) 2023 Andreas Violaris

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
from requests import Session, RequestException
from pystray import Icon, Menu, MenuItem
from PIL import Image
import pkg_resources

tray = None


def send_soap_request(service, action):
    """
    Send a SOAP request to the FRITZ!Box device.

    Args:
    service (str): The name of the service to send the request to.
    action (str): The name of the action to perform.

    Returns:
    str: The text of the response to the SOAP request. If an exception occurs while
    sending the request, a string describing the error will be returned instead.
    """

    url = "http://fritz.box:49000/igdupnp/control/WANIPConn1"
    headers = {
        "Content-Type": "text/xml; charset=utf-8",
        "SOAPACTION": f"urn:schemas-upnp-org:service:{service}#{action}"
    }
    data = f"""
                <?xml version="1.0" encoding="UTF-8"?>
                <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" 
                 s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
                   <s:Body>
                      <u:{action} xmlns:u="urn:schemas-upnp-org:service:{service}" />
                   </s:Body>
                </s:Envelope>
            """

    with Session() as session:
        try:
            response = session.post(url=url, headers=headers, data=data)
            return response.text
        except (ConnectionError, RequestException) as exc:
            return f"Error sending SOAP request: {exc}"


def parse_ip_from_xml(xml_string: str) -> str:
    """
    Parse the external IP address from an XML string.

    Args:
    xml_string (str): The XML string to parse the external IP address from.

    Returns:
    str: The external IP address if found, or a string indicating that it was not found.
    """

    try:
        start_index = xml_string.index("<NewExternalIPAddress>") + len("<NewExternalIPAddress>")
        end_index = xml_string.index("</NewExternalIPAddress>")
        ip_address = xml_string[start_index:end_index]
    except ValueError:
        ip_address = "Not found."
    return ip_address


def get_external_ip_address() -> None:
    """
    Retrieve and display the external IP address of the FRITZ!Box device.

    This function sends a SOAP request to the FRITZ!Box device to retrieve the external
    IP address of the device. The response to the request is expected to contain the
    external IP address, which is then extracted and displayed using a notification.

    Returns:
    None
    """

    response = send_soap_request("WANIPConnection:1", "GetExternalIPAddress")
    ip_address = parse_ip_from_xml(response)
    tray.notify(title="Current IP Address", message=ip_address if response else 'Failed!')


def reconnect_fritzbox() -> None:
    """
    Reconnect the FRITZ!Box device.

    This function sends a SOAP request to the FRITZ!Box device to terminate the current
    Internet connection and establish a new one. The result of the reconnection attempt
    is displayed using a notification.

    Returns:
    None
    """

    response = send_soap_request("WANIPConnection:1", "ForceTermination")
    tray.notify(title="Reconnection Result",
                message='Succeeded!' if "ForceTerminationResponse" in response else 'Failed!')


def terminate():
    """
    Terminate the current process.

    This function stops the current process.

    Returns: None
    """
    tray.stop()


def main():
    global tray
    tray = Icon("FritzBox Tray")
    tray.icon = Image.open(pkg_resources.resource_filename(__name__, 'resources/ft.ico'))
    get_external_ip_address_item = MenuItem("Display Current IP Address", get_external_ip_address)
    reconnect_item = MenuItem("Reconnect", reconnect_fritzbox)
    exit_item = MenuItem("Quit", terminate)
    menu = Menu(get_external_ip_address_item,
                reconnect_item,
                exit_item)
    tray.menu = menu
    tray.run()


if __name__ == "__main__":
    main()
