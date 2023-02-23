class AppException(Exception):
    pass


class NotFoundException(AppException):
    pass


class AuthorizationException(AppException):
    pass


class InvalidJwt(AuthorizationException):
    def __init__(self) -> None:
        super().__init__("Could not validate credentials")
