from importlib import import_module
from flask import Flask, request, jsonify, redirect, render_template
from models.database import create_tables, get_db_connection
import random
import re
import os
from datetime import datetime
from werkzeug.utils import secure_filename
from pypdf import PdfReader
from docx import Document

app = Flask(__name__)

# ==========================================
# RESUME UPLOAD SETTINGS
# ==========================================

UPLOAD_FOLDER = "uploads/resumes"

ALLOWED_RESUME_EXTENSIONS = {
    "pdf",
    "docx"
}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


create_tables()


# ==========================================
# HOME
# ==========================================

@app.route("/")
def home():
    return redirect("/login")


# ==========================================
# LOGIN PAGE
# ==========================================

@app.route("/login")
def login_page():
    return render_template("login.html")

# ==========================================
# CANDIDATE LOGIN
# ==========================================

@app.route("/login", methods=["POST"])
def login_user():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "message": "Invalid login data"
        }), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "message": "Email and password are required."
        }), 400

    connection = get_db_connection()

    user = connection.execute("""
        SELECT *
        FROM users
        WHERE email = ?
        AND password = ?
    """, (email, password)).fetchone()

    connection.close()

    if not user:
        return jsonify({
            "message": "Invalid email or password."
        }), 401

    return jsonify({
        "message": "Login successful.",
        "user_id": user["id"],
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "email": user["email"]
    }), 200


# admin login
@app.route("/admin-login")
def admin_login():
    return render_template("admin_login.html")

    #admin dashboard 
@app.route("/admin-dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")

#admin candidates
@app.route("/admin-candidates")
def admin_candidates():

    connection = get_db_connection()

    candidates = connection.execute("""
        SELECT id, first_name, last_name, email
        FROM users
        ORDER BY id DESC
    """).fetchall()

    connection.close()

    return render_template(
        "admin_candidates.html",
        candidates=candidates
    )
# ==========================================
# DELETE USER INTERVIEW HISTORY
# ==========================================

@app.route("/admin-delete-user-history/<int:user_id>", methods=["POST"])
def admin_delete_user_history(user_id):

    connection = get_db_connection()

    try:
        connection.execute("""
            DELETE FROM interview_results
            WHERE user_id = ?
        """, (user_id,))

        connection.execute("""
            DELETE FROM question_history
            WHERE user_id = ?
        """, (user_id,))

        connection.commit()

    finally:
        connection.close()

    return redirect("/admin-candidates")

# ==========================================
# ADMIN QUESTION MANAGEMENT
# ==========================================

@app.route("/admin-questions")
def admin_questions():

    connection = get_db_connection()

    questions = connection.execute("""
        SELECT
            id,
            domain,
            difficulty,
            question,
            expected_answer
        FROM questions
        ORDER BY id DESC
    """).fetchall()

    connection.close()

    return render_template(
        "admin_questions.html",
        questions=questions
    )


# ==========================================
# ADD QUESTION PAGE
# ==========================================

@app.route("/admin-add-question")
def admin_add_question():

    return render_template(
        "admin_add_question.html"
    )


# ==========================================
# ADD QUESTION
# ==========================================

@app.route("/admin-add-question", methods=["POST"])
def add_admin_question():

    data = request.form

    domain = data.get("domain")
    difficulty = data.get("difficulty")
    question = data.get("question")
    expected_answer = data.get("expected_answer")

    if not domain or not difficulty or not question:
        return "Domain, difficulty and question are required."

    connection = get_db_connection()

    connection.execute("""
        INSERT INTO questions
        (
            domain,
            question,
            difficulty,
            expected_answer
        )
        VALUES (?, ?, ?, ?)
    """, (
        domain,
        question,
        difficulty,
        expected_answer
    ))

    connection.commit()
    connection.close()

    return redirect("/admin-questions")


# ==========================================
# EDIT QUESTION PAGE
# ==========================================

@app.route("/admin-edit-question/<int:question_id>")
def admin_edit_question(question_id):

    connection = get_db_connection()

    question = connection.execute("""
        SELECT
            id,
            domain,
            difficulty,
            question,
            expected_answer
        FROM questions
        WHERE id = ?
    """, (question_id,)).fetchone()

    connection.close()

    if not question:
        return "Question not found."

    return render_template(
        "admin_edit_question.html",
        question=question
    )


# ==========================================
# UPDATE QUESTION
# ==========================================

@app.route("/admin-edit-question/<int:question_id>", methods=["POST"])
def update_admin_question(question_id):

    data = request.form

    domain = data.get("domain")
    difficulty = data.get("difficulty")
    question = data.get("question")
    expected_answer = data.get("expected_answer")

    if not domain or not difficulty or not question:
        return "Domain, difficulty and question are required."

    connection = get_db_connection()

    connection.execute("""
        UPDATE questions
        SET
            domain = ?,
            difficulty = ?,
            question = ?,
            expected_answer = ?
        WHERE id = ?
    """, (
        domain,
        difficulty,
        question,
        expected_answer,
        question_id
    ))

    connection.commit()
    connection.close()

    return redirect("/admin-questions")


