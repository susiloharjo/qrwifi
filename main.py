import qrcode

ssid = "yourwifi"
password = "yourpass"

wifi_data = f"WIFI:T:WPA;S:{ssid};P:{password};;"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(wifi_data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("wifi_qr.png")
