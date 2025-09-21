import smtplib
import os
import mimetypes
from email.message import EmailMessage
from getpass import getpass # For securely getting the email password

# ANSI Styles
class Styles:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

# Prompt user for email details
def prompt_email_details():
    print(f"{Styles.BOLD}{Styles.CYAN}Email Automation Setup{Styles.RESET}")
    sender = input("Sender Email: ")
    password = getpass("Password (hidden): ")
    recipients = input("Recipient Email(s) (comma-separated): ").split(',')
    subject = input("Subject: ")
    body = input("Message Body: ")
    html_format = input("Send as HTML? (y/n): ").strip().lower()
    attachments = input("Attachment file paths (comma-separated, optional): ").split(',')

    return sender, password, recipients, subject, body, html_format, attachments

# Create and configure the email message
def create_email(sender, recipients, subject, body, html_format, attachments):
    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = subject

    # Set content type based on user preference
    if html_format == 'y':
        msg.add_alternative(body, subtype='html')
    else:
        msg.set_content(body)

    # Attach files if provided
    for path in attachments:
        path = path.strip()
        if path and os.path.exists(path):
            mime_type, _ = mimetypes.guess_type(path)
            maintype, subtype = mime_type.split('/') if mime_type else ('application', 'octet-stream')
            with open(path, 'rb') as f:
                msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=os.path.basename(path))
        elif path:
            print(f"{Styles.RED}Attachment not found: {path}{Styles.RESET}")

    return msg

# Send the email using SMTP
def send_email(sender, password, msg):
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender, password)
            smtp.send_message(msg)
        print(f"{Styles.GREEN}Email sent successfully!{Styles.RESET}")
    except Exception as e:
        print(f"{Styles.RED}Failed to send email: {e}{Styles.RESET}")

# Main loop for repeated email sending
def main():
    print(f"{Styles.BOLD}{Styles.GREEN}Welcome to the Email Automation!{Styles.RESET}")

    while True:
        # Gather email details from user
        sender, password, recipients, subject, body, html_format, attachments = prompt_email_details()
        # Build the email message
        msg = create_email(sender, recipients, subject, body, html_format, attachments)
        # Send the email
        send_email(sender, password, msg)

        # Ask if the user want to send another email
        again = input("Do you want to send another email? (y/n): ").strip().lower()
        if again != 'y':
            print(f"{Styles.YELLOW}Exiting Email Automation. Goodbye!{Styles.RESET}")
            break

if __name__ == "__main__":
    main()