# ==========================================
# DELETE QUESTION
# ==========================================

@app.route("/admin-delete-question/<int:question_id>", methods=["POST"])
def delete_admin_question(question_id):

    connection = get_db_connection()

    connection.execute("""
        DELETE FROM questions
        WHERE id = ?
    """, (question_id,))

    connection.commit()
    connection.close()

    return redirect("/admin-questions")
    


# ==========================================
# ADMIN RESULTS
# ==========================================

@app.route("/admin-results")
def admin_results():

    connection = get_db_connection()

    results = connection.execute("""
        SELECT
            interview_results.id,
            users.first_name,
            users.last_name,
            users.email,
            interview_results.domain,
            interview_results.difficulty,
            interview_results.total_score,
            interview_results.total_questions,
            interview_results.feedback,
            interview_results.completed_at
        FROM interview_results
        JOIN users
        ON interview_results.user_id = users.id
        ORDER BY interview_results.id DESC
    """).fetchall()

    connection.close()

    return render_template(
        "admin_results.html",
        results=results
    )

# ==========================================
# REGISTER
# ==========================================
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "GET":
        return render_template("register.html")

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "message": "Invalid registration data"
        }), 400

    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")
    password = data.get("password")

    if not first_name or not last_name or not email or not password:
        return jsonify({
            "message": "All fields are required."
        }), 400

    connection = get_db_connection()

    try:

        existing_user = connection.execute("""
            SELECT id
            FROM users
            WHERE email = ?
        """, (email,)).fetchone()

        if existing_user:
            return jsonify({
                "message": "An account with this email already exists."
            }), 400

        connection.execute("""
            INSERT INTO users
            (
                first_name,
                last_name,
                email,
                password
            )
            VALUES (?, ?, ?, ?)
        """, (
            first_name,
            last_name,
            email,
            password
        ))

        connection.commit()

        return jsonify({
            "message": "Registration successful"
        }), 201

    except Exception as error:

        connection.rollback()

        print("Registration error:", error)

        return jsonify({
            "message": "Registration failed."
        }), 500

    finally:

        connection.close()


# ==========================================
# ADMIN LOGIN
# ==========================================

@app.route("/admin-login", methods=["POST"])
def admin_login_user():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "message": "Email and password are required."
        }), 400

    connection = get_db_connection()

    admin = connection.execute("""
        SELECT *
        FROM admins
        WHERE email = ?
        AND password = ?
    """, (email, password)).fetchone()

    connection.close()

    if not admin:
        return jsonify({
            "message": "Invalid admin email or password."
        }), 401

    return jsonify({
        "message": "Admin login successful.",
        "admin_id": admin["id"]
    })
# ==========================================
# ADMIN INTERVIEW SETTINGS
# ==========================================

@app.route("/admin-settings", methods=["POST"])
def admin_settings():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "message": "Invalid settings data"
        }), 400

    domain = data.get("domain")
    difficulty = data.get("difficulty")
    question_count = data.get("question_count")
    time_limit = data.get("time_limit")

    if not domain or not difficulty:
        return jsonify({
            "message": "Domain and difficulty are required."
        }), 400

    try:
        question_count = int(question_count)
        time_limit = int(time_limit)
    except (TypeError, ValueError):

        return jsonify({
            "message": "Question count and time limit must be numbers."
        }), 400

    if question_count <= 0:
        return jsonify({
            "message": "Question count must be greater than 0."
        }), 400

    if time_limit <= 0:
        return jsonify({
            "message": "Time limit must be greater than 0."
        }), 400

    connection = get_db_connection()

    try:

        connection.execute(
            """
            INSERT INTO interview_settings
            (
                domain,
                difficulty,
                question_count,
                time_limit
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                domain,
                difficulty,
                question_count,
                time_limit
            )
        )

        connection.commit()

    finally:

        connection.close()

    return jsonify({
        "message": "Interview settings saved successfully."
    }), 201

#admin interview seting

@app.route("/interview-settings", methods=["GET"])
def get_interview_settings():

    connection = get_db_connection()

    settings = connection.execute("""
        SELECT
            domain,
            difficulty,
            question_count,
            time_limit
        FROM interview_settings
        ORDER BY id DESC
        LIMIT 1
    """).fetchone()

    connection.close()

    if not settings:
        return jsonify({
            "message": "Interview settings not found."
        }), 404

    return jsonify({
        "domain": settings["domain"],
        "difficulty": settings["difficulty"],
        "question_count": settings["question_count"],
        "time_limit": settings["time_limit"]
    })
# ==========================================
# PROFILE
# ==========================================

@app.route("/profile", methods=["GET", "POST"])
def profile():

    # When browser opens /profile
    if request.method == "GET":
        return render_template("profile.html")

    # When profile.html saves the profile
    if request.method == "POST":

        data = request.get_json(silent=True)

        if not data:
            return jsonify({
                "message": "Invalid profile data"
            }), 400

        user_id = data.get("user_id")
        education = data.get("education")
        skills = data.get("skills")
        experience = data.get("experience")
        domain = data.get("domain")

        if not user_id:
            return jsonify({
                "message": "User ID is required"
            }), 400

        if not education or not skills or not experience or not domain:
            return jsonify({
                "message": "All profile fields are required"
            }), 400

        connection = get_db_connection()

        connection.execute(
            """
            INSERT INTO profiles
            (user_id, education, skills, experience, domain)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                user_id,
                education,
                skills,
                experience,
                domain
            )
        )

        connection.commit()
        connection.close()

        return jsonify({
            "message": "Profile saved successfully"
        }), 201


