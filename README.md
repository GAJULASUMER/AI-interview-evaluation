# AI-Based Automated Interview Evaluation System (Flask + MySQL)

This project recreates an AI interview evaluation workflow using:
- **Backend:** Flask (Python)
- **Frontend:** HTML/CSS/JavaScript (Jinja templates)
- **Database:** MySQL

## Features
1. User authentication (register/login/logout)
2. Resume upload (`pdf/doc/docx/txt`) and parsing
3. AI-style interview question generation from extracted skills
4. Real-time answer capture via text + browser voice input
5. NLP-based answer evaluation (relevance + depth)
6. Scoring + feedback generation for each question
7. Dashboard with score history and latest detailed report
8. Persistent storage of users/resumes/interview records

## Folder Structure

```
/app.py
/templates
/static
/models
/database
/routes
/utils
/requirements.txt
```

## Setup Instructions

1. **Create MySQL DB and tables**
   ```bash
   mysql -u root -p < database/schema.sql
   ```

2. **Create virtual environment and install dependencies**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Set environment variables** (optional defaults exist)
   ```bash
   export SECRET_KEY='your-secret'
   export MYSQL_HOST='127.0.0.1'
   export MYSQL_PORT='3306'
   export MYSQL_USER='root'
   export MYSQL_PASSWORD='password'
   export MYSQL_DB='ai_interview'
   export UPLOAD_FOLDER='uploads'
   ```

4. **Run application**
   ```bash
   python app.py
   ```

5. Open browser: `http://127.0.0.1:5000`

## Workflow
1. Register/Login
2. Upload resume
3. Start AI-generated interview
4. Answer by typing or voice input button
5. Submit interview to receive scoring and feedback
6. View history and detailed report in dashboard
