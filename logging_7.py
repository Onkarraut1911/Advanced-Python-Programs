from logging import *

LOG_FORMAT = "{asctime} -- {name} -- {message} -- {lineno}"  # style ='{'  this is changed writing syntex of this msg , {name} - give the loger name , default logger name is root

basicConfig(
    filename="logfile_logging_7.log",
    level=DEBUG,
    filemode="w",
    format=LOG_FORMAT,  # this is add date and time related info in file and our messages
    style="{",
)


logger = getLogger(
    "NAME"
)  # this is function return logger changed loger name to NAME  default name is root

# if you does not specify  loagger.  then its give default logger name root
logger.debug("This is Debug in write Mode")
logger.info("This is Info")
logger.warning("This is warning")
logger.error("This is Warning")
logger.critical("This is critical")
