from logging import *

LOG_FORMAT = (
    "%(asctime)s -- %(message)s -- %(lineno)d"  # line no of this file show in log file
)
basicConfig(
    filename="logfile_logging_6.log",
    level=DEBUG,
    filemode="w",
    format=LOG_FORMAT,  # this is add date and time related info in file and our messages
)
debug("This is Debug in write Mode")
info("This is Info")
warning("This is warning")
error("This is Warning")
critical("This is critical")
