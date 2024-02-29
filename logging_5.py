from logging import *

basicConfig(
    filename="logfile_logging_5.log",
    level=DEBUG,
    filemode="w",
    format="%(asctime)s -- %(message)s",  # this is add date and time related info in file and our messages
)
debug("This is Debug in write Mode")
info("This is Info")
warning("This is warning")
error("This is Warning")
critical("This is critical")
