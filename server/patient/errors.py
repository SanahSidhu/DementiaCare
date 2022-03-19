from core.errorfactory import (
    AuthenticationErrors,
    ChecklistErrors,
    NotesErrors,
    DataErrors,
    AWSErrors,
)


class InvalidUserCredentialsError(AuthenticationErrors):
    ...


class UserDoesNotExistError(AuthenticationErrors):
    ...


class ChecklistDataEmptyError(ChecklistErrors):
    ...


class NotesDataEmptyError(NotesErrors):
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