# ==========================================
# CANDIDATE DASHBOARD
# ==========================================

@app.route("/candidate-dashboard")
def candidate_dashboard():

    return render_template(
        "candidate_dashboard.html"
    )

# ==========================================
# RESUME PAGE
# ==========================================

@app.route("/resume")
def resume():
    return render_template("resume.html")

# ==========================================
# RESUME ANALYSIS PAGE
# ==========================================

@app.route("/resume-analysis")
def resume_analysis():

    user_id = request.args.get("user_id")

    if not user_id:
        return redirect("/login")

    connection = get_db_connection()

    resume = connection.execute("""
        SELECT
    id,
    user_id,
    file_name,
    resume_text,
    skills,
    uploaded_at
FROM resumes
        WHERE user_id = ?
        ORDER BY id DESC
        LIMIT 1
    """, (user_id,)).fetchone()

    connection.close()

    if not resume:
        return redirect("/resume")

    return render_template(
        "resume_analysis.html",
        resume=resume
    )

# ==========================================
# RESUME INTERVIEW SETTINGS
# ==========================================

@app.route("/resume-interview-settings")
def resume_interview_settings():

    user_id = request.args.get("user_id")

    if not user_id:
        return redirect("/login")

    connection = get_db_connection()

    resume = connection.execute("""
        SELECT
            id,
            file_name,
            resume_text,
            skills,
            uploaded_at
        FROM resumes
        WHERE user_id = ?
        ORDER BY id DESC
        LIMIT 1
    """, (user_id,)).fetchone()

    connection.close()

    if not resume:
        return redirect("/resume")

    return render_template(
        "resume_interview_settings.html",
        resume=resume
    )



# ==========================================
# RESUME TEXT EXTRACTION
# ==========================================

def extract_resume_text(file_path, extension):

    try:

        # PDF
        if extension == "pdf":

            reader = PdfReader(file_path)

            text = ""

            for page in reader.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

            return text.strip()

        # DOCX
        elif extension == "docx":

            document = Document(file_path)

            text = ""

            for paragraph in document.paragraphs:

                if paragraph.text.strip():
                    text += paragraph.text + "\n"

            return text.strip()

        return ""

    except Exception as error:

        print("Resume text extraction error:", error)

        return ""

    # ==========================================
# RESUME SKILL DETECTION
# ==========================================

def detect_resume_skills(resume_text):

    skill_keywords = [
        "Python",
        "Java",
        "C",
        "C++",
        "C#",
        "JavaScript",
        "HTML",
        "CSS",
        "React",
        "Node.js",
        "Flask",
        "Django",
        "SQL",
        "MySQL",
        "SQLite",
        "MongoDB",
        "Machine Learning",
        "Deep Learning",
        "Artificial Intelligence",
        "Data Science",
        "Data Analysis",
        "Pandas",
        "NumPy",
        "TensorFlow",
        "PyTorch",
        "Git",
        "GitHub",
        "REST API",
        "Bootstrap"
    ]

    detected_skills = []

    text = resume_text.lower()

    for skill in skill_keywords:

        if skill.lower() in text:

            detected_skills.append(skill)

    return detected_skills
# ==========================================
# RESUME UPLOAD
# ==========================================

