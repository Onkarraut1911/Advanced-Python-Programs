from logging import *

basicConfig(
    filename="logfile.log"
)  # this is file created in current directory , you can specify full path if you want other directory

warning("This is Warning")
error("This is Error")
critical("This is Critical")
