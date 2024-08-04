import qrcode

upi_id = input("Enter your UPI ID: ")
user_name = input("Enter your name: ")
amount = input("Enter the amount: ")
currency = "INR"

# upi://pay?pa=UPI_id&pn=NAME&am=Amount&cu=CURRENCY&tn=MASSAGE
phone_pay_url = f"upi://pay?pa={upi_id}&pn={user_name}&am={amount}&cu={currency}"
paytm_pay_url = f"upi://pay?pa={upi_id}&pn={user_name}&am={amount}&cu={currency}"
google_pay_url = f"upi://pay?pa={upi_id}&pn={user_name}&am={amount}&cu={currency}"

# Create QR codes
phone_pay_QR = qrcode.make(phone_pay_url)
google_pay_QR = qrcode.make(google_pay_url)
paytm_pay_QR = qrcode.make(paytm_pay_url)

# Show the QR codes
phone_pay_QR.show()
paytm_pay_QR.show()
google_pay_QR.show()
