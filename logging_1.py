from logging import *

debug("This is Debug")
info("This is Info")
# debug and info is low precedence than warning and error and critical is higher precedence than warning so only print warning and critical and error
warning("This is Warning")  # This is default
error("This is Error")
critical("This is Critical")
