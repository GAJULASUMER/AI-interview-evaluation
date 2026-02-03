import smtplib
from email.message import EmailMessage
from flask import current_app


def send_email(to_email: str, subject: str, body: str, attachment_path: str | None = None) -> None:
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = current_app.config["SMTP_SENDER"]
    message["To"] = to_email
    message.set_content(body)

    if attachment_path:
        with open(attachment_path, "rb") as attachment:
            message.add_attachment(
                attachment.read(),
                maintype="application",
                subtype="pdf",
                filename="interview_report.pdf",
            )

    with smtplib.SMTP(current_app.config["SMTP_HOST"], current_app.config["SMTP_PORT"]) as smtp:
        smtp.starttls()
        if current_app.config["SMTP_USER"]:
            smtp.login(current_app.config["SMTP_USER"], current_app.config["SMTP_PASSWORD"])
        smtp.send_message(message)
