import sqlite3

connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
cursor = connection.cursor()

def create_database_2():
    connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
    cursor = connection.cursor()
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS user_account (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NULL CHECK(length(username) BETWEEN 5 AND 30),
            password TEXT NULL CHECK(length(password) BETWEEN 8 AND 20),
            fullname TEXT NULL CHECK(length(fullname) <= 747),
            phone_number TEXT NULL CHECK(length(phone_number) = 10),
            email TEXT NULL UNIQUE CHECK(
                (email LIKE '%@gmail.com' OR
                email LIKE '%@outlook.com' OR
                email LIKE '%@yahoo.com' OR
                email LIKE '%@icloud.com' OR
                email LIKE '%@hotmail.com' OR
                email LIKE '%@kkumail.com')
                AND length(email) BETWEEN 6 AND 30
            )
        );
    '''
    cursor.execute(create_table_query)

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teams (
            username TEXT NOT NULL,
            tournament_name TEXT NOT NULL,
            FOREIGN KEY(username) REFERENCES user_account(username)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teams (
            team_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            team_name TEXT NOT NULL,
            tournament_name TEXT NOT NULL,
            FOREIGN KEY(username) REFERENCES user_account(username)
        )
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                player_id INTEGER PRIMARY KEY AUTOINCREMENT,
                team_id INTEGER NOT NULL,
                player_name TEXT NOT NULL,
                player_image_path TEXT,
                button_id INTEGER NOT NULL,
                button_object_name TEXT NOT NULL,
                player_number TEXT,
                player_height TEXT,
                player_weight TEXT,
                player_birthday TEXT,
                player_status TEXT,
                student_id TEXT,
                thai_id TEXT,
                phone_number TEXT,
                FOREIGN KEY(team_id) REFERENCES teams(team_id)
            )
        ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS layouts (
            layout_id INTEGER PRIMARY KEY AUTOINCREMENT,
            team_id INTEGER NOT NULL,
            layout_name TEXT NOT NULL,
            layout_exists INTEGER NOT NULL CHECK (layout_exists IN (0, 1)),
            FOREIGN KEY(team_id) REFERENCES teams(team_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS spacers (
            spacer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            layout_id INTEGER NOT NULL,
            index_position INTEGER NOT NULL,
            width INTEGER NOT NULL,
            height INTEGER NOT NULL,
            FOREIGN KEY(layout_id) REFERENCES layouts(layout_id)
        )
    ''')
    connection.commit()
    connection.close()
    print("Database created successfully!")

def create_database_for_match_result():
    connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
    cursor = connection.cursor()

    # ตารางการแข่งขัน
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS matches (
        match_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        match_date TEXT NOT NULL,
        team1_id INTEGER NOT NULL,
        team2_id INTEGER NOT NULL,
        winner TEXT
    )""")

    # ตารางผู้เล่น
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS players (
        player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        team_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        number INTEGER NOT NULL,
        is_starter BOOLEAN NOT NULL
    )""")

    # ตารางการเปลี่ยนตัว
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS substitutions (
            sub_id INTEGER PRIMARY KEY AUTOINCREMENT,
            match_id INTEGER NOT NULL,
            team_id INTEGER NOT NULL,
            player_out INTEGER NOT NULL,
            player_in INTEGER NOT NULL,
            time TEXT NOT NULL,
            period INTEGER NOT NULL
        )""")

    # ตารางฟาวล์
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fouls (
        foul_id INTEGER PRIMARY KEY AUTOINCREMENT,
        match_id INTEGER NOT NULL,
        player_id INTEGER NOT NULL,
        time TEXT NOT NULL,
        period INTEGER NOT NULL
    )""")

    # ตารางการขอเวลานอก
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS timeouts (
        timeout_id INTEGER PRIMARY KEY AUTOINCREMENT,
        match_id INTEGER NOT NULL,
        team_id INTEGER NOT NULL,
        time TEXT NOT NULL,
        period INTEGER NOT NULL
    )""")

    # ตารางคะแนนแต่ละ period
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        score_id INTEGER PRIMARY KEY AUTOINCREMENT,
        match_id INTEGER NOT NULL,
        period INTEGER NOT NULL,
        team1_score INTEGER NOT NULL,
        team2_score INTEGER NOT NULL,
        period_winner TEXT NOT NULL
    )""")

    connection.commit()
    connection.close()

def create_database_for_match_result1():
    connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
    cursor = connection.cursor()

    # ตารางการแข่งขัน
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS matches (
        match_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        match_date TEXT NOT NULL,
        team1_id INTEGER NOT NULL,
        team2_id INTEGER NOT NULL,
        winner TEXT
    )""")

    # ตารางผู้เล่น
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS players (
        player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        team_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        number INTEGER NOT NULL,
        is_starter BOOLEAN NOT NULL
    )""")

    # ตารางการเปลี่ยนตัว
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS substitutions (
            sub_id INTEGER PRIMARY KEY AUTOINCREMENT,
            match_id INTEGER NOT NULL,
            team_id INTEGER NOT NULL,
            player_out INTEGER NOT NULL,
            player_in INTEGER NOT NULL,
            time TEXT NOT NULL,
            period INTEGER NOT NULL
        )""")

    # ตารางฟาวล์
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fouls (
        foul_id INTEGER PRIMARY KEY AUTOINCREMENT,
        match_id INTEGER NOT NULL,
        team TEXT NOT NULL,
        player_id INTEGER NOT NULL,
        time TEXT NOT NULL,
        period INTEGER NOT NULL
    )""")

    # ตารางการขอเวลานอก
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS timeouts (
        timeout_id INTEGER PRIMARY KEY AUTOINCREMENT,
        match_id INTEGER NOT NULL,
        team_id INTEGER NOT NULL,
        time TEXT NOT NULL,
        period INTEGER NOT NULL
    )""")

    # ตารางคะแนนแต่ละ period
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        score_id INTEGER PRIMARY KEY AUTOINCREMENT,
        match_id INTEGER NOT NULL,
        period INTEGER NOT NULL,
        team1_score INTEGER NOT NULL,
        team2_score INTEGER NOT NULL,
        period_winner TEXT NOT NULL
    )""")

    connection.commit()
    connection.close()

def del_db_1():
    connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM user_account')
    connection.commit()
    connection.close()
    print("user_account deleted successfully!")

def del_db_2():
    connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM teams')
    cursor.execute('DELETE FROM players')
    connection.commit()
    connection.close()
    print("teams, players, layouts, spacers deleted successfully!")

def del_matches():
    connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM matches')
    cursor.execute('DELETE FROM substitutions')
    cursor.execute('DELETE FROM fouls')
    cursor.execute('DELETE FROM timeouts')
    cursor.execute('DELETE FROM scores')
    connection.commit()
    connection.close()
    print("matches deleted successfully!")

def clear_all_except_user_account():
    connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
    cursor = connection.cursor()
    # ลบข้อมูลในทุกตารางที่ไม่ใช่ user_account
    cursor.execute('DELETE FROM teams')
    cursor.execute('DELETE FROM players')
    cursor.execute('DELETE FROM matches')
    cursor.execute('DELETE FROM substitutions')
    cursor.execute('DELETE FROM fouls')
    cursor.execute('DELETE FROM timeouts')
    cursor.execute('DELETE FROM scores')
    cursor.execute('DELETE FROM tournament')
    connection.commit()
    connection.close()
    print("Cleared all data except user_account.")

clear_all_except_user_account()