@app.route("/upload-resume", methods=["POST"])
def upload_resume():

    if "resume" not in request.files:
        return jsonify({
            "message": "Please select a resume."
        }), 400

    file = request.files["resume"]

    if file.filename == "":
        return jsonify({
            "message": "Please select a resume."
        }), 400

    original_filename = secure_filename(file.filename)

    extension = original_filename.rsplit(".", 1)[-1].lower()

    if extension not in ALLOWED_RESUME_EXTENSIONS:
        return jsonify({
            "message": "Only PDF and DOCX files are allowed."
        }), 400

    user_id = request.form.get("user_id")

    if not user_id:
        return jsonify({
            "message": "User ID is required."
        }), 400

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    saved_filename = (
        f"{user_id}_{timestamp}_{original_filename}"
    )

    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        saved_filename
    )

    file.save(file_path)

    # ==========================================
    # EXTRACT RESUME TEXT
    # ==========================================

    resume_text = extract_resume_text(
        file_path,
        extension
    )
    skills = detect_resume_skills(resume_text)

    if not resume_text:

        return jsonify({
            "message": "Could not extract text from the resume."
        }), 400

    connection = get_db_connection()

    try:

        connection.execute("""
            INSERT INTO resumes
            (
                user_id,
                file_name,
                file_path,
                resume_text,
                skills,
                uploaded_at
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            user_id,
            original_filename,
            file_path,
            resume_text,
            ", ".join(skills),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

        connection.commit()

    except Exception as error:

        connection.rollback()

        print("Resume upload error:", error)

        return jsonify({
            "message": "Resume upload failed."
        }), 500

    finally:

        connection.close()

    return jsonify({
        "message": "Resume uploaded successfully.",
        "file_name": original_filename
    }), 200
# ==========================================
# CANDIDATE DASHBOARD DATA
# ==========================================

@app.route("/candidate-dashboard-data")
def candidate_dashboard_data():

    user_id = request.args.get("user_id")

    if not user_id:
        return jsonify({
            "message": "User ID is required"
        }), 400

    connection = get_db_connection()

    try:

        results = connection.execute("""
            SELECT
                domain,
                difficulty,
                total_score,
                total_questions,
                completed_at
            FROM interview_results
            WHERE user_id = ?
            ORDER BY id DESC
        """, (user_id,)).fetchall()


        interview_count = len(results)


        if interview_count > 0:

            scores = [
                float(row["total_score"])
                for row in results
            ]

            average_score = round(
                sum(scores) / len(scores),
                2
            )

            best_score = round(
                max(scores),
                2
            )

        else:

            average_score = 0
            best_score = 0


        # ==========================================
        # DOMAIN PERFORMANCE
        # ==========================================

        domain_scores = {}

        for row in results:

            domain = row["domain"]
            score = float(row["total_score"])

            if domain not in domain_scores:

                domain_scores[domain] = []

            domain_scores[domain].append(score)


        domain_averages = {}

        for domain, scores in domain_scores.items():

            domain_averages[domain] = round(
                sum(scores) / len(scores),
                2
            )


        strongest_domain = "Not available"
        improvement_domain = "Not available"


        if domain_averages:

            strongest_domain = max(
                domain_averages,
                key=domain_averages.get
            )

            improvement_domain = min(
                domain_averages,
                key=domain_averages.get
            )


        # ==========================================
        # PERFORMANCE MESSAGE
        # ==========================================

        if average_score >= 80:

            performance_message = (
                "Excellent performance! "
                "Keep practicing to maintain your skills."
            )

        elif average_score >= 60:

            performance_message = (
                "Good performance! "
                "Practice more to improve your score."
            )

        elif average_score > 0:

            performance_message = (
                "You need more practice. "
                "Focus on your weaker areas."
            )

        else:

            performance_message = (
                "Complete an interview to see "
                "your performance analysis."
            )


        # ==========================================
        # RECENT INTERVIEWS
        # ==========================================

        recent_interviews = []


        for row in results[:5]:

            recent_interviews.append({

                "domain":
                    row["domain"],

                "difficulty":
                    row["difficulty"],

                "total_score":
                    row["total_score"],

                "total_questions":
                    row["total_questions"],

                "completed_at":
                    row["completed_at"]

            })


        return jsonify({

            "interview_count":
                interview_count,

            "average_score":
                average_score,

            "best_score":
                best_score,

            "strongest_domain":
                strongest_domain,

            "improvement_domain":
                improvement_domain,

            "performance_message":
                performance_message,

            "recent_interviews":
                recent_interviews

        }), 200


    finally:

        connection.close()



    
# INTERVIEW PAGE
# ==========================================

@app.route("/interview")
def interview():

    return render_template(
        "interview.html"
    )


# ==========================================
# INTERVIEW SESSION PAGE
# ==========================================

@app.route("/interview-session")
def interview_session():

    return render_template(
        "interview_session.html"
    )


# ==========================================
# RESULT PAGE
# ==========================================

@app.route("/result")
def result():

    return render_template(
        "result.html"
    )
# ==========================================
# QUESTION FILES
# ==========================================

QUESTION_FILES = {

    "Python": "data.python",
    "Java": "data.java",
    "JavaScript": "data.javascript",
    "C": "data.c",
    "C++": "data.cpp",
    "HTML": "data.html",
    "CSS": "data.css",
    "SQL": "data.sql",
    "DBMS": "data.dbms",
    "Data Structures": "data.data_structures",
    "Data Science": "data.data_science",
    "Data Analytics": "data.data_analytics",
    "Machine Learning": "data.machine_learning",
    "Computer Networks": "data.computer_networks",
    "Operating System": "data.operating_system",
    "Cybersecurity": "data.cybersecurity",
    "Cloud Computing": "data.cloud_computing",
    "HR": "data.hr",
    "Behavioral": "data.behavioral",
    "Communication": "data.communication",
    "Algorithms": "data.algorithms",
    "Artificial Intelligence": "data.artificial_intelligence",
    "React": "data.react",
    "Node.js": "data.nodejs"
}


# Get questions

@app.route("/questions", methods=["POST"])
def get_questions():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "message": "Invalid request data"
        }), 400

    user_id = data.get("user_id")
    domain = data.get("domain")
    difficulty = data.get("difficulty")
    count = data.get("count", 10)

    try:
        count = int(count)
    except (TypeError, ValueError):
        count = 10

    if count <= 0:
        count = 10

    if not user_id:
        return jsonify({
            "message": "User ID is required"
        }), 400

    if not domain:
        return jsonify({
            "message": "Domain is required"
        }), 400

    if not difficulty:
        return jsonify({
            "message": "Difficulty is required"
        }), 400

    module_name = QUESTION_FILES.get(domain)

    if not module_name:
        return jsonify({
            "message": "Invalid domain: " + str(domain)
        }), 400

    try:

        question_module = import_module(module_name)

    except Exception as error:

        print("Question bank loading error:", error)

        return jsonify({
            "message": "Could not load question bank",
            "error": str(error)
        }), 500

    question_bank = getattr(
        question_module,
        "questions",
        {}
    )

    difficulty_questions = question_bank.get(
        difficulty,
        []
    )

    # ------------------------------------------
    # GET ADMIN-ADDED QUESTIONS FROM DATABASE
    # ------------------------------------------

    connection = get_db_connection()

    try:

        admin_questions = connection.execute(
            """
            SELECT question
            FROM questions
            WHERE domain = ?
            AND difficulty = ?
            """,
            (
                domain,
                difficulty
            )
        ).fetchall()

        admin_question_list = [
            {
                "question": row["question"]
            }
            for row in admin_questions
        ]

        # ------------------------------------------
        # COMBINE BUILT-IN + ADMIN QUESTIONS
        # ------------------------------------------

        all_questions = (
            list(difficulty_questions)
            + admin_question_list
        )

        if not all_questions:

            return jsonify({
                "message":
                    "No questions found for "
                    + domain
                    + " - "
                    + difficulty
            }), 404

        # ------------------------------------------
        # QUESTION HISTORY
        # ------------------------------------------

        history = connection.execute(
            """
            SELECT question
            FROM question_history
            WHERE user_id = ?
            AND domain = ?
            AND difficulty = ?
            """,
            (
                user_id,
                domain,
                difficulty
            )
        ).fetchall()

        previous_questions = {
            row["question"]
            for row in history
        }

        unseen_questions = [
            item
            for item in all_questions
            if item.get("question", "")
            not in previous_questions
        ]

        # ------------------------------------------
        # RESET HISTORY IF ALL QUESTIONS USED
        # ------------------------------------------

        if not unseen_questions:

            connection.execute(
                """
                DELETE FROM question_history
                WHERE user_id = ?
                AND domain = ?
                AND difficulty = ?
                """,
                (
                    user_id,
                    domain,
                    difficulty
                )
            )

            connection.commit()

            unseen_questions = list(
                all_questions
            )

        # ------------------------------------------
        # SELECT QUESTIONS
        # ------------------------------------------

        selected_questions = random.sample(
            unseen_questions,
            min(
                count,
                len(unseen_questions)
            )
        )

        # ------------------------------------------
        # SAVE QUESTION HISTORY
        # ------------------------------------------

        for item in selected_questions:

            connection.execute(
                """
                INSERT INTO question_history
                (
                    user_id,
                    domain,
                    difficulty,
                    question
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    user_id,
                    domain,
                    difficulty,
                    item.get("question", "")
                )
            )

        connection.commit()

    finally:

        connection.close()

    questions = [
        item.get("question", "")
        for item in selected_questions
    ]

    return jsonify({
        "questions": questions
    }), 200

