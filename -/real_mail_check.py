import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_otp(length=6):
    otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    return otp

def send_otp_via_email_reset_password(receiver_email, otp):
    sender_email = 'basketballscoresheet.official@gmail.com'
    sender_password = 'akmg zmum nerj iftq'

    # สร้างข้อความอีเมล
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'Your OTP code from Basketball Score Sheet for reset password'

    body = f'Your OTP code is {otp}'
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        server.sendmail(sender_email, receiver_email, message.as_string())
        print(f'OTP sent to {receiver_email}')
        server.quit()
    except smtplib.SMTPRecipientsRefused as e:
        print(f"Recipient address {receiver_email} refused: {e}")
    except smtplib.SMTPAuthenticationError as e:
        print(f"Authentication error: {e}")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    receiver_email = 'inactiveemail@provider.com'
    otp = generate_otp()
    print(f'Generated OTP: {otp}')
    send_otp_via_email_reset_password(receiver_email, otp)
