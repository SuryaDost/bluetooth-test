
1234567890
11111111
111111111
1111111111
12345678
123456789
000000111
9771370810
123456
12345
123456789
password
iloveyou
princess
import asyncio
from bleak import BleakScanner


async def scan_and_choose_device():
    print("Scanning for Bluetooth devices...")
    devices = await BleakScanner.discover()

    # Display the found devices
    for i, device in enumerate(devices):
        print(f"{i + 1}: {device.name} - {device.address}")

    # User input to choose a device
    choice = int(input("Select a device by number: ")) - 1
    if 0 <= choice < len(devices):
        selected_device = devices[choice]
        print(f"You selected: {selected_device.name} - {selected_device.address}")
        return selected_device
    else:
        print("Invalid choice. Please try again.")
        return None


# Run the function
asyncio.run(scan_and_choose_device())
