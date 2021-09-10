class UserException(Exception):
    pass


class UserNotFoundException(UserException):
    pass


class UserAlreadyExistsException(UserException):
    pass


class CreateUserException(UserException):
    pass


class UpdateUserException(UserException):
    pass