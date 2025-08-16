import smtplib
import random
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_otp_with_timer(receiver_email):
    # กำหนดระยะเวลาให้ OTP ใช้งาน (30 วินาที)
    OTP_VALIDITY_DURATION = 30  # 30 วินาที

    # สุ่ม OTP 6 หลัก
    otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])

    # เวลาที่ OTP ถูกสร้าง
    otp_creation_time = time.time()

    # ข้อความที่จะส่งในอีเมล
    sender_email = 'basketballscoresheet.official@gmail.com'
    sender_password = 'akmg zmum nerj iftq'

    # สร้างข้อความอีเมล
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'Your OTP code from Basketball Score Sheet to verify your email'

    # ใช้ HTML เพื่อทำให้ OTP เป็นตัวหนา
    body = f'Your OTP code is <br><br><b>{otp}</b><br><br>This OTP will expire in 3 minutes.'  # <b> ใช้ทำให้ตัวหนา
    message.attach(MIMEText(body, 'html'))  # เปลี่ยนเป็น 'html' เพื่อให้สามารถใช้ HTML ได้

    try:
        # เชื่อมต่อกับเซิร์ฟเวอร์ SMTP ของ Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # เปิดการเข้ารหัสการเชื่อมต่อ
        server.login(sender_email, sender_password)

        # ส่งอีเมล
        server.sendmail(sender_email, receiver_email, message.as_string())
        print(f'OTP sent to {receiver_email}')
        server.quit()
    except Exception as e:
        print(f'Error: {e}')

    # ฟังก์ชันการตรวจสอบว่า OTP ยังใช้ได้ภายในเวลา 30 วินาทีหรือไม่
    def is_otp_valid():
        current_time = time.time()
        return (current_time - otp_creation_time) <= OTP_VALIDITY_DURATION

    # ทดสอบการตรวจสอบ OTP หลังจากเวลาผ่านไป
    return otp, otp_creation_time, is_otp_valid


if __name__ == "__main__":
    receiver_email = 'kantaphit17@gmail.com'

    # เรียกฟังก์ชัน send_otp_with_timer
    otp, otp_creation_time, is_otp_valid = send_otp_with_timer(receiver_email)

    print(f'Generated OTP: {otp}')
