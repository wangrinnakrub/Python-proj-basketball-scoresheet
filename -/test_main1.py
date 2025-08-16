from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys

class ScoreSheetApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basketball Score Sheet")
        self.setGeometry(100, 60, 1000, 700)
        # self.import_style('style_main_window.qss')

        # Variables to store scores and time
        self.home_score = 0
        self.away_score = 0
        self.quarter_scores = {"1st": [0, 0], "2nd": [0, 0], "3rd": [0, 0], "4th": [0, 0]}  # Format: {Quarter: [Home, Away]}
        self.current_time = 10 * 60  # 10 minutes in seconds
        self.current_quarter_index = 0  # Index of quarters (0 = 1st Quarter)
        self.quarters = ["1st", "2nd", "3rd", "4th"]
        self.timer_running = False

        # Main layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Header Section: Game Info
        game_info_layout = QHBoxLayout()

        # Home Team Section
        home_team_layout = QVBoxLayout()
        self.home_team_label = QLabel("Home Team:")
        self.home_team_input = QLineEdit()
        self.home_team_input.setPlaceholderText("Enter Home Team Name")
        home_team_layout.addWidget(self.home_team_label)
        home_team_layout.addWidget(self.home_team_input)

        # Away Team Section
        away_team_layout = QVBoxLayout()
        self.away_team_label = QLabel("Away Team:")
        self.away_team_input = QLineEdit()
        self.away_team_input.setPlaceholderText("Enter Away Team Name")
        away_team_layout.addWidget(self.away_team_label)
        away_team_layout.addWidget(self.away_team_input)

        # Display for scores
        self.score_display = QLabel(f"{self.home_score:02d} : {self.away_score:02d}")
        self.score_display.setStyleSheet("font-size: 24px; font-weight: bold;")

        game_info_layout.addLayout(home_team_layout)
        game_info_layout.addStretch()
        game_info_layout.addWidget(self.score_display)
        game_info_layout.addStretch()
        game_info_layout.addLayout(away_team_layout)

        main_layout.addLayout(game_info_layout)

        timer_layout = QHBoxLayout()

        left_timer_layout = QVBoxLayout()
        self.quarter_label = QLabel("Quarter:")
        self.current_quarter_display = QLabel(self.quarters[self.current_quarter_index])
        self.current_quarter_display.setStyleSheet("font-size: 18px; font-weight: bold;")
        left_timer_layout.addWidget(self.quarter_label, alignment=Qt.AlignmentFlag.AlignLeft)
        left_timer_layout.addWidget(self.current_quarter_display, alignment=Qt.AlignmentFlag.AlignLeft)

        # Center Layout: Timer
        center_timer_layout = QVBoxLayout()
        self.timer_display = QLabel(self.format_time(self.current_time))
        self.timer_display.setStyleSheet("font-size: 24px; font-weight: bold;")
        center_timer_layout.addWidget(QLabel("Time:", alignment=Qt.AlignmentFlag.AlignCenter))
        center_timer_layout.addWidget(self.timer_display, alignment=Qt.AlignmentFlag.AlignCenter)

        # Right Layout: Timer Controls
        right_timer_layout = QVBoxLayout()
        self.start_timer_button = QPushButton("Start Timer")
        self.stop_timer_button = QPushButton("Stop Timer")
        self.reset_timer_button = QPushButton("Reset")
        self.reset_timer_button.clicked.connect(self.reset_game)

        right_timer_layout.addWidget(self.start_timer_button, alignment=Qt.AlignmentFlag.AlignRight)
        right_timer_layout.addWidget(self.stop_timer_button, alignment=Qt.AlignmentFlag.AlignRight)
        right_timer_layout.addWidget(self.reset_timer_button, alignment=Qt.AlignmentFlag.AlignRight)

        # Combine layouts
        timer_layout.addLayout(left_timer_layout)
        timer_layout.addStretch()  # Add space between sections
        timer_layout.addLayout(center_timer_layout)
        timer_layout.addStretch()
        timer_layout.addLayout(right_timer_layout)


        main_layout.addLayout(timer_layout)

        # Connect Timer Buttons
        self.start_timer_button.clicked.connect(self.start_timer)
        self.stop_timer_button.clicked.connect(self.stop_timer)

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        # Player Stats Section
        player_stats_layout = QHBoxLayout()

        # Home Team Player Stats
        home_player_layout = QVBoxLayout()
        home_player_layout.addWidget(QLabel("Home Team Players"))
        self.home_player_table = QTableWidget(12, 5)  # Adjust row count to your needs
        self.home_player_table.setHorizontalHeaderLabels(["No.", "Name", "Points", "Fouls", "Sub"])
        self.home_player_table.setFixedSize(523, 386)
        home_player_layout.addWidget(self.home_player_table)

        # Away Team Player Stats
        away_player_layout = QVBoxLayout()
        away_player_layout.addWidget(QLabel("Away Team Players"))
        self.away_player_table = QTableWidget(12, 5)
        self.away_player_table.setHorizontalHeaderLabels(["No.", "Name", "Points", "Fouls", "Sub"])
        self.away_player_table.setFixedSize(523, 386)
        away_player_layout.addWidget(self.away_player_table)

        player_stats_layout.addLayout(home_player_layout)
        player_stats_layout.addStretch()
        player_stats_layout.addLayout(away_player_layout)

        main_layout.addLayout(player_stats_layout)

        # Scoring Section
        score_section_layout = QHBoxLayout()

        # Home Team Scoring
        home_score_layout = QVBoxLayout()
        home_score_layout.addWidget(QLabel("Home Team Score"))
        self.home_two_points = QPushButton("2 Points")
        self.home_three_points = QPushButton("3 Points")
        self.home_free_throw = QPushButton("Free Throw")

        home_score_layout.addWidget(self.home_two_points)
        home_score_layout.addWidget(self.home_three_points)
        home_score_layout.addWidget(self.home_free_throw)

        # Away Team Scoring
        away_score_layout = QVBoxLayout()
        away_score_layout.addWidget(QLabel("Away Team Score"))
        self.away_two_points = QPushButton("2 Points")
        self.away_three_points = QPushButton("3 Points")
        self.away_free_throw = QPushButton("Free Throw")

        away_score_layout.addWidget(self.away_two_points)
        away_score_layout.addWidget(self.away_three_points)
        away_score_layout.addWidget(self.away_free_throw)

        score_section_layout.addLayout(home_score_layout)
        score_section_layout.addStretch()
        score_section_layout.addLayout(away_score_layout)

        main_layout.addLayout(score_section_layout)

        # Timeout Section
        # Variables for timeout counts
        self.timeout_count_home_12 = 0  # Home team's timeouts for 1st & 2nd quarters
        self.timeout_count_away_12 = 0  # Away team's timeouts for 1st & 2nd quarters
        self.timeout_count_home_34 = 0  # Home team's timeouts for 3rd & 4th quarters
        self.timeout_count_away_34 = 0   # Total timeouts used in 3rd and 4th quarter

        # Timeout Section
        timeout_layout = QVBoxLayout()

        timeout_buttons_layout = QHBoxLayout()
        self.home_timeout_button = QPushButton("Timeout - Home")
        self.home_timeout_button.clicked.connect(self.timeout_home)
        self.away_timeout_button = QPushButton("Timeout - Away")
        self.away_timeout_button.clicked.connect(self.timeout_away)

        timeout_buttons_layout.addWidget(self.home_timeout_button)
        timeout_buttons_layout.addWidget(self.away_timeout_button)

        timeout_labels_layout = QHBoxLayout()
        self.timeout_label_home_12 = QLabel("Home Timeout Count: 0/2 (1st & 2nd Quarter)")
        self.timeout_label_away_12 = QLabel("Away Timeout Count: 0/2 (1st & 2nd Quarter)")
        self.timeout_label_home_34 = QLabel("Home Timeout Count: 0/3 (3rd & 4th Quarter)")
        self.timeout_label_away_34 = QLabel("Away Timeout Count: 0/3 (3rd & 4th Quarter)")

        timeout_labels_layout.addWidget(self.timeout_label_home_12)
        timeout_labels_layout.addWidget(self.timeout_label_home_34)
        timeout_labels_layout.addWidget(self.timeout_label_away_12)
        timeout_labels_layout.addWidget(self.timeout_label_away_34)

        timeout_layout.addLayout(timeout_buttons_layout)
        timeout_layout.addLayout(timeout_labels_layout)

        main_layout.addLayout(timeout_layout)


        # Bottom Section: Quarter Summary
        summary_layout = QHBoxLayout()
        self.quarter_summary = QLabel("Quarter Summary: 1st: 00 - 00 | 2nd: 00 - 00 | 3rd: 00 - 00 | 4th: 00 - 00")
        summary_layout.addWidget(self.quarter_summary)

        main_layout.addLayout(summary_layout)

        # Connect Buttons to update score
        self.home_two_points.clicked.connect(lambda: self.update_score("home", 2))
        self.home_three_points.clicked.connect(lambda: self.update_score("home", 3))
        self.home_free_throw.clicked.connect(lambda: self.update_score("home", 1))
        self.away_two_points.clicked.connect(lambda: self.update_score("away", 2))
        self.away_three_points.clicked.connect(lambda: self.update_score("away", 3))
        self.away_free_throw.clicked.connect(lambda: self.update_score("away", 1))

    def eventFilter(self, obj, event):
        """Event filter to clear focus when clicking outside input fields."""
        if event.type() == QEvent.Type.MouseButtonPress:
            if obj not in [self.home_team_input, self.away_team_input]:
                self.clear_focus_from_inputs()
        return super().eventFilter(obj, event)

    def clear_focus_from_inputs(self):
        """Clear focus from Home and Away Team Input fields."""
        self.home_team_input.clearFocus()
        self.away_team_input.clearFocus()
        self.setFocus(Qt.FocusReason.OtherFocusReason)

    def import_style(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print(f"Error: Cannot find the file '{file_name}'")

    def start_timer(self):
        if not self.timer_running:
            self.timer.start(1000)  # Update every second
            self.timer_running = True

    def stop_timer(self):
        self.timer.stop()
        self.timer_running = False

    def update_timer(self):
        if self.current_time > 0:
            self.current_time -= 1
            self.timer_display.setText(self.format_time(self.current_time))
        else:
            self.timer.stop()
            self.timer_running = False
            self.advance_quarter()

    def timeout_home(self):
        if self.can_take_timeout("home"):
            self.stop_timer()
            self.increment_timeout_count("home")
            QMessageBox.information(self, "Timeout", "Home team has taken a timeout.")
        else:
            QMessageBox.warning(self, "Timeout", "No timeouts remaining for Home team in this quarter set.")

    def timeout_away(self):
        if self.can_take_timeout("away"):
            self.stop_timer()
            self.increment_timeout_count("away")
            QMessageBox.information(self, "Timeout", "Away team has taken a timeout.")
        else:
            QMessageBox.warning(self, "Timeout", "No timeouts remaining for Away team in this quarter set.")


    def can_take_timeout(self, team):
        """Check if timeout is allowed based on the current quarter and team."""
        if self.current_quarter_index < 2:  # 1st & 2nd Quarters
            if team == "home":
                return self.timeout_count_home_12 < 2
            elif team == "away":
                return self.timeout_count_away_12 < 2
        else:  # 3rd & 4th Quarters
            if team == "home":
                return self.timeout_count_home_34 < 3
            elif team == "away":
                return self.timeout_count_away_34 < 3


    def increment_timeout_count(self, team):
        """Increment the timeout count based on the current quarter and team."""
        if self.current_quarter_index < 2:  # 1st & 2nd Quarters
            if team == "home":
                self.timeout_count_home_12 += 1
                self.timeout_label_home_12.setText(f"Home Timeout Count: {self.timeout_count_home_12}/2 (1st & 2nd Quarter)")
            elif team == "away":
                self.timeout_count_away_12 += 1
                self.timeout_label_away_12.setText(f"Away Timeout Count: {self.timeout_count_away_12}/2 (1st & 2nd Quarter)")
        else:  # 3rd & 4th Quarters
            if team == "home":
                self.timeout_count_home_34 += 1
                self.timeout_label_home_34.setText(f"Home Timeout Count: {self.timeout_count_home_34}/3 (3rd & 4th Quarter)")
            elif team == "away":
                self.timeout_count_away_34 += 1
                self.timeout_label_away_34.setText(f"Away Timeout Count: {self.timeout_count_away_34}/3 (3rd & 4th Quarter)")


    def advance_quarter(self):
        if self.current_quarter_index < len(self.quarters) - 1:
            self.current_quarter_index += 1
            self.current_time = 10 * 60  # Reset time for the next quarter
            self.current_quarter_display.setText(self.quarters[self.current_quarter_index])
            self.timer_display.setText(self.format_time(self.current_time))

            # Reset timeout counts for 1st & 2nd to 0 when advancing to 3rd quarter
            if self.current_quarter_index == 2:
                self.timeout_count_home_12 = 0
                self.timeout_count_away_12 = 0
                self.timeout_label_home_12.setText("Home Timeout Count: 0/2 (1st & 2nd Quarter)")
                self.timeout_label_away_12.setText("Away Timeout Count: 0/2 (1st & 2nd Quarter)")

    @staticmethod
    def format_time(seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

    def update_score(self, team, points):
        # Update the main score
        if team == "home":
            self.home_score += points
        elif team == "away":
            self.away_score += points

        # Update the score display
        self.score_display.setText(f"{self.home_score:02d} : {self.away_score:02d}")

        # Update the selected quarter score
        current_quarter = self.quarters[self.current_quarter_index]
        if team == "home":
            self.quarter_scores[current_quarter][0] += points
        elif team == "away":
            self.quarter_scores[current_quarter][1] += points

        # Update the quarter summary
        summary_text = "Quarter Summary: " + " | ".join(
            [f"{q}: {scores[0]:02d} - {scores[1]:02d}" for q, scores in self.quarter_scores.items()]
        )
        self.quarter_summary.setText(summary_text)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        # Clear focus from tables
        self.home_player_table.clearFocus()
        self.away_player_table.clearFocus()

    def reset_game(self):
        # Reset scores
        self.home_score = 0
        self.away_score = 0
        self.score_display.setText(f"{self.home_score:02d} : {self.away_score:02d}")

        # Reset time and quarter
        self.current_time = 10 * 60
        self.current_quarter_index = 0
        self.current_quarter_display.setText(self.quarters[self.current_quarter_index])
        self.timer_display.setText(self.format_time(self.current_time))

        # Reset quarter scores
        self.quarter_scores = {"1st": [0, 0], "2nd": [0, 0], "3rd": [0, 0], "4th": [0, 0]}
        summary_text = "Quarter Summary: " + " | ".join(
            [f"{q}: {scores[0]:02d} - {scores[1]:02d}" for q, scores in self.quarter_scores.items()]
        )
        self.quarter_summary.setText(summary_text)

        # Reset timeout counts
        self.timeout_count_home_12 = 0
        self.timeout_count_away_12 = 0
        self.timeout_count_home_34 = 0
        self.timeout_count_away_34 = 0

        self.timeout_label_home_12.setText("Home Timeout Count: 0/2 (1st & 2nd Quarter)")
        self.timeout_label_away_12.setText("Away Timeout Count: 0/2 (1st & 2nd Quarter)")
        self.timeout_label_home_34.setText("Home Timeout Count: 0/3 (3rd & 4th Quarter)")
        self.timeout_label_away_34.setText("Away Timeout Count: 0/3 (3rd & 4th Quarter)")

        # Stop the timer if running
        self.stop_timer()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScoreSheetApp()
    window.show()
    sys.exit(app.exec())
