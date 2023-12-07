"""
  Playing around with logging in Python
"""

import logging


def simple_method(name):
    return name + " called"


"""
    If you want to change the logging, you need to call basicConfig FIRST!  before any calls to log
"""
logging.basicConfig(level=logging.DEBUG) # Debugging should now be turned on, so we see the end log message
#logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s') # Write logs to file
#logging.basicConfig(format='%(process)d %(asctime)s %(levelname)s: %(message)s')  # Include the process ID and timestamp

logging.debug("Starting logging_playing script")

# In the default logger 'debug' and 'info' are turned off
logging.debug("Logging a debug message")
logging.info("Logging a info message")
logging.warning("Logging a warning message")
logging.error("Logging a error message")
logging.critical("Logging a critical message")



name = "Tom"
print(simple_method(name))

# when logging a variable, it is best not to use f-string formatting, and pass in the variable as an arument due to lazy evaluation
logging.debug("Processing with name %s", name)
int_var = 10
float_var = 99.99
logging.debug("Multiple arguments: %s %i %f", name, int_var, float_var) # note you can use %s for all types it seems

# Capture Errors and stack traces:
a = 5
b = 0
try:
    c = a / b
except Exception as e:
    logging.error("Exception occurred", exc_info=True)

# This should be the same as above
try:
    c2 = a / b
except Exception as e:
    logging.exception("Exception occurred")

    

logging.debug("Done logging_playing script")