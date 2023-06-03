import sys
from src.logger import logging


def error_message_deatails (error,error_deatails:sys):
        _,_,exc_tb  = error_deatails.exc_info()
        filename = exc_tb.tb_frame.f_code.co_filename
        error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}].format()"
        filename,exc_tb.tb_lineno,str(error)
        

class customexception (Exception):
        def __init__ (self,error_message,error_deatails:sys):
                 super().__init__(error_message)
                 self.error_message = error_message_deatails(error_message,error_deatails=error_deatails )
        

        def __str__(self) :
                return self.error_message
        
