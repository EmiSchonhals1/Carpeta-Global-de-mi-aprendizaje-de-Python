import qrcode

link = input("Ingrese el link de lo que quiera enlazar al QR: ")

data = link

img = qrcode.make(data)

img.save("QR\\qr_usuario.png")


