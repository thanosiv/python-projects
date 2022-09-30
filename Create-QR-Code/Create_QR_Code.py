import pyqrcode

# Let the user provide the string/URL/etc. for what to convert to QR Code
qrstring = input('Enter the string for which you want to convert to a QR Code:')

# Convert the text provided by the user to a QR Code
convertstr = pyqrcode.create(qrstring)

# Save the QR Code as a file called "qr.svg" in the same directory as this .py file
convertstr.svg("qr.svg", scale = 8)
