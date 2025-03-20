import pandas
import smtplib
import os
from email.message import EmailMessage

mainfile = pandas.read_csv("automail.csv")
email_list = mainfile.iloc[:, 1].tolist()
id_list = mainfile.iloc[:, 2].tolist()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("xxxxxxxxxxxxxxxxx@gmail.com", "poqk opgo lems svcn")
subject = "xxxxxxxxxxxxxxxxxxxxxxxxx"
body = "xxxxxxxxxxxxxxxxxxxxxxxxx"
for email, ids in zip(email_list, id_list):
    certificate_file = fr"D:\python\{ids}.pdf" #depends upon the file location
    msg = EmailMessage()
    msg['From'] = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    msg['To'] = email
    msg['Subject'] = subject
    msg.set_content(body)
    if os.path.exists(certificate):
        with open(certificate_file, "rb") as f:
            msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=os.path.basename(certificate))
        server.send_message(msg)
        print(f"Certificate sent to {email}")
    else:
        print(f"Certificate not found for {email} ({certificate})")
server.quit()
