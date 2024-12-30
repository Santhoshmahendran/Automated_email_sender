import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd

# Email sender credentials
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'santhoshm2000411@gmail.com'
EMAIL_PASSWORD = 'iqfb tusa kakr nbhe'

# Load recipient data from a CSV file
recipients_file = 'recipients.csv'
recipients = pd.read_csv(recipients_file)

# Email details
subject = "Your Subject Here"
body = """
Dear {name},

This is a sample bulk email sent using Python. 
We hope this message finds you well!

Best regards,
Your Team
"""

# Sending emails
def send_bulk_emails():
    try:
        # Set up SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        for index, row in recipients.iterrows():
            # Create email
            msg = MIMEMultipart()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = row['email']
            msg['Subject'] = subject

            # Personalize the email body
            personalized_body = body.format(name=row['name'])
            msg.attach(MIMEText(personalized_body, 'plain'))

            # Send email
            server.send_message(msg)
            print(f"Email sent to {row['name']} ({row['email']})")

        # Close the server
        server.quit()
        print("All emails sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the script
if __name__ == "__main__":
    send_bulk_emails()
