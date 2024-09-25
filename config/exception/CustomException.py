from config.exception.Exception import BaseCustomException

class CustomException:
    # Kakao OAuth
    KakaoOAuthCodeIsNotValid = BaseCustomException(code=400, detail='Kakao OAuth code is not valid.')
    KakaoOAuthAccessTokenIsNotValid = BaseCustomException(code=400, detail='Kakao OAuth access token is not valid.')