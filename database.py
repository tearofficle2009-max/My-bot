import sqlite3

def init_db():
    conn = sqlite3.connect("bot_data.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS group_videos (group_id INTEGER PRIMARY KEY, video_id TEXT)")
    conn.commit()
    conn.close()

def save_video(group_id, video_id):
    conn = sqlite3.connect("bot_data.db")
    cursor = conn.cursor()
    cursor.execute("REPLACE INTO group_videos (group_id, video_id) VALUES (?, ?)", (group_id, video_id))
    conn.commit()
    conn.close()

def get_video(group_id):
    conn = sqlite3.connect("bot_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT video_id FROM group_videos WHERE group_id = ?", (group_id,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None
