from flask import g, current_app
from app.extensions import auth
from config import Config
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired


def verify_auth_token(token):
    serializer = Serializer(Config.SECRET_KEY)
    try:
        serializer_data = serializer.loads(token)
        return serializer_data
    except SignatureExpired:
        return None
    except BadSignature:
        return None


@auth.verify_password
def verify_password(token, password):
    # current_app.logger.debug(token)
    infos = verify_auth_token(token)
    if not infos:
        return False
    else:
        g.userId = int(infos['userId'])
        return True
