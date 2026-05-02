from flask import Flask, redirect, url_for
from database.db import close_db
from routes.auth_routes import auth_bp
from routes.resume_routes import resume_bp
from routes.interview_routes import interview_bp
from routes.dashboard_routes import dashboard_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object("database.config.Config")

    app.register_blueprint(auth_bp)
    app.register_blueprint(resume_bp)
    app.register_blueprint(interview_bp)
    app.register_blueprint(dashboard_bp)

    app.teardown_appcontext(close_db)

    @app.route("/")
    def home():
        return redirect(url_for("auth.login"))

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
