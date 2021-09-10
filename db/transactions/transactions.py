import utils.common as cf
from db.connection.db_conn import DbConnection
from db.transactions.sql_statements import SQLStatements as sqls
from db.transactions.constants import SQLConstants as sc
from db.transactions.validations import Validations
from db.transactions.exceptions import CreateUserException, UpdateUserException, UserException, UserNotFoundException, UserAlreadyExistsException
from db.transactions.messages import Messages as m
from db.connection.constants import DbConstants as dc


class User:


    def __init__(self):
        self.conn_instance = DbConnection(cf.get_env_var(dc.ENV_DB_USERNAME), cf.get_env_var(dc.ENV_DB_PASSWORD), 
                                        cf.get_env_var(dc.ENV_DB_HOSTNAME), cf.get_env_var(dc.ENV_DB_NAME))
    

    def select_user(self, user_id):
        cursor = self.conn_instance.execute_statement(sqls.get_fmtsql_stmt(sqls.SELECT_USER, [user_id]))
        return cursor.fetchall()


    def check_if_user_exists(self, user_id):
        return True if self.select_user(user_id) else False


    def create_user(self, user_id, name=None, dob=None, gender=None, email=None):
        try:
            Validations.validate_user_field(sc.USER_ID, user_id)
            Validations.validate_user_field(sc.USER_NAME, name)
            Validations.validate_user_field(sc.USER_DOB, dob)
            Validations.validate_user_field(sc.USER_GENDER, gender)
            Validations.validate_user_field(sc.USER_EMAIL, email)
        except UserException as e:
            raise CreateUserException(str(e))
        if self.check_if_user_exists(user_id):
            raise UserAlreadyExistsException(m.USER_ALREADY_EXISTS.format(user_id=user_id))
        self.conn_instance.execute_statement(
                        sqls.get_fmtsql_stmt(sqls.INSERT_USER, [user_id, name, dob, gender, email]))


    def delete_user(self, user_id):
        if not self.check_if_user_exists(user_id):
            raise UserNotFoundException(m.USER_NOT_FOUND.format(user_id=user_id))        
        self.conn_instance.execute_statement(sqls.get_fmtsql_stmt(sqls.DELETE_USER, [user_id]))


    def _update_user_detail(self, user_id, field_name, value_to_update):
        try:
            Validations.validate_user_field(field_name, value_to_update)
        except UserException as e:
            raise UpdateUserException(str(e))
        if not self.check_if_user_exists(user_id):
            raise UserNotFoundException(m.USER_NOT_FOUND.format(user_id=user_id))
        self.conn_instance.execute_statement(sqls.get_fmtsql_stmt(sqls.update_user(field_name), [user_id, value_to_update]))


    def update_user_name(self, user_id, name):
        self._update_user_detail(user_id, sc.USER_NAME, name)


    def update_user_email(self, user_id, email):
        self._update_user_detail(user_id, sc.USER_EMAIL, email)


    def update_user_gender(self, user_id, gender):
        self._update_user_detail(user_id, sc.USER_GENDER, gender)


    def update_user_dob(self, user_id, dob):
        self._update_user_detail(user_id, sc.USER_DOB, dob)



class Policies:

    def __init__(self):
        self.conn_instance = DbConnection(cf.get_env_var(dc.ENV_DB_USERNAME), 
                                        cf.get_env_var(dc.ENV_DB_PASSWORD), 
                                        cf.get_env_var(dc.ENV_DB_HOSTNAME), 
                                        cf.get_env_var(dc.ENV_DB_NAME))
        

    def add_policy(self, policy_id, customer_name, policy_start_date, sum_assured, premium_mode, premium_amount, 
                    user_id, mobile=None, email=None, residence_address=None, dob=None, height=None, weight=None, 
                    occupation=None, policy_no=None, policy_maturity_date=None, policy_period=None, policy_name=None, 
                    term=None, nominee_name=None, nominee_relation=None, father_full_name=None, mother_full_name=None, 
                    spouse_name=None, premium_receipt_given=False, policy_bond_given=False, other_details=None):
        pass