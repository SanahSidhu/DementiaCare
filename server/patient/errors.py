from core.errorfactory import AuthenticationErrors, AWSErrors


class InvalidUserCredentialsError(AuthenticationErrors):
    ...


class UserDoesNotExistError(AuthenticationErrors):
    ...


class UserExistsError(AuthenticationErrors):
    ...


class AWSDownloadError(AWSErrors):
    ...


class AWSUploadError(AWSErrors):
    ...