# ==========================================
# RESUME-BASED QUESTION SELECTION
# ==========================================

@app.route("/resume-questions", methods=["POST"])
def resume_questions():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "message": "Invalid request data"
        }), 400

    user_id = data.get("user_id")
    difficulty = data.get("difficulty")
    count = data.get("count", 10)

    if not user_id:
        return jsonify({
            "message": "User ID is required"
        }), 400

    if not difficulty:
        return jsonify({
            "message": "Difficulty is required"
        }), 400

    try:
        count = int(count)
    except (TypeError, ValueError):
        count = 10

    if count < 5:
        count = 5

    if count > 30:
        count = 30

    connection = get_db_connection()

    try:

        # ------------------------------------------
        # GET LATEST RESUME
        # ------------------------------------------

        resume = connection.execute("""
            SELECT skills
            FROM resumes
            WHERE user_id = ?
            ORDER BY id DESC
            LIMIT 1
        """, (user_id,)).fetchone()

        if not resume:

            return jsonify({
                "message": "No resume found."
            }), 404

        skills_text = resume["skills"] or ""

        skills = [
            skill.strip()
            for skill in skills_text.split(",")
            if skill.strip()
        ]

        if not skills:

            return jsonify({
                "message":
                    "No skills were detected in your resume."
            }), 400

        # ------------------------------------------
        # LOAD QUESTIONS FROM MATCHING SKILLS
        # ------------------------------------------

        all_questions = []

        matched_skills = []

        for skill in skills:

            module_name = QUESTION_FILES.get(skill)

            if not module_name:
                continue

            try:

                question_module = import_module(
                    module_name
                )

                question_bank = getattr(
                    question_module,
                    "questions",
                    {}
                )

                skill_questions = question_bank.get(
                    difficulty,
                    []
                )

                for item in skill_questions:

                    question = item.get(
                        "question",
                        ""
                    )

                    if question:

                        all_questions.append({
                            "question": question,
                            "domain": skill
                        })

                matched_skills.append(skill)

            except Exception as error:

                print(
                    "Resume question bank error:",
                    skill,
                    error
                )

        # ------------------------------------------
        # ADMIN QUESTIONS
        # ------------------------------------------

        if matched_skills:

            placeholders = ",".join(
                ["?"] * len(matched_skills)
            )

            admin_questions = connection.execute(
                f"""
                SELECT domain, question
                FROM questions
                WHERE domain IN ({placeholders})
                AND difficulty = ?
                """,
                tuple(matched_skills) + (difficulty,)
            ).fetchall()

            for row in admin_questions:

                all_questions.append({
                    "question": row["question"],
                    "domain": row["domain"]
                })

        # ------------------------------------------
        # REMOVE DUPLICATES
        # ------------------------------------------

        unique_questions = {}

        for item in all_questions:

            question_text = item["question"]

            unique_questions[
                question_text
            ] = item

        all_questions = list(
            unique_questions.values()
        )

        if not all_questions:

            return jsonify({
                "message":
                    "No matching questions found "
                    "for your resume skills."
            }), 404

        # ------------------------------------------
        # GET PREVIOUS QUESTIONS
        # ------------------------------------------

        history = connection.execute("""
            SELECT question
            FROM question_history
            WHERE user_id = ?
        """, (user_id,)).fetchall()

        previous_questions = {
            row["question"]
            for row in history
        }

        # ------------------------------------------
        # REMOVE PREVIOUSLY ASKED QUESTIONS
        # ------------------------------------------

        unseen_questions = [
            item
            for item in all_questions
            if item["question"]
            not in previous_questions
        ]

        # ------------------------------------------
        # IF NOT ENOUGH NEW QUESTIONS,
        # ALLOW PREVIOUS QUESTIONS
        # ------------------------------------------

        if len(unseen_questions) >= count:

            selected_questions = random.sample(
                unseen_questions,
                count
            )

        else:

            selected_questions = list(
                unseen_questions
            )

            remaining_needed = (
                count - len(selected_questions)
            )

            previous_pool = [
                item
                for item in all_questions
                if item["question"]
                in previous_questions
            ]

            if previous_pool:

                selected_questions.extend(
                    random.sample(
                        previous_pool,
                        min(
                            remaining_needed,
                            len(previous_pool)
                        )
                    )
                )

        # ------------------------------------------
        # SAVE QUESTION HISTORY
        # ------------------------------------------

        for item in selected_questions:

            connection.execute("""
                INSERT INTO question_history
                (
                    user_id,
                    domain,
                    difficulty,
                    question
                )
                VALUES (?, ?, ?, ?)
            """, (
                user_id,
                item["domain"],
                difficulty,
                item["question"]
            ))

        connection.commit()

        # ------------------------------------------
        # RESPONSE
        # ------------------------------------------

        return jsonify({
            "questions": [
                item["question"]
                for item in selected_questions
            ],
            "skills": matched_skills,
            "difficulty": difficulty
        }), 200

    except Exception as error:

        connection.rollback()

        print(
            "Resume question selection error:",
            error
        )

        return jsonify({
            "message":
                "Could not generate resume questions."
        }), 500

    finally:

        connection.close()

