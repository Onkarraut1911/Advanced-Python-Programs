from logging import *

basicConfig(
    filename="logfile_logging_3.log", level=DEBUG
)  # default level is warning now in this changed to debug so all run
debug("This is Debug")
info("This is Info")
warning("This is warning")
error("This is Warning")
critical("This is critical")
