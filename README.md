# AI-interview-evaluation

Starter full-stack scaffold for the **AI-Powered Mock Interview System** using **React + Flask + MongoDB**. This repo provides a working baseline with key API routes, data models, and UI pages that map to the requested features.

## Structure

```
backend/
  app/
    routes/
    services/
    utils/
  app.py
  requirements.txt
  .env.example
frontend/
  src/
    pages/
    services/
  index.html
  package.json
```

## Backend

### Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python app.py
```

### API Endpoints (sample)

- `POST /api/auth/signup`
- `POST /api/auth/verify-otp`
- `POST /api/auth/login`
- `POST /api/auth/forgot-password`
- `POST /api/auth/reset-password`
- `POST /api/resume/upload`
- `POST /api/interview/submit`
- `POST /api/interview/report`
- `POST /api/interview/email-report`
- `GET /api/dashboard/profile`
- `GET /api/dashboard/history`
- `GET /api/admin/users`
- `DELETE /api/admin/users/<user_id>`
- `GET /api/admin/interviews`
- `POST /api/admin/roles`
- `POST /api/admin/questions`
- `POST /api/chatbot/ask`

## Frontend

```bash
cd frontend
npm install
npm run dev
```

## Environment Variables

See `backend/.env.example` for MongoDB Atlas and SMTP settings.

## Notes

- The current code provides placeholder services for ATS scoring, interview evaluation, and HR chatbot responses.
- Extend `backend/app/services/` with production ML pipelines (Whisper, MediaPipe, ATS analysis) and integrate file uploads and GridFS.
- The UI pages are minimal but wired to API endpoints for quick iteration.
