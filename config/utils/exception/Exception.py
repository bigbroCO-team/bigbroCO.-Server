from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler
# from config.settings.base import log


class BaseCustomException(APIException):
    status_code = 400
    default_code = "default_code"
    default_detail = "default_detail"


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code

    # log.error(response.data)

    return response