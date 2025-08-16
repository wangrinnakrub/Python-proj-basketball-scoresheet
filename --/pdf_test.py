import sqlite3
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def export_match_to_pdf(team1_name, team2_name, output_file='match_summary_full.pdf'):
    conn = sqlite3.connect("C:/Users/ASUS/OneDrive/Desktop/Dabest/basketball_score_sheet.db")
    cursor = conn.cursor()

    cursor.execute("SELECT team_id, tournament_name FROM teams WHERE team_name = ?", (team1_name,))
    t1_data = cursor.fetchone()
    cursor.execute("SELECT team_id FROM teams WHERE team_name = ?", (team2_name,))
    t2_data = cursor.fetchone()

    if not t1_data or not t2_data:
        print("❌ ไม่เจอทีมในฐานข้อมูล")
        return

    team1_id, tournament_name = t1_data
    team2_id = t2_data[0]

    cursor.execute("""
        SELECT match_id, match_date FROM matches
        WHERE (team1_id = ? AND team2_id = ?) OR (team1_id = ? AND team2_id = ?)
    """, (team1_id, team2_id, team2_id, team1_id))
    match = cursor.fetchone()

    if not match:
        print("❌ ไม่เจอแมตช์ระหว่าง 2 ทีมนี้")
        return

    match_id, match_date = match

    c = canvas.Canvas(output_file, pagesize=A4)
    width, height = A4
    y = 800

    def draw_line(text, size=12, offset=20):
        nonlocal y
        if y < 50:  # ถ้าใกล้ขอบล่างแล้ว
            c.showPage()
            y = 800
            c.setFont("Helvetica", size)
        c.setFont("Helvetica", size)
        c.drawString(50, y, text)
        y -= offset

    draw_line("🏀 Tournament Match Summary", 16, 30)
    draw_line(f"Tournament: {tournament_name}")
    draw_line(f"Match ID: {match_id} | Match Date: {match_date}")
    draw_line(f"{team1_name} (ID: {team1_id}) vs {team2_name} (ID: {team2_id})", 14, 25)
    cursor.execute("SELECT winner FROM matches WHERE match_id = ?", (match_id,))
    winner_row = cursor.fetchone()
    if winner_row:
        draw_line(f"🏆 Match Winner: {winner_row[0]}", 13, 25)

    draw_line(f"Players for {team1_name}:", 12, 18)
    cursor.execute("SELECT player_name, player_number FROM players WHERE team_id = ?", (team1_id,))
    for name, number in cursor.fetchall():
        draw_line(f" - #{number} {name}", 10, 14)

    draw_line(f"Players for {team2_name}:", 12, 18)
    cursor.execute("SELECT player_name, player_number FROM players WHERE team_id = ?", (team2_id,))
    for name, number in cursor.fetchall():
        draw_line(f" - #{number} {name}", 10, 14)

    for period in range(1, 5):
        draw_line(f"\nPeriod {period}", 13, 20)

        cursor.execute("""
            SELECT team1_score, team2_score, period_winner FROM scores
            WHERE match_id = ? AND period = ?
        """, (match_id, period))
        result = cursor.fetchone()
        if result:
            t1_score, t2_score, winner = result
            draw_line(f"Score: {team1_name} {t1_score} - {t2_score} {team2_name}", 11)
            draw_line(f"Winner: {winner}", 11)

        # Timeouts (no LIKE)
        draw_line("Timeouts:", 11)
        cursor.execute("""
            SELECT team_id, time FROM timeouts
            WHERE match_id = ? AND period = ? ORDER BY time DESC
        """, (match_id, period))
        for team_id, time in cursor.fetchall():
            draw_line(f" - Team {team_id} @ {time}", 10)

        # Substitutions (no LIKE)
        draw_line("Substitutions:", 11)
        cursor.execute("""
            SELECT team_id, player_out, player_in, time FROM substitutions
            WHERE match_id = ? AND period = ? ORDER BY time DESC
        """, (match_id, period))
        for team_id, player_out, player_in, time in cursor.fetchall():
            draw_line(f" - Team {team_id}: Out {player_out}, In {player_in} @ {time}", 10)

        # Fouls (no LIKE)
        draw_line("Fouls:", 11)
        cursor.execute("""
            SELECT player_id, time FROM fouls
            WHERE match_id = ? AND period = ? ORDER BY time DESC
        """, (match_id, period))
        for player_id, time in cursor.fetchall():
            draw_line(f" - Player {player_id} @ {time}", 10)

    c.save()
    conn.close()
    print(f"✅ สร้าง PDF เรียบร้อย: {output_file}")

export_match_to_pdf("team1", "team2", "C:/report_pdf/team1_vs_team2.pdf")
