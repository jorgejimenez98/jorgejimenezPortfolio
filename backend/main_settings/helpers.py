from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


def get_spanish_text(full_name):
    return f"""
        Hola {full_name}, muchas gracias por contactarme, en menos de 24 horas te contactaré (Esto es un mensaje programado)
    """


def get_english_text(full_name):
    return f"""
        Hello {full_name}, thank you very much for contacting me, in less than 24 hours I will contact you (This is a scheduled message)
    """


def send_email_to_user(params, sender_email):
    params['isForMe'] = False
    full_name = params.get('fullName', '')
    language = params.get('languaje', 'es')
    context = {
        'message': get_spanish_text(full_name) if language == 'es' else get_english_text(full_name)
    }
    htmly = get_template('email.html')
    subject = 'Hello' if language == 'en' else 'Hola'
    to  = params["email"]
    html_content = htmly.render(context)
    msg = EmailMultiAlternatives(
        subject, params['message'], sender_email, [to]
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def send_email_to_me(params):
    import os 
    params['isForMe'] = True
    htmly = get_template('email.html')
    to  = os.environ.get('EMAIL_HOST_USER')
    html_content = htmly.render(params)
    subject = 'Hola, alguien te ha escrito a tu portafolio'
    msg = EmailMultiAlternatives(
        subject, params['message'], params['email'], [to]
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
