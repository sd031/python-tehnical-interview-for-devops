#pip install pymysql smtplib

import subprocess
import smtplib
from email.message import EmailMessage
import datetime
import os

# Database Configuration
DB_HOST = 'localhost'
DB_USER = 'your_db_username'
DB_PASSWORD = 'your_db_password'
DB_NAME = 'your_db_name'
BACKUP_PATH = '/path/to/backup/folder/'

# Email Configuration
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
EMAIL_USER = 'your_email@example.com'
EMAIL_PASSWORD = 'your_email_password'
RECIPIENT_EMAIL = 'recipient@example.com'

def send_email(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_USER
    msg['To'] = RECIPIENT_EMAIL

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")

def backup_database():
    # Create a timestamped backup file
    filestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    filename = f"{DB_NAME}-{filestamp}.sql"
    filepath = os.path.join(BACKUP_PATH, filename)

    # Run the backup command
    command = f"mysqldump -h {DB_HOST} -u {DB_USER} -p{DB_PASSWORD} {DB_NAME} > {filepath}"
    
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"Backup successful: {filename}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Backup failed: {e}")
        send_email("Database Backup Failed", f"Backup failed for {DB_NAME} at {filestamp}")
        return False

if __name__ == "__main__":
    backup_database()
