from core.errorfactory import AuthenticationErrors, AWSErrors, DataErrors


class InvalidUserCredentialsError(AuthenticationErrors):
    ...


class UserDoesNotExistError(AuthenticationErrors):
    ...


class UserExistsError(AuthenticationErrors):
    ...


class InvalidInsertionError(DataErrors):
    ...


class DataInsertionError(DataErrors):
    ...


class InvalidFieldError(DataErrors):
    ...


class DataFetchingError(DataErrors):
    ...


class DataRemovalError(DataErrors):
    ...


class AWSDownloadError(AWSErrors):
    ...


class AWSUploadError(AWSErrors):
    ...
