from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


def jwtPayloadHandler(token, user=None, request=None):
    return {
        'token': token,
        'user': {
            'name': user.username
        }
    }


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token
