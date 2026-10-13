# Assignment 5: Personal QR Code Generator (qrcode)
import qrcode

message = input("Enter your name or message: ")
qr1 = qrcode.make(message)
qr1.save("message.png")
print("Message QR code saved!")

website = input("Enter a website URL: ")
qr2 = qrcode.make(website)
qr2.save("website.png")
print("Website QR code saved!")
