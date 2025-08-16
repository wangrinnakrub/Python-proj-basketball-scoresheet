import smtplib,random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_otp_email(recipient_email):
    # ตั้งค่าอีเมล
    sender_email = "basketballscoresheet.official@gmail.com"
    password = "akmg zmum nerj iftq"

    otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
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

# ใช้งานฟังก์ชัน
send_otp_email("kantaphit17@gmail.com")
