import qrcode 


qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=30,border=10
                 )

qr.add_data("https://open.spotify.com/user/31e2bszlu4s324e75uvgi5yacg34?si=HBjBhL8gSbm_HX9qXd0Z9w")

qr.make(fit=True)
img=qr.make_image(fill_color="indigo",back_color="white")

img.save("Sotify.png")