# ==========================================
# RESUME INTERVIEW PAGE
# ==========================================

@app.route("/resume-interview")
def resume_interview():

    user_id = request.args.get("user_id")
    difficulty = request.args.get("difficulty")
    question_count = request.args.get("question_count")

    if not user_id:
        return redirect("/login")

    if not difficulty:
        return redirect("/resume-interview-settings?user_id=" + str(user_id))

    if not question_count:
        question_count = 10

    return render_template(
        "resume_interview.html"
    )
# ==========================================
# RESUME RESULT PAGE
# ==========================================

@app.route("/resume-result")
def resume_result():

    user_id = request.args.get("user_id")

    if not user_id:
        return redirect("/login")

    connection = get_db_connection()

    result = connection.execute("""
        SELECT
            id,
            user_id,
            domain,
            difficulty,
            total_score,
            total_questions,
            feedback,
            completed_at
        FROM interview_results
        WHERE user_id = ?
        AND domain = 'Resume-Based'
        ORDER BY id DESC
        LIMIT 1
    """, (user_id,)).fetchone()

    connection.close()

    if not result:
        return redirect("/resume")

    return render_template(
        "resume_result.html",
        result=result
    )

# ====================================
# TEXT CLEANING
# ==========================================

def clean_text(text):

    if not text:
        return set()

    text = text.lower()

    words = re.findall(
        r"[a-zA-Z0-9+#.]+",
        text
    )

    stop_words = {
        "the",
        "is",
        "a",
        "an",
        "and",
        "or",
        "to",
        "of",
        "in",
        "on",
        "for",
        "with",
        "are",
        "was",
        "were",
        "be",
        "been",
        "this",
        "that",
        "it",
        "as",
        "by",
        "from",
        "can",
        "used",
        "use",
        "has",
        "have",
        "which",
        "what",
        "how",
        "why",
        "where",
        "when"
    }

    words = [
        word
        for word in words
        if word not in stop_words
        and len(word) > 2
    ]

    return set(words)


