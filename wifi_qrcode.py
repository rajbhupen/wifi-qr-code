import qrcode

# Define your WiFi credentials
wifi_ssid = "wifi_ssid"
wifi_password = "wifi_password"
wifi_security = "WPA"  # Change to "WEP" or "nopass" if needed

# Define the QR code content as a string
qr_code_content = f"WIFI:S:{wifi_ssid};T:{wifi_security};P:{wifi_password};;"

# Generate the QR code with more control
qr = qrcode.QRCode(
    version=1,  # Version of the QR code (1-40, 1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
    box_size=10,  # Size of each box in the QR code
    border=4,  # Border thickness
)
qr.add_data(qr_code_content)
qr.make(fit=True)

# Create an image from the QR Code instance
qr_image = qr.make_image(fill="black", back_color="white")

# Save the QR code as an image file
qr_image.save("wifi_qr_code.png")

print("QR code generated and saved as wifi_qr_code.png")
