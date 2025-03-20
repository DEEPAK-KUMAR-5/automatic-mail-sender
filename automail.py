import pandas as pd
import os as os
import smtplib
df = pd.read_csv("automail.csv")
second_column = df.iloc[:, 1].tolist()
server= smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("dk020402007@gmail.com", "poqk opgo lems svcn")
message = "hi this ia an automated mail from team GDG"
for i in second_column:
    server.sendmail("dk020402007@gmail.com",i, message)
    print("mail sent to f{i}")
server.quit()
    