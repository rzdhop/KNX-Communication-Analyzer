# main
from gui import *
from logs import logs

# init the repo of the logs
log = logs()

try:

    f1 = Tk()
    f1.resizable(width = 1000, height = 1000)
    app = Fenetre_principale(f1)
    f1.mainloop()  

except Exception as err:
    log.err(err)