# ==========================================
# EVALUATE ONE ANSWER
# ==========================================

def evaluate_answer(student_answer, expected_answer):

    if not student_answer or not expected_answer:
        return 0

    student_words = clean_text(student_answer)
    expected_words = clean_text(expected_answer)

    if not expected_words:
        return 0

    matched_words = student_words.intersection(
        expected_words
    )

    score = (
        len(matched_words)
        / len(expected_words)
    ) * 100

    score = min(
        round(score),
        100
    )

    return score


# ==========================================
# FEEDBACK
# ==========================================

def get_feedback(score):

    if score >= 80:
        return (
            "Excellent answer. "
            "You covered most important concepts."
        )

    if score >= 60:
        return (
            "Good answer. "
            "Try to include a few more important concepts."
        )

    if score >= 40:
        return (
            "Average answer. "
            "Your answer needs more relevant details."
        )

    if score > 0:
        return (
            "Weak answer. "
            "Try to explain the main concepts more clearly."
        )

    return (
        "No answer was provided. "
        "Try to answer the question."
    )


# ==========================================
# EVALUATE COMPLETE INTERVIEW
# ==========================================

@app.route("/evaluate", methods=["POST"])
def evaluate_interview():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "message": "Invalid interview data"
        }), 400

    user_id = data.get("user_id")
    domain = data.get("domain")
    difficulty = data.get("difficulty")
    questions = data.get("questions", [])
    answers = data.get("answers", [])

    if not user_id:
        return jsonify({
            "message": "User ID is required"
        }), 400

    if not domain:
        return jsonify({
            "message": "Domain is required"
        }), 400

    if not difficulty:
        return jsonify({
            "message": "Difficulty is required"
        }), 400

    if not questions:
        return jsonify({
            "message": "No questions found"
        }), 400

    module_name = QUESTION_FILES.get(domain)

    if not module_name:
        return jsonify({
            "message": "Invalid domain"
        }), 400

    try:

        question_module = import_module(module_name)

    except Exception as error:

        print("Question module error:", error)

        return jsonify({
            "message": "Unable to load question bank"
        }), 500

    question_bank = getattr(
        question_module,
        "questions",
        {}
    )

    difficulty_questions = question_bank.get(
        difficulty,
        []
    )

    # ==========================================
    # BUILT-IN EXPECTED ANSWERS
    # ==========================================

    expected_answers = {}

    for item in difficulty_questions:

        question_text = item.get(
            "question",
            ""
        )

        expected_answer = item.get(
            "expected_answer",
            ""
        )

        expected_answers[
            question_text
        ] = expected_answer

    # ==========================================
    # ADMIN-ADDED EXPECTED ANSWERS
    # ==========================================

    connection = get_db_connection()

    try:

        admin_questions = connection.execute(
            """
            SELECT
                question,
                expected_answer
            FROM questions
            WHERE domain = ?
            AND difficulty = ?
            """,
            (
                domain,
                difficulty
            )
        ).fetchall()

        for row in admin_questions:

            expected_answers[
                row["question"]
            ] = row["expected_answer"]

        # ==========================================
        # EVALUATE EVERY QUESTION
        # ==========================================

        results = []
        total_score = 0

        for index, question in enumerate(questions):

            if index < len(answers):

                answer = answers[index] or ""

            else:

                answer = ""

            expected_answer = expected_answers.get(
                question,
                ""
            )

            score = evaluate_answer(
                answer,
                expected_answer
            )

            feedback = get_feedback(score)

            total_score += score

            results.append({

                "question":
                    question,

                "answer":
                    (
                        answer
                        if answer
                        else "No answer provided"
                    ),

                "expected_answer":
                    expected_answer,

                "score":
                    score,

                "feedback":
                    feedback

            })

        # ==========================================
        # CALCULATE SCORE
        # ==========================================

        question_count = len(questions)

        if question_count > 0:

            total_percentage = round(
                total_score / question_count,
                2
            )

        else:

            total_percentage = 0

        # ==========================================
        # OVERALL FEEDBACK
        # ==========================================

        if total_percentage >= 80:

            overall_feedback = (
                "Excellent performance! "
                "Your answers show strong understanding."
            )

        elif total_percentage >= 60:

            overall_feedback = (
                "Good performance. "
                "You understand the main concepts, "
                "but there is room for improvement."
            )

        elif total_percentage >= 40:

            overall_feedback = (
                "Average performance. "
                "Try to improve your understanding "
                "and explanation of concepts."
            )

        else:

            overall_feedback = (
                "Needs improvement. "
                "Review the important concepts "
                "and practice more interview questions."
            )

        # ==========================================
        # COMPLETION DATE AND TIME
        # ==========================================

        from datetime import datetime

        completed_at = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # ==========================================
        # SAVE RESULT
        # ==========================================

        connection.execute(
            """
            INSERT INTO interview_results
            (
                user_id,
                domain,
                difficulty,
                total_score,
                total_questions,
                feedback,
                completed_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user_id,
                domain,
                difficulty,
                total_percentage,
                question_count,
                overall_feedback,
                completed_at
            )
        )

        connection.commit()

    finally:

        connection.close()

    # ==========================================
    # RETURN RESULT
    # ==========================================

    return jsonify({

        "message":
            "Interview evaluated successfully",

        "score":
            total_percentage,

        "total_questions":
            question_count,

        "feedback":
            overall_feedback,

        "completed_at":
            completed_at,

        "results":
            results

    }), 200

# ==========================================
# RESUME INTERVIEW EVALUATION
# ==========================================

@app.route("/resume-evaluate", methods=["POST"])
def resume_evaluate():

    from datetime import datetime

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "message": "Invalid evaluation data."
        }), 400

    user_id = data.get("user_id")
    difficulty = data.get("difficulty", "Medium")
    questions = data.get("questions", [])
    answers = data.get("answers", [])

    if not user_id:
        return jsonify({
            "message": "User ID is required."
        }), 400

    if not questions:
        return jsonify({
            "message": "No questions found."
        }), 400

    connection = get_db_connection()

    try:

        # ------------------------------------------
        # GET EXPECTED ANSWERS
        # ------------------------------------------

        expected_answers = {}

        # Built-in question banks
        for domain, module_name in QUESTION_FILES.items():

            try:

                question_module = import_module(
                    module_name
                )

                question_bank = getattr(
                    question_module,
                    "questions",
                    {}
                )

                difficulty_questions = question_bank.get(
                    difficulty,
                    []
                )

                for item in difficulty_questions:

                    question_text = item.get(
                        "question",
                        ""
                    )

                    expected_answers[
                        question_text
                    ] = item.get(
                        "expected_answer",
                        ""
                    )

            except Exception as error:

                print(
                    "Resume evaluation question error:",
                    error
                )

        # ------------------------------------------
        # ADMIN QUESTIONS
        # ------------------------------------------

        admin_questions = connection.execute("""
            SELECT
                question,
                expected_answer
            FROM questions
            WHERE difficulty = ?
        """, (difficulty,)).fetchall()

        for row in admin_questions:

            expected_answers[
                row["question"]
            ] = row["expected_answer"] or ""

        # ------------------------------------------
        # EVALUATE QUESTIONS
        # ------------------------------------------

        results = []
        total_score = 0

        for index, question in enumerate(questions):

            if index < len(answers):

                answer = answers[index] or ""

            else:

                answer = ""

            expected_answer = expected_answers.get(
                question,
                ""
            )

            score = evaluate_answer(
                answer,
                expected_answer
            )

            feedback = get_feedback(score)

            total_score += score

            results.append({

                "question":
                    question,

                "answer":
                    (
                        answer
                        if answer
                        else "No answer provided"
                    ),

                "expected_answer":
                    expected_answer,

                "score":
                    score,

                "feedback":
                    feedback

            })

        # ------------------------------------------
        # FINAL SCORE
        # ------------------------------------------

        question_count = len(questions)

        if question_count > 0:

            final_score = round(
                total_score / question_count,
                2
            )

        else:

            final_score = 0

        # ------------------------------------------
        # OVERALL FEEDBACK
        # ------------------------------------------

        if final_score >= 80:

            overall_feedback = (
                "Excellent performance! "
                "Your answers show strong understanding."
            )

        elif final_score >= 60:

            overall_feedback = (
                "Good performance. "
                "You understand the main concepts, "
                "but there is room for improvement."
            )

        elif final_score >= 40:

            overall_feedback = (
                "Average performance. "
                "Try to improve your understanding "
                "and explanation of concepts."
            )

        else:

            overall_feedback = (
                "Needs improvement. "
                "Review the important concepts "
                "and practice more interview questions."
            )

        # ------------------------------------------
        # SAVE RESULT
        # ------------------------------------------

        completed_at = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        connection.execute(
            """
            INSERT INTO interview_results
            (
                user_id,
                domain,
                difficulty,
                total_score,
                total_questions,
                feedback,
                completed_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user_id,
                "Resume-Based",
                difficulty,
                final_score,
                question_count,
                overall_feedback,
                completed_at
            )
        )

        connection.commit()

        return jsonify({

            "message":
                "Resume interview evaluated successfully",

            "score":
                final_score,

            "total_questions":
                question_count,

            "feedback":
                overall_feedback,

            "completed_at":
                completed_at,

            "results":
                results

        }), 200

    except Exception as error:

        connection.rollback()

        print(
            "Resume evaluation error:",
            error
        )

        return jsonify({
            "message":
                "Could not evaluate resume interview."
        }), 500

    finally:

        connection.close()




if __name__ == "__main__":
        app.run(debug=True)

    