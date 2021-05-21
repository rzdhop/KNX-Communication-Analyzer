'''
Created on 03-03-2021

@author: Guillaume
'''

import os
import datetime
from tkinter import messagebox


class logs:

    def __init__(self, path: str = None):
        """
        Initialization of the logs repo path
        If there is no initialized path, take a relative path.
        """

        if path == None:
            path = str(os.path.dirname(__file__))

        path = path + "/logs"

        self.path = path

        try:
            if not os.path.exists(path):
                os.mkdir(path)
        except OSError:
            messagebox.showerror(title="Err", message="Creation Failed")

    def err(self, err: str = None):
        """
        Method to log the error
        """
        print(err)

        try:
            file = open(self.path + "/Err.txt", 'a')

            date = datetime.datetime.now()

            if err == None:
                err = "Unknown error"

            messagebox.showerror(title="Err", message=err)

            file.write("--------- {0} {1} {2} {3} {4} ---------\n{5}\n\n\n".format(date.strftime(
                "%Y"), date.strftime("%A"), date.strftime("%d"), date.strftime("%B"), date.strftime("%X"), err))

            file.close()

        except IOError:
            messagebox.showerror(title="Err", message="Can't log Err")

    def info(self, info: str):
        """
        Method for logging information
        """

        print(info)

        try:
            file = open(self.path + "/Info.txt", 'a')

            date = datetime.datetime.now()

            file.write("--------- {0} {1} {2} {3} {4} ---------\n{5}\n\n\n".format(date.strftime(
                "%Y"), date.strftime("%A"), date.strftime("%d"), date.strftime("%B"), date.strftime("%X"), info))

            file.close()

        except IOError:
            messagebox.showerror(title="Err", message="Can't log Info")
