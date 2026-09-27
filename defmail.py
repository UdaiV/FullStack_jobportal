from email.message import EmailMessage
import ssl
import smtplib
import threading
def _smtp_worker(email_sender,email_receiver,email_password,em):
    
    try:
        context=ssl.create_default_context()
        print("Connecting to server...")
        with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
            smtp.login(email_sender,email_password)
            print("Logged in successfully. Sending email...")
            smtp.sendmail(email_sender,email_receiver,em.as_string())
            print("Email sent successfully!")
            
    except Exception as e:
        print(f"An error occurred: {e}")
        

def send_otp(otp,email_receiver):
    
    email_sender = "to-mail-id"
    email_password="your-passcode-here"
    
    subject= "---Your Account Verification Code---"
    body= f" Your OTP for Skill hunt Account Verification is {otp}"


    em=EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    try:
        # 3. Start the background thread, passing all 4 arguments
        bg_thread = threading.Thread(
            target=_smtp_worker, 
            args=(email_sender, email_receiver, email_password, em)
        )
        bg_thread.start()
        
        # ⚡ 4. Instantly return True to views.py so the page loads immediately
        return True, "Email processing started in background..."
        
    except Exception as e:
        return False, f"Failed to initialize background thread: {e}"
    