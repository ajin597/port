from flask import Flask, request, render_template_string
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Configurations
SMTP_SERVER = 'smtp.gmail.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Replace with your SMTP port (587 for TLS)
SMTP_USERNAME = 'cjebin9@gmail.com'  # Replace with your email
SMTP_PASSWORD = 'valchleyikulpfhk'  # Replace with your email password

@app.route('/')
def index():
    # Render your HTML form here
    return render_template_string(open('templates/index.html').read())

@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    # Prepare the email
    msg = MIMEText(f"Name: {name}\nEmail: {email}\n\n{message}")
    msg['Subject'] = subject
    msg['From'] = SMTP_USERNAME
    msg['To'] = SMTP_USERNAME  # Send to yourself

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_USERNAME, SMTP_USERNAME, msg.as_string())
        return "Your message has been sent. Thank you!"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
