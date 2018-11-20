import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Correo():
    def __init__(self, enviar_a, asunto):
        self.fromaddr = "lumaku97@gmail.com"
        self.toaddr = enviar_a

        self.msg = MIMEMultipart()
        self.msg['From'] = 'ECFM_proyecto_final <' + self.fromaddr + '>'
        self.msg['To'] = self.toaddr 
        self.msg['Subject'] = asunto
    
    def cuerpo(self, contenido):
        body = contenido
        self.msg.attach(MIMEText(body, 'plain'))

    def enviar(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.fromaddr, "Helpm98msoyluis")
        server.sendmail(self.fromaddr, self.toaddr, self.msg.as_string())
        server.quit()