from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sqlite3, re
# from pdf_test import *
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


class History(QMainWindow):
    switch_to_mainwindow_from_history = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Basketball Score Sheet - Set Up Match')
        self.showMaximized()
        self.import_style('C:/Users/ASUS/OneDrive/Desktop/code/python/ED251007/project/style_history.qss')
        self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))

        # self.username = 'navyy'

        self.connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
        self.cursor = self.connection.cursor()

        self.ui()


        QTimer.singleShot(0, self.clear_initial_focus)
        # self.installEventFilter(self)

    def clear_error_label(self):
        self.tournament_name_error_label.setText('')

    def clear_input_box(self):
        self.tournament_name_input_box.clear()

    def clear_initial_focus(self):
        self.setFocus(Qt.FocusReason.OtherFocusReason)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            if obj not in [self.tournament_name_input_box]:
                self.clear_focus_from_all()
        return super().eventFilter(obj, event)

    def clear_focus_from_all(self):
        self.tournament_name_input_box.clearFocus()
        self.setFocus(Qt.FocusReason.OtherFocusReason)

    def import_style(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print(f"Error: Cannot find the file '{file_name}'")

    def ui(self):
        main_widget = QWidget()

        self.addWidgetsToLayout(main_widget)

        self.setCentralWidget(main_widget)

    def addWidgetsToLayout(self, parent):
        self.back_button = QPushButton(parent)
        self.back_button.setGeometry(15,10,40,40)
        self.back_button.setIcon(QIcon("C:\pic\—Pngtree—vector back icon_4267356.png"))
        self.back_button.setIconSize(QSize(25,25))
        self.back_button.setContentsMargins(20,20,0,0)
        self.back_button.setObjectName('back_to_sign_in')
        self.back_button.clicked.connect(self.switch_to_mainwindow_from_history.emit)
        self.back_button.setStyleSheet('''
            QPushButton#back_to_sign_in{
                background: transparent;
                background-color: transparent;
                border:none;
                border-radius: 20px;

            }
            QPushButton#back_to_sign_in:hover{
                background: transparent;
                background-color: rgb(226, 226, 226);
                border:none;
                border-radius: 20px;
            }''')

        self.history_label = QLabel('HISTORY', parent)
        self.history_label.setObjectName('history_label')
        self.history_label.setGeometry(695, 40, 500, 50)
        self.history_label.setStyleSheet('''QLabel#history_label{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 40px;
        }''')

        # *-------------- select team --------------*#
        self.select_team_label = QLabel('Select teams', parent)
        self.select_team_label.setObjectName('select_team_label')
        self.select_team_label.setGeometry(675, 120, 162, 30)
        self.select_team_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.select_team_label.setStyleSheet('''QLabel#select_team_label{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 20px;
        }''')

        self.select_team_combobox = QComboBox(parent)
        self.select_team_combobox.setObjectName('select_team_combobox')
        self.select_team_combobox.setGeometry(632, 170, 250, 35)
        self.select_team_combobox.setCurrentIndex(-1)
        self.select_team_combobox.currentIndexChanged.connect(self._sync_filename_from_combo)

        self.file_name_label = QLabel('File name', parent)
        self.file_name_label.setObjectName('file_name_label')
        self.file_name_label.setGeometry(675, 250, 162, 30)
        self.file_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.file_name_label.setStyleSheet('''QLabel#file_name_label{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 20px;
        }''')

        self.file_name_input_box = QLineEdit(parent)
        self.file_name_input_box.setObjectName('file_name_input_box')
        self.file_name_input_box.setGeometry(632, 295, 250, 35)
        self.file_name_input_box.setPlaceholderText('Enter file name')
        self.file_name_input_box.setClearButtonEnabled(True)
        self.file_name_input_box.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.file_name_input_box.setCursorPosition(0)
        # self.file_name_input_box.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.file_name_input_box.setStyleSheet('''QLineEdit#file_name_input_box{
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 20px;
            border-radius: 8px;
            padding-left: 10px;
        }''')

        self.download_button = QPushButton('Download', parent)
        self.download_button.setObjectName('download_button')
        self.download_button.setGeometry(658, 360, 200, 35)
        self.download_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.download_button.clicked.connect(self.on_download_button_clicked)
        self.download_button.setStyleSheet('''QPushButton#download_button{
            background: transparent;
            background-color: rgb(226, 226, 226);
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 20px;
            border-radius: 8px;
            border: 2px solid rgb(226, 226, 226);
            padding: 5px;
        }''')

    def _sync_filename_from_combo(self):
        text = self.select_team_combobox.currentText().strip()
        if not text:
            return
        # ตัดคำว่า " draw" ด้านท้ายถ้ามี (ไม่สนตัวพิมพ์ใหญ่เล็ก)
        clean = re.sub(r'\s+draw\s*$', '', text, flags=re.IGNORECASE)
        # ใส่เป็นชื่อไฟล์เริ่มต้น (ไม่เติมสกุล)
        self.file_name_input_box.setText(clean)

    def load_match_data(self):
        if not hasattr(self, 'username'):
            return

        self.select_team_combobox.clear()

        # ดึงแมตช์ของ user เรียงตามลำดับเรคคอร์ด (match_id ASC)
        query = """
            SELECT m.match_id, t1.team_name, t2.team_name
            FROM matches m
            JOIN teams t1 ON m.team1_id = t1.team_id
            JOIN teams t2 ON m.team2_id = t2.team_id
            WHERE m.username = ?
            ORDER BY m.match_id ASC
        """
        self.cursor.execute(query, (self.username,))
        rows = self.cursor.fetchall()

        # helper: map ลำดับเรคคอร์ด -> ป้ายรอบ
        def phase_for(record_no: int) -> str:
            if 1 <= record_no <= 16:  return "round16"
            if 17 <= record_no <= 24: return "round8"
            if 25 <= record_no <= 28: return "round4"
            if 29 <= record_no <= 30: return "round2"
            if record_no == 31:       return "winner"
            return "round"  # กรณีเกินจากสโคปที่ระบุ

        # เพิ่มรายการลง combobox พร้อมป้ายรอบด้านหน้า
        for idx, (match_id, team1_name, team2_name) in enumerate(rows, start=1):
            label = phase_for(idx)
            display_text = f"{label} - {team1_name} vs {team2_name}"
            self.select_team_combobox.addItem(display_text, userData=match_id)


    def load_match_data_old(self):
        if not hasattr(self, 'username'):
            return

        self.select_team_combobox.clear()

        query = """
            SELECT m.match_id, t1.team_name, t2.team_name, m.winner
            FROM matches m
            JOIN teams t1 ON m.team1_id = t1.team_id
            JOIN teams t2 ON m.team2_id = t2.team_id
            WHERE m.username = ?
        """
        self.cursor.execute(query, (self.username,))
        matches = self.cursor.fetchall()

        for match_id, team1_name, team2_name, winner in matches:
            display_text = f"{team1_name} vs {team2_name}"
            if winner and str(winner).strip().lower() == "draw":
                display_text += " draw"  # ← ต่อท้ายตามที่ต้องการ
            self.select_team_combobox.addItem(display_text, userData=match_id)

    def is_valid_file_name(self, file_name):
        if not file_name.strip():
            return False, "File name cannot be empty."

        if len(file_name) > 255:
            return False, "File name cannot exceed 255 characters."

        if re.search(r'[\\/:*?"<>|]', file_name):
            return False, "File name contains invalid characters: \\ / : * ? \" < > |"

        reserved_names = [
            "CON", "PRN", "AUX", "NUL",
            "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
            "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"
        ]
        if file_name.upper() in reserved_names:
            return False, f"File name '{file_name}' is reserved and cannot be used."

        return True, "File name is valid."

    # def on_download_button_clicked(self):
    #     file_name = self.file_name_input_box.text()
    #     is_valid, message = self.is_valid_file_name(file_name)

    #     if not is_valid:
    #         QMessageBox.warning(self, "Invalid File Name", message)
    #         return

    #     index = self.select_team_combobox.currentIndex()
    #     if index == -1:
    #         QMessageBox.warning(self, "No Match Selected", "Please select a match to download.")
    #         return
    #     match_id = self.select_team_combobox.itemData(index)

    #     # เอาข้อความจากคอมโบ แล้วตัด " draw" ออกถ้ามี
    #     match_text = self.select_team_combobox.currentText()
    #     match_text_clean = re.sub(r'\s+draw\s*$', '', match_text, flags=re.IGNORECASE)

    #     if " vs " not in match_text_clean:
    #         QMessageBox.warning(self, "Invalid Match", "Invalid match format.")
    #         return
    #     team1_name, team2_name = match_text_clean.split(" vs ", 1)

    #     save_path, _ = QFileDialog.getSaveFileName(
    #         self,
    #         "Save PDF",
    #         f"{file_name}.pdf",
    #         "PDF Files (*.pdf);;All Files (*)"
    #     )

    #     if not save_path:
    #         return

    #     try:
    #         self.export_match_to_pdf(team1_name, team2_name, output_file=save_path)
    #         QMessageBox.information(self, "Success", f"PDF saved successfully at:\n{save_path}")
    #     except Exception as e:
    #         QMessageBox.critical(self, "Error", f"Failed to save PDF:\n{str(e)}")

    def on_download_button_clicked(self):
        # ถ้าผู้ใช้ยังไม่พิมพ์ ให้ดึงจาก combobox มาเป็นค่าเริ่มต้น
        if not self.file_name_input_box.text().strip():
            self._sync_filename_from_combo()

        file_name = self.file_name_input_box.text()
        is_valid, message = self.is_valid_file_name(file_name)
        if not is_valid:
            QMessageBox.warning(self, "Invalid File Name", message)
            return

        # ต้องเลือกแมตช์ก่อน
        index = self.select_team_combobox.currentIndex()
        if index == -1:
            QMessageBox.warning(self, "No Match Selected", "Please select a match to download.")
            return
        match_id = self.select_team_combobox.itemData(index)

        # ดึงข้อความจาก combobox (ตัดคำว่า " draw" ทิ้งก่อนแยกชื่อทีม)
        match_text = self.select_team_combobox.currentText()
        match_text_clean = re.sub(r'\s+draw\s*$', '', match_text, flags=re.IGNORECASE)
        if " vs " not in match_text_clean:
            QMessageBox.warning(self, "Invalid Match", "Invalid match format.")
            return
        team1_name, team2_name = match_text_clean.split(" vs ", 1)

        # ค่า default ให้เริ่มที่โฟลเดอร์ Downloads
        downloads_dir = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DownloadLocation)
        if not downloads_dir:
            downloads_dir = QDir.homePath()  # กันเหนียว
        default_path = QDir(downloads_dir).filePath(f"{file_name}.pdf")

        save_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save PDF",
            default_path,  # ← เริ่มที่ Downloads และใส่ชื่อไฟล์เริ่มต้น
            "PDF Files (*.pdf);;All Files (*)"
        )
        if not save_path:
            return

        try:
            self.export_match_to_pdf(team1_name, team2_name, output_file=save_path)
            QMessageBox.information(self, "Success", f"PDF saved successfully at:\n{save_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save PDF:\n{str(e)}")

    # def export_match_to_pdf(self, team1_name, team2_name, output_file='match_summary_full.pdf'):
    #     conn = sqlite3.connect("C:/Users/ASUS/OneDrive/Desktop/Dabest/basketball_score_sheet.db")
    #     cursor = conn.cursor()

    #     cursor.execute("SELECT team_id, tournament_name FROM teams WHERE team_name = ?", (team1_name,))
    #     t1_data = cursor.fetchone()
    #     cursor.execute("SELECT team_id FROM teams WHERE team_name = ?", (team2_name,))
    #     t2_data = cursor.fetchone()

    #     if not t1_data or not t2_data:
    #         print("❌ ไม่เจอทีมในฐานข้อมูล")
    #         return

    #     team1_id, tournament_name = t1_data
    #     team2_id = t2_data[0]

    #     cursor.execute("""
    #         SELECT match_id, match_date FROM matches
    #         WHERE (team1_id = ? AND team2_id = ?) OR (team1_id = ? AND team2_id = ?)
    #     """, (team1_id, team2_id, team2_id, team1_id))
    #     match = cursor.fetchone()

    #     if not match:
    #         print("❌ ไม่เจอแมตช์ระหว่าง 2 ทีมนี้")
    #         return

    #     match_id, match_date = match

    #     c = canvas.Canvas(output_file, pagesize=A4)
    #     width, height = A4
    #     y = 800

    #     def draw_line(text, size=12, offset=20):
    #         nonlocal y
    #         if y < 50:  # ถ้าใกล้ขอบล่างแล้ว
    #             c.showPage()
    #             y = 800
    #             c.setFont("Helvetica", size)
    #         c.setFont("Helvetica", size)
    #         c.drawString(50, y, text)
    #         y -= offset

    #     draw_line("🏀 Tournament Match Summary", 16, 30)
    #     draw_line(f"Tournament: {tournament_name}")
    #     draw_line(f"Match ID: {match_id} | Match Date: {match_date}")
    #     draw_line(f"{team1_name} (ID: {team1_id}) vs {team2_name} (ID: {team2_id})", 14, 25)
    #     cursor.execute("SELECT winner FROM matches WHERE match_id = ?", (match_id,))
    #     winner_row = cursor.fetchone()
    #     if winner_row:
    #         draw_line(f"🏆 Match Winner: {winner_row[0]}", 13, 25)

    #     draw_line(f"Players for {team1_name}:", 12, 18)
    #     cursor.execute("SELECT player_name, player_number FROM players WHERE team_id = ?", (team1_id,))
    #     for name, number in cursor.fetchall():
    #         draw_line(f" - #{number} {name}", 10, 14)

    #     draw_line(f"Players for {team2_name}:", 12, 18)
    #     cursor.execute("SELECT player_name, player_number FROM players WHERE team_id = ?", (team2_id,))
    #     for name, number in cursor.fetchall():
    #         draw_line(f" - #{number} {name}", 10, 14)

    #     for period in range(1, 5):
    #         draw_line(f"\nPeriod {period}", 13, 20)

    #         cursor.execute("""
    #             SELECT team1_score, team2_score, period_winner FROM scores
    #             WHERE match_id = ? AND period = ?
    #         """, (match_id, period))
    #         result = cursor.fetchone()
    #         if result:
    #             t1_score, t2_score, winner = result
    #             draw_line(f"Score: {team1_name} {t1_score} - {t2_score} {team2_name}", 11)
    #             draw_line(f"Winner: {winner}", 11)

    #         # Timeouts (no LIKE)
    #         draw_line("Timeouts:", 11)
    #         cursor.execute("""
    #             SELECT team_id, time FROM timeouts
    #             WHERE match_id = ? AND period = ? ORDER BY time DESC
    #         """, (match_id, period))
    #         for team_id, time in cursor.fetchall():
    #             draw_line(f" - Team {team_id} @ {time}", 10)

    #         # Substitutions (no LIKE)
    #         draw_line("Substitutions:", 11)
    #         cursor.execute("""
    #             SELECT team_id, player_out, player_in, time FROM substitutions
    #             WHERE match_id = ? AND period = ? ORDER BY time DESC
    #         """, (match_id, period))
    #         for team_id, player_out, player_in, time in cursor.fetchall():
    #             draw_line(f" - Team {team_id}: Out {player_out}, In {player_in} @ {time}", 10)

    #         # Fouls (no LIKE)
    #         # draw_line("Fouls:", 11)
    #         # cursor.execute("""
    #         #     SELECT player_id, time FROM fouls
    #         #     WHERE match_id = ? AND period = ? ORDER BY time DESC
    #         # """, (match_id, period))
    #         # for player_id, time in cursor.fetchall():
    #         #     draw_line(f" - Player {player_id} @ {time}", 10)
    #         # Fouls (with team name)

    #         draw_line("Fouls:", 11)
    #         cursor.execute("""
    #             SELECT player_id, time FROM fouls
    #             WHERE match_id = ? AND period = ? ORDER BY time DESC
    #         """, (match_id, period))
    #         for player_id, time in cursor.fetchall():
    #             cursor.execute("SELECT team_id FROM players WHERE player_id = ?", (player_id,))
    #             team_row = cursor.fetchone()
    #             if team_row:
    #                 foul_team_id = team_row[0]
    #                 if foul_team_id == team1_id:
    #                     foul_team_name = team1_name
    #                 elif foul_team_id == team2_id:
    #                     foul_team_name = team2_name
    #                 else:
    #                     foul_team_name = f"ID:{foul_team_id}"
    #             else:
    #                 foul_team_name = "Unknown"
    #             draw_line(f" - Player {player_id} ({foul_team_name}) @ {time}", 10)

    #     c.save()
    #     conn.close()
    #     print(f"✅ สร้าง PDF เรียบร้อย: {output_file}")

    def export_match_to_pdf(self, team1_name, team2_name, output_file='match_summary_full.pdf'):
            conn = sqlite3.connect("C:/Users/ASUS/OneDrive/Desktop/Dabest/basketball_score_sheet.db")
            cursor = conn.cursor()

            # หา team_id
            cursor.execute("SELECT team_id, tournament_name FROM teams WHERE team_name = ?", (team1_name,))
            t1_data = cursor.fetchone()
            cursor.execute("SELECT team_id FROM teams WHERE team_name = ?", (team2_name,))
            t2_data = cursor.fetchone()
            if not t1_data or not t2_data:
                print("❌ ไม่เจอทีมในฐานข้อมูล")
                conn.close()
                return
            team1_id, tournament_name = t1_data
            team2_id = t2_data[0]

            # หา match
            cursor.execute("""
                SELECT match_id, match_date FROM matches
                WHERE (team1_id = ? AND team2_id = ?) OR (team1_id = ? AND team2_id = ?)
            """, (team1_id, team2_id, team2_id, team1_id))
            match = cursor.fetchone()
            if not match:
                print("❌ ไม่เจอแมตช์ระหว่าง 2 ทีมนี้")
                conn.close()
                return
            match_id, match_date = match

            # เตรียม PDF
            c = canvas.Canvas(output_file, pagesize=A4)
            width, height = A4
            y = 800
            def draw_line(text, size=12, offset=20):
                nonlocal y
                if y < 50:
                    c.showPage()
                    y = 800
                    c.setFont("Helvetica", size)
                c.setFont("Helvetica", size)
                c.drawString(50, y, text)
                y -= offset

            # Header
            draw_line("🏀 Tournament Match Summary", 16, 30)
            draw_line(f"Tournament: {tournament_name}")
            draw_line(f"Match ID: {match_id} | Match Date: {match_date}")
            draw_line(f"{team1_name} (ID: {team1_id}) vs {team2_name} (ID: {team2_id})", 14, 25)

            # Winner ทั้งเกม (ถ้ามี) — อนุญาตให้แสดงได้
            cursor.execute("SELECT winner FROM matches WHERE match_id = ?", (match_id,))
            winner_row = cursor.fetchone()
            if winner_row:
                draw_line(f"🏆 Match Winner: {winner_row[0]}", 13, 25)

            # Players
            draw_line(f"Players for {team1_name}:", 12, 18)
            cursor.execute("SELECT player_name, player_number FROM players WHERE team_id = ?", (team1_id,))
            for name, number in cursor.fetchall():
                draw_line(f" - #{number} {name}", 10, 14)

            draw_line(f"Players for {team2_name}:", 12, 18)
            cursor.execute("SELECT player_name, player_number FROM players WHERE team_id = ?", (team2_id,))
            for name, number in cursor.fetchall():
                draw_line(f" - #{number} {name}", 10, 14)

            # สรุปตาม period
            for period in range(1, 5):
                draw_line(f"\nPeriod {period}", 13, 20)

                # Score (เอาเฉพาะสกอร์ ไม่ต้องพิมพ์ winner ของ period)
                cursor.execute("""
                    SELECT team1_score, team2_score FROM scores
                    WHERE match_id = ? AND period = ?
                """, (match_id, period))
                result = cursor.fetchone()
                if result:
                    t1_score, t2_score = result
                    draw_line(f"Score: {team1_name} {t1_score} - {t2_score} {team2_name}", 11)

                # Timeouts
                draw_line("Timeouts:", 11)
                cursor.execute("""
                    SELECT team_id, time FROM timeouts
                    WHERE match_id = ? AND period = ? ORDER BY time DESC
                """, (match_id, period))
                for tid, t in cursor.fetchall():
                    tname = team1_name if tid == team1_id else (team2_name if tid == team2_id else f"ID:{tid}")
                    draw_line(f" - {tname} @ {t}", 10)

                # Substitutions (ทีม, ผู้เล่นออก, ผู้เล่นเข้า, เวลา)
                draw_line("Substitutions:", 11)
                cursor.execute("""
                    SELECT team_id, player_out, player_in, time FROM substitutions
                    WHERE match_id = ? AND period = ? ORDER BY time DESC
                """, (match_id, period))

                def _clean_player_no(tag):
                    """
                    รับค่าอย่าง 'player9_team1' หรือ 'player5_team2' แล้วคืน '9' หรือ '5'
                    ถ้าไม่มีตัวเลข ให้คืนสตริงเดิม
                    """
                    if tag is None:
                        return "?"
                    s = str(tag)
                    m = re.search(r'(\d+)', s)
                    return m.group(1) if m else s

                for tid, p_out, p_in, t in cursor.fetchall():
                    tname = (team1_name if tid == team1_id
                            else team2_name if tid == team2_id
                            else f"ID:{tid}")
                    out_no = _clean_player_no(p_out)
                    in_no  = _clean_player_no(p_in)
                    draw_line(f" - {tname}: out #{out_no}, in #{in_no} @ {t}", 10)

                # Fouls (ทีม, หมายเลขผู้เล่น, เวลา)
                draw_line("Fouls:", 11)
                cursor.execute("""
                    SELECT team, player_id, time FROM fouls
                    WHERE match_id = ? AND period = ? ORDER BY time DESC
                """, (match_id, period))
                for team_val, player_no, t in cursor.fetchall():
                    # team อาจเก็บเป็น 'team1'/'team2' หรือเป็น team_id (int)
                    if isinstance(team_val, str):
                        tname = team1_name if team_val.lower() == "team1" else (team2_name if team_val.lower() == "team2" else team_val)
                    else:
                        tname = team1_name if team_val == team1_id else (team2_name if team_val == team2_id else f"ID:{team_val}")
                    draw_line(f" - {tname}, player #{player_no} @ {t}", 10)

            c.save()
            conn.close()
            print(f"✅ สร้าง PDF เรียบร้อย: {output_file}")

    def fetch_username(self,username):
        self.username = username
        self.load_match_data()


#! ---------- run program --------- #
if __name__ == "__main__":
    app = QApplication([])
    history = History()
    history.show()
    app.exec()
