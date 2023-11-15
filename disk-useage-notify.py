#pip install psutil

import psutil
import smtplib
from email.message import EmailMessage

def send_alert(disk_usage, threshold):
    msg = EmailMessage()
    msg.set_content(f"Warning: Disk usage is at {disk_usage}% which exceeds the threshold of {threshold}%")
    msg['Subject'] = "Disk Usage Alert"
    msg['From'] = 'sender@example.com'
    msg['To'] = 'recipient@example.com'

    # SMTP configuration
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login('username', 'password')
    server.send_message(msg)
    server.quit()

def check_disk_usage(threshold=80):
    # Adjust the partition as needed, e.g., "/" for the root partition in Linux
    partition = "/"
    disk_usage = psutil.disk_usage(partition).percent
    print(f"Disk usage for {partition}: {disk_usage}%")

    if disk_usage > threshold:
        print("Disk usage exceeds the threshold, sending alert...")
        send_alert(disk_usage, threshold)

check_disk_usage()
