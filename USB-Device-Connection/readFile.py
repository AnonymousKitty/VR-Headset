import sys
import usb.core
import usb.util


dev1 = usb.core.find(idVendor = 0x1bae, idProduct = 0x19c)
dev2 = usb.core.find(idVendor = 0x1bae, idProduct = 0x19d)
dev3 = usb.core.find(idVendor = 0x424, idProduct = 0x2534)
devices = [dev1, dev2, dev3]

for devs in devices:
	if devs is None:
		raise ValueError('Device is not connected\n')
	else:	
		print('USB device', devs.idProduct, 'found')

device = dev3
# the following code is copied from http://steventsnyder.com/reading-a-dymo-usb-scale-using-python/		

# use the first/default configuration
device.set_configuration()
# first endpoint
endpoint = device[0][(0,0)][0]

# read a data packet
attempts = 10
data = None
while data is None and attempts > 0:
    try:
        data = device.read(endpoint.bEndpointAddress,
                           endpoint.wMaxPacketSize)
    except usb.core.USBError as e:
        data = None
        if e.args == ('Operation timed out',):
            attempts -= 1
            continue

print(data)

