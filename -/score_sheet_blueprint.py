from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys

class ScoreSheetApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basketball Score Sheet")
        self.setGeometry(100, 60, 1000, 700)

        # Variables to store scores
        self.home_score = 0
        self.away_score = 0

        # Main layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Header Section: Game Info
        game_info_layout = QHBoxLayout()

        self.home_team_label = QLabel("Home Team")
        self.away_team_label = QLabel("Away Team")

        # Display for scores, updating this in real-time
        self.score_display = QLabel(f"{self.home_score:02d} : {self.away_score:02d}")
        self.score_display.setStyleSheet("font-size: 24px; font-weight: bold;")

        game_info_layout.addWidget(self.home_team_label)
        game_info_layout.addStretch()
        game_info_layout.addWidget(self.score_display)
        game_info_layout.addStretch()
        game_info_layout.addWidget(self.away_team_label)

        main_layout.addLayout(game_info_layout)

        # Player Stats Section
        player_stats_layout = QHBoxLayout()

        # Home Team Player Stats
        home_player_layout = QVBoxLayout()
        home_player_layout.addWidget(QLabel("Home Team Players"))
        self.home_player_table = QTableWidget(12, 5)  # Adjust row count to your needs
        self.home_player_table.setHorizontalHeaderLabels(["No.", "Name", "Points", "Fouls", "Sub"])
        home_player_layout.addWidget(self.home_player_table)

        # Away Team Player Stats
        away_player_layout = QVBoxLayout()
        away_player_layout.addWidget(QLabel("Away Team Players"))
        self.away_player_table = QTableWidget(12, 5)
        self.away_player_table.setHorizontalHeaderLabels(["No.", "Name", "Points", "Fouls", "Sub"])
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
        timeout_layout = QHBoxLayout()

        self.home_timeout_button = QPushButton("Timeout - Home")
        self.away_timeout_button = QPushButton("Timeout - Away")
        timeout_layout.addWidget(self.home_timeout_button)
        timeout_layout.addWidget(self.away_timeout_button)

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

    def update_score(self, team, points):
        if team == "home":
            self.home_score += points
        elif team == "away":
            self.away_score += points

        # Update the score display
        self.score_display.setText(f"{self.home_score:02d} : {self.away_score:02d}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScoreSheetApp()
    window.show()
    sys.exit(app.exec())
