import os
import pickle
import google.auth
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# SCOPES ของ Google API ที่ต้องการเข้าถึง
SCOPES = ['https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email']

def google_login():
    """ ทำการล็อกอินผ่าน Google OAuth 2.0 """
    creds = None
    # เช็คว่าไฟล์ token.pickle มีอยู่หรือไม่ (ไฟล์ token นี้เก็บ token ของผู้ใช้หลังจากล็อกอินแล้ว)asdqwd
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # ถ้าไม่มี token หรือหมดอายุ ให้เริ่มกระบวนการ OAuthasd
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # เริ่ม OAuth Flow และรับ credentials ใหม่จาก client_secret.json
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # บันทึก credentials ลงในไฟล์ token.pickle
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # เชื่อมต่อกับ Google API และดึงข้อมูลผู้ใช้
    try:
        # สร้าง service object สำหรับ Google API
        service = build('people', 'v1', credentials=creds)
        profile = service.people().get(resourceName='people/me').execute()

        # ดึงข้อมูลโปรไฟล์
        print(f'Name: {profile["names"][0]["displayName"]}')
        print(f'Email: {profile["emailAddresses"][0]["value"]}')

    except Exception as e:
        print(f'Error fetching profile: {e}')

if __name__ == '__main__':
    google_login()
