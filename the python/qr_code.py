import qrcode

# Read your HTML file
with open("hello.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# Create QR code
qr = qrcode.QRCode(
    version=None,  # auto-adjust size
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=10,
    border=4,
)

qr.add_data(html_data)
qr.make(fit=True)

# Save QR code image
img = qr.make_image(fill_color="black", back_color="white")
img.save("pusphati_html_qr.png")

print("QR code saved as pusphati_html_qr.png")
