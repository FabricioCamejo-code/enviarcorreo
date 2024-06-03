import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time
import textwrap

def enviar_email():
    try:
        # Configuración del remitente y destinatario
        remitente = "xxxxxx@gmail.com"
        destinatarios = ["xxxxxxx@gmail.com", "info@consultoresdeempresas.com", "info@grupoorono.com.ar", "rrhh@toyotsu.com.ar", "seleccion@mooksrrhh.com", "contacto@esentiarh.com", "consultas@vicentin.com.ar", "florencia_manrique@carrefour.com", "rrhh@juleriaque.com.ar", "busquedas@toyota.com.ar", "rrhh@randstad.com.ar", "info@randstad.com.ar", "cvrosario@excelencialaboral.com.ar", "cv@tpr.com.ar", "smirabelli@bayton.com.ar", "consultas@pullmenrosario.com.ar", "cv@citycenter-rosario.com.ar", "personal@crucijuegos.com", "ainza@consultoresdeempresas.com", "comercial@gruporta.com.ar", "cv@grta.odoo.com", "info@tconsultores.com.ar", "contacto@bayton.com.ar", "info@amia-empleos.org.ar", "contacto@asorum.com.ar", "matias.paciaroni@evolucionarh.com.ar", "info@excelencialaboral.com.ar", "cvrosario@excelencialaboral.com.ar"]
        for destinatario in destinatarios:
            # Crear el objeto Multipart
            mensaje = MIMEMultipart()
            mensaje['From'] = remitente
            mensaje['To'] = destinatario
            mensaje['Subject'] = "Solicitud de Empleo y Adjunto de Curriculum Vitae, Operario"

            # Cuerpo del mensaje como HTML
            cuerpo_mensaje = textwrap.dedent('''\
                <html>
                <body>
                <p>Estimado/a Gerente de Recursos Humanos:</p>
                <p>Espero que este correo lo/a encuentre bien.</p>
                <p>Me dirijo a usted para expresar mi interés en oportunidades laborales que puedan surgir en su organización. Como profesional en búsqueda activa de nuevos desafíos, deseo compartir mi hoja de vida adjunta para su consideración.</p>
                <p>En mi búsqueda de crecimiento profesional, he identificado a su empresa como un entorno donde puedo aportar mis habilidades y experiencia, así como aprender y desarrollarme en nuevos desafíos.</p>
                <p>Agradezco de antemano su tiempo y consideración. Quedo a disposición para ampliar cualquier información adicional que pudiera necesitar. Espero tener la oportunidad de discutir cómo mi experiencia y habilidades pueden contribuir al éxito de su equipo.</p>
                <p>Quedo a la espera de sus comentarios y aprovecho la oportunidad para enviarle un cordial saludo.</p>
                <p>Atentamente,</p>
                <p><img src="cid:imagen"></p>
                <p>xxxxxxxx</p>
                <p>xxxxxxx</p>
                <p>xxxxxx@gmail.com</p>
                </body>
                </html>
            ''')

            # Adjuntar el cuerpo del mensaje como HTML
            mensaje.attach(MIMEText(cuerpo_mensaje, 'html'))

            # Adjuntar la imagen
            with open("FABRI.png", "rb") as imagen:
                parte_imagen = MIMEBase("image", "jpeg")
                parte_imagen.set_payload(imagen.read())
            encoders.encode_base64(parte_imagen)
            parte_imagen.add_header("Content-ID", "<imagen>")
            mensaje.attach(parte_imagen)

            # Adjuntar el CV
            archivo_adjunto = "CV_2024050300273933.pdf"
            with open(archivo_adjunto, "rb") as adjunto:
                parte_adjunta = MIMEBase('application', 'octet-stream')
                parte_adjunta.set_payload(adjunto.read())
            encoders.encode_base64(parte_adjunta)
            parte_adjunta.add_header('Content-Disposition', f"attachment; filename= {archivo_adjunto}")
            mensaje.attach(parte_adjunta)

            # Conexión al servidor SMTP de Gmail
            servidor_smtp = smtplib.SMTP('smtp.gmail.com', 587)
            servidor_smtp.starttls()
            servidor_smtp.login(remitente, "xxxx xxxx xxxx xxxx")

            # Envío del correo electrónico
            servidor_smtp.sendmail(remitente, destinatario, mensaje.as_string())
            print("Correo enviado correctamente a", destinatario)

            # Cerrar conexión
            servidor_smtp.quit()

    except Exception as e:
        print("Se ha producido un error durante el envío del correo electrónico:", str(e))

# Bucle para enviar el correo cada 24 horas
while True:
    enviar_email()
    # Esperar 8 min aprox. (600 segundos)
    time.sleep(600)
