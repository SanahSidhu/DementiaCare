from core.errorfactory import AuthenticationErrors


class InvalidUserCredentialsError(AuthenticationErrors):
    ...


class UserDoesNotExistError(AuthenticationErrors):
    ...


class UserExistsError(AuthenticationErrors):
    ...
