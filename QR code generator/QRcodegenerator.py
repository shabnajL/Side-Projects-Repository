import pyqrcode
#import png

# string which represent the QR code
string = "https://youtu.be/IwzkfMmNMpM"
# genrating the QR code
url = pyqrcode.create(string)

# creating and saving the SVG file
url.svg("Dreamers.svg", scale = 8)
# creating and saving the EPS file
url.eps("Dreamers.eps", scale = 2)
print(url.terminal(quiet_zone=1))

# creating and saving the PNG file(not working)
#url.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
#url.show()
