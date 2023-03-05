from typing import Optional


class AppException(Exception):
    pass


class NotFoundException(AppException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message or "Could not find resource"
        super().__init__(message)


class AuthorizationException(AppException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message or "Could not validate credentials"
        super().__init__(message)


class UserExists(AppException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message or "A user with this email or phone exists already"
        super().__init__(message)


class InvalidCredentials(AuthorizationException):
    def __init__(self, message: Optional[str] = None) -> None:
        message = message or "Invalid email or password"
        super().__init__(message)


class InvalidJwt(AuthorizationException):
    pass
