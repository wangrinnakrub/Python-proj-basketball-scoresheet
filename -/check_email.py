import smtplib
import dns.resolver

def check_email_exists(email):
    try:
        domain = email.split('@')[1]
        records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(records[0].exchange)

        # กำหนดให้เชื่อมต่อกับ Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587, timeout=20)
        server.starttls()  # เริ่มการเข้ารหัส TLS
        server.helo()
        server.mail('wangrinnakrub.9@gmail.com')  # ใส่อีเมลจริงที่คุณใช้งาน
        code, message = server.rcpt(email)
        server.quit()

        if code == 250:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error occurred: {e}")
        return False

# ทดสอบการทำงาน
email = "kantaphit17@gmail.com"  # ใส่อีเมลที่ต้องการตรวจสอบasd
try:
    result = check_email_exists(email)
    if result:
        print("Email exists!")
    else:
        print("Email does not exist.")
except Exception as e:
    print(f"Error occurred during execution: {e}")
