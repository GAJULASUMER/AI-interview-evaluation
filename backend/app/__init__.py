from flask import Flask
from .config import Config
from .extensions import mongo
from .routes.auth import auth_bp
from .routes.resume import resume_bp
from .routes.interview import interview_bp
from .routes.dashboard import dashboard_bp
from .routes.admin import admin_bp
from .routes.chatbot import chatbot_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(resume_bp, url_prefix="/api/resume")
    app.register_blueprint(interview_bp, url_prefix="/api/interview")
    app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")
    app.register_blueprint(admin_bp, url_prefix="/api/admin")
    app.register_blueprint(chatbot_bp, url_prefix="/api/chatbot")

    @app.get("/api/health")
    def health_check():
        return {"status": "ok"}

    return app
