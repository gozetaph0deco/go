import qrcode
from qrcode.constants import ERROR_CORRECT_H

URL = "https://gozetaph0deco.github.io/go/"

# High error correction (H = 30%) -> stays scannable even if print is smudged.
qr = qrcode.QRCode(
    version=None,
    error_correction=ERROR_CORRECT_H,
    box_size=20,   # large modules -> crisp at print sizes
    border=4,
)
qr.add_data(URL)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr-code.png")
print("Saved qr-code.png  ->", URL)
print("Image size:", img.size, "px")
