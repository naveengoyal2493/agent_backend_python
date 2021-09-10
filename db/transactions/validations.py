import utils.common as cf
from app_logging.log import Log
from db.transactions.exceptions import UserException
from db.transactions.constants import SQLConstants as sc
from db.transactions.messages import Messages as m


class Validations:

    @staticmethod
    def validate_user_field(field_name, value_to_update):
        if field_name == sc.USER_ID:
            if not value_to_update:
                raise UserException(m.USER_ID_CANNOT_BE_EMPTY)
            if not len(value_to_update) == sc.USER_ID_LENGTH:
                raise UserException(m.USER_ID_IS_INCORRECT)
            return

        if value_to_update:
            if field_name == sc.USER_NAME:
                Log.debug_message(m.FIELD_NAME.format(field_name=field_name))
                if not cf.is_string_size_less_then_length(value_to_update, sc.NAME_LENGTH):
                    raise UserException(m.NAME_CANNOT_EXCEED_LIMIT.format(name_length=sc.NAME_LENGTH))
            elif field_name == sc.USER_GENDER:
                Log.debug_message(m.FIELD_NAME.format(field_name=field_name))
                if not cf.does_string_exist_in_list(value_to_update, sc.GENDER_NOTATIONS):
                    raise UserException(m.INVALID_GENDER)
            elif field_name == sc.USER_DOB:
                Log.debug_message(m.FIELD_NAME.format(field_name=field_name))
                if not cf.is_valid_date(value_to_update, sc.DATE_FORMAT):
                    raise UserException(m.INVALID_DOB.format(dob=value_to_update))
            elif field_name == sc.USER_EMAIL:
                Log.debug_message(m.FIELD_NAME.format(field_name=field_name))
                if not (cf.is_string_size_less_then_length(value_to_update, sc.EMAIL_LENGTH) and cf.is_valid_email(value_to_update)):
                    raise UserException(m.INVALID_EMAIL)
            else:
                Log.debug_message(m.INVALID_FIELD_NAME)
                raise UserException(m.INVALID_FIELD_NAME)

