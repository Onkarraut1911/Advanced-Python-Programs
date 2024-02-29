from logging import *

basicConfig(
    filename="logfile_logging_4.log",
    level=DEBUG,
    filemode="w",  # default filemode is apend int his changed to write
)  # default level is warning now in this changed to debug so all run
debug("This is Debug in write Mode")  # write mode overrite the data in the file
info("This is Info")
warning("This is warning")
error("This is Warning")
critical("This is critical")
