import sys
import usb.core

dev = usb.core.find(find_all=True)

for cfg in dev:
	sys.stdout.write('Decimal      VendorID=' + str(cfg.idVendor) + ' & ProductID=' + str(cfg.idProduct) + '\n')
	sys.stdout.write('Hexadecimal  VendorID=' + hex(cfg.idVendor) + ' & ProductID=' + hex(cfg.idProduct) + '\n')


dev1 = usb.core.find(idVendor = 0x1bae, idProduct = 0x19c)
dev2 = usb.core.find(idVendor = 0x1bae, idProduct = 0x19d)
dev3 = usb.core.find(idVendor = 0x424, idProduct = 0x2534)
devices = [dev1, dev2, dev3]

for devs in devices:
	if devs is None:
		raise ValueError('Device is not connected\n')
	else:	
		print('USB device', devs.idProduct, 'found')
