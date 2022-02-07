from core.errorfactory import AuthenticationErrors


class UserExistsError(AuthenticationErrors):
    ...


class UserDoesNotExistError(AuthenticationErrors):
    ...


class InvalidUserCredentialsError(AuthenticationErrors):
    ...
