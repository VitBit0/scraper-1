from email.message import EmailMessage
import ssl
import smtplib as smt
def send_email(con,tar):
    contenuto=str(con)
    bot="redtread.0@gmail.com"
    em=EmailMessage()
    em["From"]=bot
    em["To"]=tar
    em["Subject"]="esempio oggetto email"
    em.set_content(contenuto)
    try:
        context=ssl.create_default_context()
        email=smt.SMTP_SSL("smtp.gmail.com", 465, context=context)
        email.login(bot ,"oynklhanjhslxjrx")
        email.sendmail(bot,tar,em.as_string())
        email.close()
        print("Done!")
    except:
        print("scusa è avvenuto un errore",TypeError)
      