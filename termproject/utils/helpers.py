import jwt
import datetime

from mailjet_rest import Client

from termproject.config import SECRET_KEY
from termproject.utils.emailTemplates import verify_email, reset_password

#encoding jwt token
def encodeToken(email):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            'iat': datetime.datetime.utcnow(),
            'sub': email
        }
        return jwt.encode(
            payload,
            SECRET_KEY,
            algorithm='HS256'
        )
    except Exception as e:
        return e

#decoding jwt token
def decodeToken(auth_token):
    try:
        payload = jwt.decode(auth_token, SECRET_KEY, algorithms=["HS256"])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. try again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. try again.'

#sending email using mailjet api
def sendEmail(email, name, token, type):
    api_key = ''
    api_secret = ''
    mailjet = Client(auth=(api_key, api_secret), version='v3')
    subject = {
        "verify": "Verify your email",
        "reset": "Reset your password"
    }
    if type == "verify":
        template = verify_email.substitute(token=token, name=name)
    elif type == "reset":
        template = reset_password.substitute(token=token)

    data = {
        'FromEmail': "verifyemail425@gmail.com",
        'FromName': "Heart Disease Classifier",
        'Recipients': [
            {
                "Email": email,
                "Name": name
            }
        ],
        'Subject': subject[type],
        'Text-part': "Dear passenger, welcome to Mailjet! May the delivery force be with you!",
        'Html-part': template
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())