import os
import smtplib
from twilio.rest import Client

# Define variables
MY_PHONE = "+44"

# Define local variables
TWILIO_PHONE = os.environ["TWILIO_PHONE"]
TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_EMAIL_PASSWORD"]

# Use Gmail to send email
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(
        user=MY_EMAIL,
        password=MY_PASSWORD
    )
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Subject:Happy Birthday\n\n...to you!"
    )

# Use Twilio to send text message
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
message = client.messages.create(
    body="It's going to rain today you doofus.",
    from_=TWILIO_PHONE,
    to=MY_PHONE,
)

# Print result
print(message.status)
