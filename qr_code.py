'''
This project was guided by Codédex guide 'Generate a QR Code with Python'

'''

import qrcode

website_link= input("paste the link for the qr code:")

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)

qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color = 'black', back_color = 'white')
name= input("give file a name: ")
img.save(name + ".png")