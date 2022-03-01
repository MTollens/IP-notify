# IP-notify
A bash + Python script to autonomously update the developer of a device's IP change

created for the development of an autonomous robot, on my campus's wireless network, where we were unable to assign the device a static IP address.
also useful for devices that need to send infrequent but important updates. we would often be in the middle of debugging the device in a hallway via a VNC connection 
when the network would reassign it to a new IP. causing much headache. this script means if the VNC connection was lost I could expect a message that would inform me of the new address and we could keep working. without having to plug in a monitor and keyboard.

the main program is a simple loop that runs forever and checks the device's currently assigned IP address.
if the address is determined to have changed, then the program calls a second python subprocess to send a short message via the Telegram API.
the IP address is pulled from IFCONFIG via the Ubuntu Bash terminal.

written for Ubuntu Linux but usable on other setups with minor changes
