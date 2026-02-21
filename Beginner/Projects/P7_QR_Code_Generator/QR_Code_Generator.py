


                                            #   QR_Code Generator

# :: Step 0 :-

# - install QR_Code library
# - install pillow library


# :: Step 1 :-

# - user ki upi id as a input leni hai.




# :: Step 2 :-

# - Har payment app ke liye ak url_id define krenge jisme payment_id or kuch details mention hongi.



# :: Step 3 :-

# - Har payment app ke liye ak qr code generate hoga , qrcode.make() function ki help se




# :: Step 4 :-

# - Isme generate kiye gye Qr Code ko save bhi krr payenge image ke form mai apne machine prr.



# :: Step 5 :-

# - Generate kiye hue Qr code ko display krne ke liye ham pillow_viewer ka use krenge.






import qrcode

# Taking UPI ID As a input 
 
upi_id = input("Enter your UPI ID = ")


# UPI ID FORMATE :  upi://pay?pa = UPI_ID&pn=NAME&am=Amount&cu = CURRENCY&tn = MESSAGE

# --> Defining the payment URL based on the UPI ID and the payment app.
# --> You can modify these URLs based on the payment apps you want to support.


phonepe_url = f'upi://pay?pa ={upi_id}&pn=Recipient%20Name&mc = 1234'
paytm_url = f'upi://pay?pa ={upi_id}&pn=Recipient%20Name&mc = 1234'
google_pay_url = f'upi://pay?pa ={upi_id}&pn=Recipient%20Name&mc = 1234'


# Create QR Codes for each payment app

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Save the Qr Code to image file ( optional )

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')


# Display the QR codes ( You may need to install PIL / Pillow Library)

phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()