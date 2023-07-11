import qrcode

data = "https://www.youtube.com/watch?v=mCdA4bJAGGk"

img = qrcode.make(data)

img.save("QR\\qr_hello_world.png")