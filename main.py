import smtplib
import yagmail

#Need to provide location of our smtp server
#Gmail = 'smtp.gmail.com'
#Hotmail = 'smtp.live.com'
#Outlook = 'outlook.office365.com'
#Yahoo = 'smtp.mail.yahoo.com'
my_email = "jfrancone.automail@gmail.com"
#Gmail uses implicit ssl so you must use port 465 to send the messages
port1_SSL = 465
port2_TLS = 587
Subject = "Automatic Email"
Content = "Hello! This email was sent through python code :)"
with open ("pw.txt") as file:
    password = file.readline()



#Makes our connection secure
#You can't use this with gmail as it uses implicit SSl instead of tsl but is still pretty secure
#connection.starttls()

# try:
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
#         #connection.login(user = my_email, password = password)
#         #connection.starttls()
#         connection.login(user = my_email, password = password)
#         connection.sendmail(from_addr=my_email, to_addrs="jfrancone.automail@yahoo.com", msg ="Hello")

# except:
#     print("Connection Error.")

# else:
#     print("Email sent successfully")



with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
    connection.login(user = my_email, password = password)
    #connection.login(user = my_email, password = password)
    connection.sendmail(from_addr=my_email, to_addrs="jfrancone.automail@yahoo.com", msg =f"Subject: {Subject} \n\n{Content}")

