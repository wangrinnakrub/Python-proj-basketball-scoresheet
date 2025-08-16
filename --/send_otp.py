import smtplib
import random
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# กำหนดค่าบัญชี Gmail ที่ใช้ส่ง
GMAIL_SENDER_EMAIL = "basketballscoresheet.official@gmail.com"
GMAIL_APP_PASSWORD = "akmg zmum nerj iftq"

# ตั้งค่า SMTP ของ Gmail (ใช้ส่งไปทุกโดเมน)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

otp_data = {}  # เก็บข้อมูล OTP ของแต่ละอีเมล

def send_otp_email(recipient_email):
    """ ส่ง OTP ไปยังอีเมลปลายทาง (ใช้ Gmail เป็นตัวส่ง) """
    max_requests = 3
    request_limit_duration = timedelta(minutes=15)
    cooldown_period = timedelta(seconds=30)

    # ตรวจสอบการร้องขอ OTP
    if recipient_email in otp_data:
        user_data = otp_data[recipient_email]
        if 'last_request_time' in user_data and datetime.now() < user_data['last_request_time'] + cooldown_period:
            return 'Please wait before requesting a new OTP.'

        if datetime.now() < user_data['first_request_time'] + request_limit_duration:
            if user_data['request_count'] >= max_requests:
                wait_minutes = (user_data['first_request_time'] + request_limit_duration - datetime.now()).total_seconds() // 60
                return f"Request limit reached. Try again after {int(wait_minutes)} minutes."
            else:
                user_data['request_count'] += 1
        else:
            user_data['request_count'] = 1
            user_data['first_request_time'] = datetime.now()
    else:
        otp_data[recipient_email] = {'request_count': 1, 'first_request_time': datetime.now()}

    # สร้าง OTP
    otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    otp_data[recipient_email]['otp'] = otp
    otp_data[recipient_email]['expires_at'] = datetime.now() + timedelta(minutes=3)
    otp_data[recipient_email]['last_request_time'] = datetime.now()

    # อ่านไฟล์ HTML สำหรับอีเมล
    with open("C:/Users/ASUS/OneDrive/Desktop/code/html/otp_style.html", "r", encoding="utf-8") as file:
        body = file.read()

    body = body.replace("{{ otp_code }}", otp)

    # ตั้งค่าอีเมล
    msg = MIMEMultipart()
    msg['From'] = GMAIL_SENDER_EMAIL
    msg['To'] = recipient_email
    msg['Subject'] = 'Your OTP Code for Verification'
    msg.attach(MIMEText(body, 'html'))

    # ส่งอีเมลผ่าน SMTP ของ Gmail
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(GMAIL_SENDER_EMAIL, GMAIL_APP_PASSWORD)
        server.sendmail(GMAIL_SENDER_EMAIL, recipient_email, msg.as_string())
        server.quit()
        return 'OTP email sent successfully'
    except Exception as e:
        return f"Failed to send OTP email: {e}"

def verify_otp(recipient_email, input_otp):
    """ ตรวจสอบ OTP """
    if recipient_email in otp_data:
        if datetime.now() > otp_data[recipient_email]['expires_at']:
            del otp_data[recipient_email]
            return 'OTP has expired.'
        elif otp_data[recipient_email]['otp'] == input_otp:
            del otp_data[recipient_email]
            return 'OTP is valid!'
        else:
            return 'Invalid OTP.'
    return 'No OTP found for this email.'

def time_until_next_request(recipient_email):
    """ ตรวจสอบเวลาที่เหลือก่อนขอ OTP ใหม่ """
    cooldown_period = timedelta(seconds=30)
    if recipient_email in otp_data and 'last_request_time' in otp_data[recipient_email]:
        next_request_time = otp_data[recipient_email]['last_request_time'] + cooldown_period
        time_left = (next_request_time - datetime.now()).total_seconds()
        return max(0, time_left)
    return 0

def get_otp_request_count(recipient_email):
    if recipient_email in otp_data:
        return otp_data[recipient_email]['request_count']
    else:
        return 0
