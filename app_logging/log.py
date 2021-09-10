import time
import sys

class Log:

    TIME = "TIME"
    WARNING = "WARNING"
    ERROR = "ERROR"
    DEBUG = "DEBUG"


    @staticmethod
    def __format_message(log_type, message):
        message = message.replace("\n", "")
        if log_type == Log.WARNING or log_type == Log.ERROR or log_type == Log.DEBUG:
            message = log_type + ": " + message
        message = time.strftime("%d/%m/%Y") + " " + time.strftime("%H:%M:%S") + " - " + message
        return message


    @staticmethod
    def log(log_type, message):
        if log_type == Log.TIME:
            print(Log.__format_message(Log.TIME, message))


    @staticmethod
    def time_message(message):
        Log.log(Log.TIME, message)
    

    @staticmethod
    def debug_message(message):
        Log.log(Log.DEBUG, message)
