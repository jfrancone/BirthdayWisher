import smtplib
import datetime as dt
import random
import pandas as pd
import os
import unicodedata as ud
import re
import urllib.parse

class Engine():
    def __init__(self):
        self.birthday_people = []
        
        #Email Setup
        self.my_email = "jfrancone.automail@gmail.com"
        #Gmail uses implicit ssl so you must use port 465 to send the messages
        self.port1_SSL = 465
        self.port2_TLS = 587
        self.Subject = "Happy Birthday!"
        self.Content = None
        with open ("pw.txt") as file:
            self.password = file.readline()

        #Finding the Day of the Week
        self.now = dt.datetime.now()
        self.day_of_week = self.now.weekday()

        #Retrieving information from birthdays.csv
        self.birthday_df = pd.read_csv("birthdays.csv")
        self.birthday_dict = self.birthday_df.to_dict(orient = 'records')
        #print(birthday_dict)

    def run(self):
        #print("Program Running")
        for item in self.birthday_dict:
            if item['month'] == self.now.month and item['day'] == self.now.day:
                #print("Today is your birthday!")
                birthday_person = item['name']
                print(f"Today is your birthday, {birthday_person}!")
                self.birthday_people.append(birthday_person)
        self.get_random_letter()
        #print(self.birthday_people)
    
    def get_random_letter(self):
        #print("Getting Random Letter")
        for person in self.birthday_people:
            self.recipient = self.birthday_df[self.birthday_df.name == person] 
            print(self.recipient)
            recipient_index = self.birthday_df.index[self.birthday_df['name'] == person].tolist()
            recipient_index = recipient_index[0]
            #print(type(recipient_index))
            #print(recipient_index)
            self.recipient_email = self.birthday_df.at[recipient_index, 'email']
            print(self.recipient_email)
            self.letter = random.choice(os.listdir("/Users/jfran/code/Birthday-Wisher/letter_templates/"))
            #print(self.letter)

            for i in range(len(self.letter)):
                with open(f"letter_templates/{self.letter}") as letter_file:
                    self.letter_content = letter_file.read()
                    self.letter_content = self.letter_content.replace('[NAME]', person)
                    #self.letter_content = (self.letter_content).encode('utf-8').strip()
                    
                    
                    #self.letter_content = re.sub(r"[^\x00-\x7F]+", "", self.letter_content)
            print(self.letter_content)
            print(type(self.letter_content))
                    #self.letter_content = (self.letter_content).encode('utf-8')
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
                connection.login(user = self.my_email, password = self.password)
                #connection.login(user = my_email, password = password)
                connection.sendmail(
                    from_addr=self.my_email, 
                    to_addrs=self.recipient_email, 
                    msg =f"Subject: {self.Subject} \n\n{self.letter_content}")
            
            #print(self.letter_content)
            
                

        #print(self.letter_content)

        


    
    
#print(contents)
#print(type(contents))

#todays_quote = random.choice(contents)

#print(todays_quote)
# if day_of_week == 5:
#     print("Today is Saturday!")

#Makes our connection secure
#You can't use this with gmail as it uses implicit SSl instead of tsl but is still pretty secure
#connection.starttls()

# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
#     connection.login(user = my_email, password = password)
#     #connection.login(user = my_email, password = password)
#     connection.sendmail(from_addr=my_email, to_addrs="jfrancone.automail@yahoo.com", msg =f"Subject: {Subject} \n\n{Content}")
