from config.util.exception.exception import BaseCustomException


class CustomException:
    # Authentication
    UnauthorizedError = BaseCustomException(code=401, detail='Unauthorized')
    TokenExpiredError = BaseCustomException(code=403, detail="Token is expired")
    InvalidTokenError = BaseCustomException(code=403, detail="Invalid token error")

    # User
    UserNotFoundError = BaseCustomException(code=400, detail='User not found')