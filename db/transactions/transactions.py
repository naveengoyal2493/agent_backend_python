from typing import NamedTuple
from db.connection.db_conn import DbConnection
from db.transactions.sql_statements import SQLStatements as sqls
from db.transactions.exceptions import UserNotFoundException
from db.transactions.messages import Messages
from db.connection.constants import DbConstants as dc
from utils.common import get_env_var
from app_logging.log import Log

class User:

    def __init__(self):
        self.conn_instance = DbConnection(get_env_var(dc.ENV_DB_USERNAME), 
                                        get_env_var(dc.ENV_DB_PASSWORD), 
                                        get_env_var(dc.ENV_DB_HOSTNAME), 
                                        get_env_var(dc.ENV_DB_NAME))
    

    def create_user(self, user_id, name=None, dob=None, gender=None, email=None):
        self.conn_instance.execute_statement(
                        sqls.get_fmtsql_stmt(sqls.INSERT_USER, [user_id, name, dob, gender, email]))


    def delete_user(self, user_id):
        if not self.check_if_user_exists(user_id):
            raise UserNotFoundException(Messages.USER_NOT_FOUND.format(user_id=user_id))        
        self.conn_instance.execute_statement(sqls.get_fmtsql_stmt(sqls.DELETE_USER, [user_id]))

    
    def select_user(self, user_id):
        cursor = self.conn_instance.execute_statement(sqls.get_fmtsql_stmt(sqls.SELECT_USER, [user_id]))
        return cursor.fetchall()


    def update_user_name(self, user_id, name):
        if not self.check_if_user_exists(user_id):
            raise UserNotFoundException(Messages.USER_NOT_FOUND.format(user_id=user_id))
        self.conn_instance.execute_statement(sqls.get_fmtsql_stmt(sqls.UPDATE_USER_NAME, [user_id, name]))


    def update_user_dob(self, user_id, dob):
        if not self.check_if_user_exists(user_id):
            raise UserNotFoundException(Messages.USER_NOT_FOUND.format(user_id=user_id))
        self.conn_instance.execute_statement(sqls.get_fmtsql_stmt(sqls.UPDATE_USER_DOB, [user_id, dob]))


    def update_user_gender(self, user_id, gender):
        if not self.check_if_user_exists(user_id):
            raise UserNotFoundException(Messages.USER_NOT_FOUND.format(user_id=user_id))
        self.conn_instance.execute_statement(sqls.get_fmtsql_stmt(sqls.UPDATE_USER_GENDER, [user_id, gender]))


    def update_user_email(self, user_id, email):
        if not self.check_if_user_exists(user_id):
            raise UserNotFoundException(Messages.USER_NOT_FOUND.format(user_id=user_id))
        self.conn_instance.execute_statement(sqls.get_fmtsql_stmt(sqls.UPDATE_USER_EMAIL, [user_id, email]))


    def check_if_user_exists(self, user_id):
        return True if self.select_user(user_id) else False