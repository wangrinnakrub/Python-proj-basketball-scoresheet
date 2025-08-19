from PyQt6.QtWidgets import *
# from PyQt6.QtCore import *
from PyQt6.QtCore import Qt, QRect, QPropertyAnimation, pyqtProperty
from PyQt6.QtGui import *
import sys
import traceback

from sign_in import Signin_page
from sign_up import Signup_page
from create_account import Create_account
from forgot_password import Forgot_password_page
from otp_check import *
from reset_password import Reset_password
from z_main_window_1 import *
from zz_create_team import *
from z_tournament_32 import *
from zzz_set_up_match import *
from zzzz_competition import *
from history import *

class OTPThread(QThread):
    otp_sent = pyqtSignal(str)

    def __init__(self, email):
        super().__init__()
        self.email = email

    def run(self):
        import time
        time.sleep(1)
        self.otp_sent.emit(self.email)


class MainApp(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Basketball Score Sheet')
        self.setWindowIcon(QIcon(r"C:/pic/basketball-ball.png"))

        self.connection = sqlite3.connect(r'C:/Users/ASUS/OneDrive/Desktop/Dabest/basketball_score_sheet.db')
        self.cursor = self.connection.cursor()

        self.sign_in = Signin_page()
        self.sign_up = Signup_page()
        self.create_account = Create_account()
        self.forgot_password = Forgot_password_page()
        self.otp_check = otp_check()
        self.reset_password = Reset_password()
        self.main_window = Main_window()
        self.create_team = Create_team()
        self.tournament32 = tournament32()
        self.set_up_match = Set_up_match()
        self.competition = Competition()
        self.history = History()

        self.addWidget(self.sign_in)
        self.addWidget(self.sign_up)
        self.addWidget(self.otp_check)
        self.addWidget(self.create_account)
        self.addWidget(self.forgot_password)
        self.addWidget(self.reset_password)
        self.addWidget(self.main_window)
        self.addWidget(self.create_team)
        self.addWidget(self.tournament32)
        self.addWidget(self.set_up_match)
        self.addWidget(self.competition)
        self.addWidget(self.history)

        self.setCurrentWidget(self.sign_in)
        # self.setGeometry(280, 90, 700, 650)

        # sign in
        self.sign_in.switch_to_forgot_password.connect(self.sign_in_switch_to_forgot_password)
        self.sign_in.switch_to_main_window.connect(self.switch_to_main_window)
        self.sign_in.switch_to_sign_up.connect(self.sign_in_switch_to_sign_up)

        # Sign up
        self.sign_up.switch_to_sign_in.connect(lambda: self.switch_with_animation_from_left(self.sign_in))
        # self.sign_up.switch_to_sign_in.connect(lambda: self.change_to(self.sign_in))
        self.sign_up.switch_to_otp_check.connect(self.switch_to_otp_check)

        # otp check
        self.otp_check.switch_to_create_account.connect(self.switch_to_create_account)
        self.otp_check.switch_to_sign_up.connect(lambda: self.switch_with_animation_from_left(self.sign_up))
        self.otp_check.switch_to_reset_password.connect(self.switch_to_reset_password)

        # create account
        self.create_account.switch_to_sign_up.connect(self.switch_to_sign_up)
        self.create_account.switch_to_sign_in.connect(self.switch_to_sign_in_create_account)

        # forgot password
        self.forgot_password.switch_to_sign_in.connect(self.switch_to_sign_in)
        self.forgot_password.switch_to_otp_check.connect(self.switch_to_otp_check_forgot_password)

        # reset password
        self.reset_password.switch_to_forgot_password.connect(self.switch_to_forgot_password)
        self.reset_password.switch_to_sign_in.connect(self.switch_to_sign_in_reset_password)

        # main window 1
        self.main_window.switch_to_sign_in.connect(self.switch_to_sign_in_from_main_window)
        self.main_window.switch_to_tournament_32.connect(self.switch_to_tournament_32)
        self.main_window.switch_to_history.connect(self.switch_to_history)

        # tournament 32
        self.tournament32.switch_to_create_team_from_tournament_32_.connect(lambda team_name, team_id: self.switch_to_create_team_from_tournament_32(team_name, team_id))
        self.tournament32.switch_to_main_window.connect(lambda : self.switch_with_animation_from_left(self.main_window))
        self.tournament32.switch_to_set_up_match_from_tournament_32.connect(self.switch_to_set_up_match_from_tour32)

        # create team
        self.create_team.switch_to_tournament32.connect(lambda team_id, team_name: self.switch_to_tournament_32_from_create_team(team_id, team_name))
        self.create_team.switch_to_tournament32_normal.connect(self.switch_to_tournament_32_from_create_team_normal)

        # set up match
        self.set_up_match.switch_to_tournament_32_from_set_up_match.connect(self.switch_to_tournament_32_from_set_up_match_)
        self.set_up_match.switch_to_competition_from_set_up_match.connect(self.switch_to_competition_from_set_up_match_)

        # competition
        self.competition.switch_to_match_set_up_from_competition.connect(self.switch_to_match_set_up_from_competition_)
        self.competition.switch_to_tournament_32_from_competition.connect(self.switch_to_tournament_32_from_competition_)

        # history
        self.history.switch_to_mainwindow_from_history.connect(self.switch_to_mainwindow_from_history)



    def change_to(self,page):
        self.setCurrentWidget(page)

# ----------------------------------------------------------------- #

    def sign_in_switch_to_forgot_password(self):
        self.sign_in.username_input_box_normal_border()
        self.sign_in.password_input_box_normal_border()
        self.sign_in.clear_error_label()
        self.sign_in.clear_username_password_focus()
        self.switch_with_animation_from_right(self.forgot_password)

    def sign_in_switch_to_sign_up(self):
        self.sign_in.username_input_box_normal_border()
        self.sign_in.password_input_box_normal_border()
        self.sign_in.clear_error_label()
        self.sign_in.clear_username_password_focus()
        self.switch_with_animation_from_right(self.sign_up)

# ----------------------------------------------------------------- #

    def on_otp_sent(self, email):
        self.otp_check.receive_data_from_sign_up(email)

    def send_otp(self):
        email = self.sign_up.fetch_user_data()

        self.otp_thread = OTPThread(email)
        self.otp_thread.otp_sent.connect(self.on_otp_sent)
        self.otp_thread.start()

    def switch_to_otp_check(self):
        self.switch_with_animation_from_right(self.otp_check)
        QTimer.singleShot(0, self.send_otp)

# ----------------------------------------------------------------- #

    def on_otp_sent_forgot_password(self, email):
        self.otp_check.receive_data_from_forgot_password(email)

    def send_otp_forgot_password(self):
        email = self.forgot_password.fetch_email()

        self.otp_thread = OTPThread(email)
        self.otp_thread.otp_sent.connect(self.on_otp_sent_forgot_password)
        self.otp_thread.start()

    def switch_to_otp_check_forgot_password(self):
        self.switch_with_animation_from_right(self.otp_check)
        QTimer.singleShot(0, self.send_otp_forgot_password)

# ----------------------------------------------------------------- #

    def switch_to_sign_up(self):
        self.otp_check.clear_input_boxs()
        self.create_account.clear_input_boxs()
        self.switch_with_animation_from_left(self.sign_up)

    def switch_to_sign_in_create_account(self):
        self.otp_check.clear_input_boxs()
        self.create_account.clear_input_boxs()
        self.sign_up.clear_input_boxs()
        self.switch_with_animation_from_right(self.sign_in)

# ----------------------------------------------------------------- #

    def switch_to_create_account(self):
        fullname,phonenumber,email = self.sign_up.fetch_all_user_data()
        self.create_account.receive_data_from_sign_up_in_create_account(fullname,phonenumber,email)
        self.switch_with_animation_from_right(self.create_account)

    def switch_to_reset_password(self):
        email = self.forgot_password.fetch_email()
        self.reset_password.receive_data_from_forgot_password(email)
        self.switch_with_animation_from_right(self.reset_password)

    def switch_to_sign_in(self):
        self.otp_check.clear_input_boxs()
        self.switch_with_animation_from_left(self.sign_in)

# ----------------------------------------------------------------- #

    def switch_to_forgot_password(self):
        self.otp_check.clear_input_boxs()
        self.reset_password.clear_input_boxs()
        self.switch_with_animation_from_left(self.forgot_password)

    def switch_to_sign_in_reset_password(self):
        self.forgot_password.clear_input_boxs()
        self.otp_check.clear_input_boxs()
        self.reset_password.clear_input_boxs()
        self.switch_with_animation_from_left(self.sign_in)

# ----------------------------------------------------------------- #

    def switch_to_main_window(self):
        username_or_email = self.sign_in.fetched_username()
        self.username = username_or_email
        self.main_window.fetch_username(username_or_email)
        self.sign_in.clear_username_password_focus()
        self.switch_with_animation_from_right(self.main_window)

# ----------------------------------------------------------------- #

    def switch_to_sign_in_from_main_window(self):
        self.sign_in.clear_input_box()
        self.sign_in.clear_focus_from_all()
        self.switch_with_animation_from_left(self.sign_in)
        # test for thunwa

# ----------------------------------------------------------------- #

    def switch_to_create_team_from_tournament_32(self, team_name, team_id):
        print('🔁 ไป create_team ครั้งแรก team_name' ,team_name)
        # if team_id is None:
        #     print("⚠️ team_id เป็น None, ตั้งค่าเป็น 0 แทน")
        #     team_id = 0
        print(f"🛠 ถูกเรียก switch_to_create_team_from_tournament_32: team_id = {team_id}")
        # traceback.print_stack()
        if hasattr(self, "create_team"):
            self.create_team.deleteLater()

        print(f"🔍 ก่อนสร้าง Create_team: team_id = {team_id}")
        self.create_team = Create_team(team_id)
        # self.create_team.switch_to_tournament32.connect(self.switch_to_tournament_32_from_create_team)

        if team_name == 'ทีมที่เคยมีข้อมูล':
            print('หน้าดูข้อมูล')
            print(f"✅ โหลดข้อมูลทีม {team_name} (Team ID: {team_id})")
            self.create_team.switch_to_tournament32_normal.connect(self.switch_to_tournament_32_from_create_team_normal)
            self.cursor.execute("SELECT team_name FROM teams WHERE team_id = ?",(team_id,))
            team_name = self.cursor.fetchone()[0]
            self.create_team.load_team_data(team_name, team_id)
            self.create_team.prepare_for_team_view()
        elif team_name == 'สร้างทีมใหม่':
            print("🚀 หน้าเพิ่มข้อมูลใหม่")
            self.create_team.switch_to_tournament32.connect(lambda team_id, team_name: self.switch_to_tournament_32_from_create_team(team_id, team_name))
            self.create_team.switch_to_tournament32_normal.connect(self.switch_to_tournament_32_from_create_team_normal)
            self.create_team.prepare_for_team_creation()

        self.addWidget(self.create_team)
        self.switch_with_animation_from_right(self.create_team)

# ----------------------------------------------------------------- #

    def switch_to_tournament_32(self):
        self.cursor.execute("SELECT COUNT(*) FROM tournament WHERE username = ?", (self.username,))
        tournament_count = self.cursor.fetchone()[0]

        if tournament_count > 0:
            self.cursor.execute("""
                SELECT match_id, winner
                FROM matches
                WHERE username = ?
            """, (self.username,))
            match_results = self.cursor.fetchall()

            if len(match_results) == 48:
                match_winners = {match_id: winner for match_id, winner in match_results}
                winners_round_8 = [None] * 8
                for i in range(0, 16, 2):
                    match_id = (i // 2) + 33
                    if match_id in match_winners and match_winners[match_id]:
                        winners_round_8[i // 2] = match_winners[match_id]

                    self.tournament32.update_round_8_buttons(winners_round_8)
                    print("อัพเดทปุ่มรอบ 8 ทีมเรียบร้อย")
                else:
                    print("ยังไม่มี match id ครบ 48 คู่ ไม่อัพเดทปุ่มรอบ 8")

                self.switch_with_animation_from_right(self.tournament32)

            if len(match_results) == 32:
                match_winners = {match_id: winner for match_id, winner in match_results}
                winners_round_32 = [None] * 16
                for i in range(0, 32, 2):
                    match_id = (i // 2) + 1
                    if match_id in match_winners and match_winners[match_id]:
                        winners_round_32[i // 2] = match_winners[match_id]

                self.tournament32.update_round_16_buttons(winners_round_32)
                self.tournament32.fetch_usernames(self.username)
                self.tournament32.load_team_button(self.username)
            else:
                print("ยังไม่มี match id ครบ 32 คู่ ไม่อัพเดทปุ่มรอบ 32")
        else:
            print("ยังไม่มี tournament ใน database")

        self.switch_with_animation_from_right(self.tournament32)

# ----------------------------------------------------------------- #

    def switch_to_tournament_32_from_create_team(self, team_id, team_name):
        if team_id is not None and team_name is not None:
            print(f"🔁 กลับมาที่ tournament32: team_id = {team_id}, team_name = {team_name}")
            self.tournament32.update_team_button(team_id,self.username, team_name)
        else:
            print("\n⚠️ team_id หรือ team_name เป็น None, ไม่ทำการอัพเดท\n")
        self.switch_with_animation_from_left(self.tournament32)

    def switch_to_tournament_32_from_create_team_normal(self):
        print('back แบบธรรมดา')
        self.switch_with_animation_from_left(self.tournament32)

# ----------------------------------------------------------------- #

    def switch_to_set_up_match_from_tour32(self):
        self.set_up_match.get_username(self.username)
        self.switch_with_animation_from_right(self.set_up_match)

# ----------------------------------------------------------------- #

    def switch_to_tournament_32_from_set_up_match_(self):
        self.set_up_match.select_team_disconnect()
        self.switch_with_animation_from_left(self.tournament32)

    def switch_to_competition_from_set_up_match_(self):
        username = self.set_up_match.fetch_username()
        self.competition.get_username(username)
        # team1_info = self.set_up_match.get_team1_info()
        # team2_info = self.set_up_match.get_team2_info()
        # self.competition.set_initial_players(team1_info, team2_info)
        self.switch_with_animation_from_right(self.competition)

# ----------------------------------------------------------------- #

    def switch_to_match_set_up_from_competition_(self):
        self.switch_with_animation_from_left(self.set_up_match)

    def switch_to_tournament_32_from_competition_(self):
        self.cursor.execute("""
            SELECT match_id, winner
            FROM matches
            WHERE username = ?
        """, (self.username,))
        match_results = self.cursor.fetchall()

        match_winners = {match_id: winner for match_id, winner in match_results}

        winners_round_32 = [None] * 16
        for i in range(0, 32, 2):
            match_id = (i // 2) + 1
            if match_id in match_winners:
                winner = match_winners[match_id]
                if winner:
                    winners_round_32[i // 2] = winner

        self.tournament32.update_round_16_buttons(winners_round_32)
        self.tournament32.hide_set_up_match_button()
        self.switch_with_animation_from_right(self.tournament32)

# ----------------------------------------------------------------- #

    def switch_to_history(self):
        self.history.fetch_username(self.username)
        # self.history.load_match_history()
        self.switch_with_animation_from_right(self.history)

    def switch_to_mainwindow_from_history(self):
        self.switch_with_animation_from_left(self.main_window)


# todo------------------------------------------- animation ---------------------------------------------- #

    def switch_with_animation_from_right(self, new_widget):

        new_widget.setGeometry(self.width(), 0, self.width(), self.height())
        self.setCurrentWidget(new_widget)

        self.animation = QPropertyAnimation(new_widget, b"pos")
        self.animation.setDuration(300)
        self.animation.setStartValue(QPoint(self.width(), 0))
        self.animation.setEndValue(QPoint(0, 0))

        self.animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.animation.start()

    def switch_with_animation_from_left(self, new_widget):

        new_widget.setGeometry(-self.width(), 0, self.width(), self.height())
        self.setCurrentWidget(new_widget)

        self.animation = QPropertyAnimation(new_widget, b"pos")
        self.animation.setDuration(300)
        self.animation.setStartValue(QPoint(-self.width(), 0))
        self.animation.setEndValue(QPoint(0, 0))

        self.animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.animation.start()



app = QApplication(sys.argv)
main_app = MainApp()
# main_app.show()
main_app.showMaximized()
sys.exit(app.exec())
