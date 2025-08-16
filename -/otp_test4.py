import smtplib
import random
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# สร้างตัวแปรเก็บข้อมูล OTP, เวลาหมดอายุ, และจำนวนครั้งที่ร้องขอ OTP
otp_data = {}
sender_email = "basketballscoresheet.official@gmail.com"
password = "akmg zmum nerj iftq"

def send_otp_email(recipient_email):
    # ตั้งค่าจำนวนครั้งที่ขอ OTP ได้สูงสุด และช่วงเวลาจำกัด
    max_requests = 3
    request_limit_duration = timedelta(minutes=15)
    cooldown_period = timedelta(seconds=30)

    # ตรวจสอบข้อมูลผู้ใช้ใน otp_data
    if recipient_email in otp_data:
        user_data = otp_data[recipient_email]

        # ตรวจสอบช่วงเวลาคูลดาวน์ 30 วินาที
        if 'last_request_time' in user_data:
            if datetime.now() < user_data['last_request_time'] + cooldown_period:
                print("Please wait 30 seconds before requesting a new OTP.")
                return

        # หากยังไม่หมดเวลา 15 นาที ตรวจสอบจำนวนครั้งที่ขอ OTP
        if datetime.now() < user_data['first_request_time'] + request_limit_duration:
            if user_data['request_count'] >= max_requests:
                print("Request limit reached. Try again after 15 minutes.")
                return
            else:
                # เพิ่มจำนวนครั้งที่ขอ OTP
                user_data['request_count'] += 1
        else:
            # หากเลย 15 นาที ให้รีเซ็ตจำนวนครั้งและตั้งค่าเวลาเริ่มต้นใหม่
            user_data['request_count'] = 1
            user_data['first_request_time'] = datetime.now()
    else:
        # สร้างข้อมูลใหม่หากอีเมลนี้ยังไม่เคยร้องขอ OTP
        otp_data[recipient_email] = {
            'request_count': 1,
            'first_request_time': datetime.now()
        }

    # สร้างรหัส OTP แบบสุ่ม
    otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    otp_data[recipient_email]['otp'] = otp
    otp_data[recipient_email]['expires_at'] = datetime.now() + timedelta(minutes=3)
    otp_data[recipient_email]['last_request_time'] = datetime.now()

    # อ่านไฟล์ HTML
    with open("C:/Users/ASUS/OneDrive/Desktop/code/html/otp_style.html", "r", encoding="utf-8") as file:
        body = file.read()

    # แทนที่ placeholder {{ otp_code }} ด้วยค่า otp_code จริง
    body = body.replace("{{ otp_code }}", otp)

    # สร้างเมลแบบ MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = 'Your OTP Code for Verification'

    # เพิ่มเนื้อหาลงในอีเมล
    msg.attach(MIMEText(body, 'html'))

    # ส่งอีเมลผ่าน SMTP
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print("OTP email sent successfully")
    except Exception as e:
        print(f"Failed to send OTP email: {e}")

def verify_otp(recipient_email, input_otp):
    # ตรวจสอบว่า OTP หมดอายุหรือยัง
    if recipient_email in otp_data:
        if datetime.now() > otp_data[recipient_email]['expires_at']:
            print("OTP has expired.")
            del otp_data[recipient_email]  # ลบ OTP ที่หมดอายุ
        elif otp_data[recipient_email]['otp'] == input_otp:
            print("OTP is valid!")
            del otp_data[recipient_email]  # ลบ OTP ที่ใช้แล้ว
        else:
            print("Invalid OTP.")
    else:
        print("No OTP found for this email.")

# ใช้งานฟังก์ชันส่งอีเมล
send_otp_email("kantaphit17@gmail.com")

# รอ 5 วินาทีเพื่อจำลองการขอ OTP ใหม่
time.sleep(5)
send_otp_email("kantaphit17@gmail.com")  # จะส่งได้เพราะผ่าน 30 วินาทีแล้ว

# รอให้ผู้ใช้กรอก OTP
time.sleep(5)  # จำลองการหน่วงเวลาในการกรอก OTP
print(otp_data)
verify_otp("kantaphit17@gmail.com", input("Enter OTP: "))
print(otp_data)
