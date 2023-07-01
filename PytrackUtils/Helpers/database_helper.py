import sqlite3

def cursor_execute(command:str, args: tuple):
    conn = sqlite3.connect("pyTrack.db")
    c = conn.cursor()

    c.execute(command, args,)

    conn.commit()
    conn.close()

def truncate_table(table:str):
    conn = sqlite3.connect("pyTrack.db")
    c = conn.cursor()

    c.execute(f"TRUNCATE TABLE {table}")

    conn.commit()
    conn.close()

def clear_window_history():
    truncate_table("windowTimeEntries")

def clear_window_settings():
    truncate_table("windowTypes")
