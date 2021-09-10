from os import stat
import mysql.connector

from mysql.connector import Error
from app_logging.log import Log
from db.connection.exception import DBException
from db.connection.messages import Messages

class DbConnection:
    """Base class for db connections, provides creation and cleanup of connection and means to execute statements"""

    def __init__(self, db_user, db_pass, db_hostname, db_name):
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_hostname = db_hostname
        self.db_name = db_name
        self.conn = self.get_connection()

        # Defensive check to make sure we have a connection
        if not self.conn:
            raise DBException(Messages.UNABLE_TO_AQUIRE_CONNECTION)


    def get_connection(self):
        try:
            conn = mysql.connector.connect(host=self.db_hostname, database=self.db_name, user=self.db_user, 
                                            password=self.db_pass, auth_plugin='mysql_native_password')

            if conn:
                return conn
            else:
                raise DBException(Messages.UNABLE_TO_AQUIRE_CONNECTION)
        except Error as e:
            raise DBException(Messages.UNABLE_TO_AQUIRE_CONNECTION + str(e))


    def __del__(self):
        """Ensures that the connection is closed when the instance gets out of scope"""
        try:
            if self.conn:
                self.conn.close()
        except mysql.connector.Error as e:
            raise DBException(Messages.UNABLE_TO_CLOSE_CONNECTION.format(message=str(e)))
        except AttributeError:
            Log.time_message(Messages.NO_CONNECTION_TO_CLOSE)


    def execute_statement(self, statement, params=None):
        """Execute a statement against current connection"""
        Log.time_message(Messages.EXECUTING_STATEMENT.format(statement=statement))
        try:
            cursor = self.conn.cursor(buffered=True)
            if params:
                cursor.execute(statement, params)
            cursor.execute(statement)
            self.conn.commit()
            return cursor
            
        except Error as e:
            raise DBException(Messages.FAILED_TO_EXECUTE.format(statement=statement, message=str(e)))
