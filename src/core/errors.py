from jsonrpc import BaseError


class AuthBearer(BaseError):
    CODE = 7000
    MESSAGE = 'Authorization Bearer error'


class AuthCredentialsError(BaseError):
    CODE = 7001
    MESSAGE = 'Auth credentials error'


class AccessTokenExpiredError(BaseError):
    CODE = 8000
    MESSAGE = 'Access Token expired'


class RefreshTokenExpiredError(BaseError):
    CODE = 8001
    MESSAGE = 'Refresh Token expired'


class AccountNotFound(BaseError):
    CODE = 6000
    MESSAGE = 'Account not found'


class Http404(BaseError):
    CODE = 404
    MESSAGE = 'Object DoesNotExist'


class APIException(BaseError):
    MESSAGE = 'Bad request'
    CODE = 400
