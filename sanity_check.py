import smtplib, ssl
import pandas as pd

def sanity_check():
    df = pd.read_csv('sales_force.csv')
    check_list = ['Type', 'Properties', 'Description']

    for word in check_list:
        m = df['Column Description'].str.contains(word).mean()
        if m != 1:
            send_mail()
            print('Sanity error')
            return False
    return True


def send_mail():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "informativos.atha@gmail.com"  # Enter your address
    receiver_email = "informativos.atha@gmail.com"  # Enter receiver address
    password = 'Givilata_12022518'
    message = """\
    Subject: Hi there, sanity check not worked

    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)