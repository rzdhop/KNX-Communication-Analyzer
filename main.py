# main
import gui
from logs import logs

# init the repo of the logs
log = logs()

try:

    print("Gui")

except Exception as err:
    log.err(err)
