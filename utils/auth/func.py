from rest_framework.exceptions import AuthenticationFailed
from functools import wraps
import jwt
from common.models import Customer
from config.settings import SECRET_KEY


def IsAuthenticated(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        token = request.COOKIES.get('access')

        if not token:
            raise AuthenticationFailed('Token is missing')

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

            user = Customer.objects.filter(username=payload['username']).first()

            if not user:
                raise AuthenticationFailed('User not found')

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token is expired')
        except Exception as e:
            raise AuthenticationFailed(str(e))
        return func(self, request, *args, **kwargs)

    return wrapper