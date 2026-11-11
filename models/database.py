import sqlite3

DATABASE = "interview.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def create_tables():

    connection = get_db_connection()

    # ==========================================
    # ADMINS TABLE
    # ==========================================

    connection.execute("""
        CREATE TABLE IF NOT EXISTS admins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # ==========================================
    # USERS TABLE
    # ==========================================

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # ==========================================
    # PROFILES TABLE
    # ==========================================

    connection.execute("""
        CREATE TABLE IF NOT EXISTS profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            education TEXT,
            skills TEXT,
            experience TEXT,
            domain TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # ==========================================
    # RESUMES TABLE
    # ==========================================

    connection.execute("""
        CREATE TABLE IF NOT EXISTS resumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            file_name TEXT NOT NULL,
            file_path TEXT NOT NULL,
            resume_text TEXT,
            skills TEXT,
            uploaded_at TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # ==========================================
    # INTERVIEW SETTINGS TABLE
    # ==========================================

    connection.execute("""
        CREATE TABLE IF NOT EXISTS interview_settings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            question_count INTEGER NOT NULL,
            time_limit INTEGER NOT NULL
        )
    """)

    # ==========================================
    # QUESTIONS TABLE
    # ==========================================

    connection.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain TEXT NOT NULL,
            question TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            expected_answer TEXT
        )
    """)

    # ==========================================
    # QUESTION HISTORY TABLE
    # ==========================================

    connection.execute("""
        CREATE TABLE IF NOT EXISTS question_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            domain TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            question TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # ==========================================
    # INTERVIEW RESULTS TABLE
    # ==========================================

    connection.execute("""
        CREATE TABLE IF NOT EXISTS interview_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            domain TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            total_score REAL NOT NULL,
            total_questions INTEGER NOT NULL,
            feedback TEXT,
            completed_at TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # ==========================================
    # ADD completed_at TO OLD DATABASE
    # ==========================================

    columns = connection.execute("""
        PRAGMA table_info(interview_results)
    """).fetchall()

    column_names = [
        column["name"]
        for column in columns
    ]

    if "completed_at" not in column_names:

        connection.execute("""
            ALTER TABLE interview_results
            ADD COLUMN completed_at TEXT
        """)

    # ==========================================
    # DEFAULT ADMIN
    # ==========================================

    connection.execute("""
        INSERT OR IGNORE INTO admins
        (email, password)
        VALUES (?, ?)
    """, (
        "admin@virtualinterview.com",
        "admin123"
    ))

    connection.commit()

    connection.close()