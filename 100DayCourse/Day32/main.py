# import smtplib

# my_email = "huandrew321@gmail.com"
# password = "urwzaavdhowlenbu"

# """
# Gmail: smtp.gmail.com

# Hotmail: smtp.live.com

# Outlook: outlook.office365.com

# Yahoo: smtp.mail.yahoo.com
# """

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls() # make the connection secure
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="huandrew02@gmail.com", 
#         msg="Subject:Hello\n\nThis is the content of my email."
#     )


# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# if year == 2023:
#     print("No need to wear a face mask now.")
# print(day_of_week)

# date_of_birth = dt.datetime(year=2002, month=4, day=1)
# print(f"My date of birth is {date_of_birth}")


# ----------------------------Monday Motivation-------------------------
# import random
# import datetime as dt
# import smtplib

# my_email = "huandrew321@gmail.com"
# password = "urwzaavdhowlenbu"

# now = dt.datetime.now()
# weekday = now.weekday()

# if weekday == 0:
#     with open("quotes.txt") as file:
#         quotes = file.readlines()
#         random_quote = random.choice(quotes)

#     print(random_quote)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls() # make the connection secure
#         connection.login(user=my_email, password=password)
#         connection.sendmail(
#             from_addr=my_email, 
#             to_addrs="huandrew02@gmail.com", 
#             msg=f"Subject:Monday Motivation\n\n{random_quote}"
#         )

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
import random
import datetime as dt
import smtplib
import os
import pandas as pd

my_email = "huandrew321@gmail.com"
password = "urwzaavdhowlenbu"

# Step 2: Check if today matches a birthday in birthdays.csv
def check_birthday_today():
    today = dt.date.today()
    birthdays_df = pd.read_csv('birthdays.csv')
    today_matches = birthdays_df[
        (birthdays_df['month'] == today.month) &
        (birthdays_df['day'] == today.day)
    ]
    return today_matches

# Step 3: Generate a letter with [NAME] replaced by the person's name
def generate_letter(name):
    template_folder = 'letter_templates'
    template_files = os.listdir(template_folder)
    chosen_template_filename = random.choice(template_files)
    chosen_template_path = os.path.join(template_folder, chosen_template_filename)
    with open(chosen_template_path, 'r') as template_file:
        letter_template = template_file.read()
    return letter_template.replace('[NAME]', name)

# Step 4: Send the generated letter to the person's email address
def send_letter(email, letter_content):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # make the connection secure
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=email, 
            msg=f"Subject:Happy Birthday!\n\n{letter_content}"
        )

# Main program
if __name__ == "__main__":
    today_matches = check_birthday_today()
    if not today_matches.empty:
        for index, row in today_matches.iterrows():
            name = row['name']
            email = row['email']
            letter = generate_letter(name)
            send_letter(email, letter)



