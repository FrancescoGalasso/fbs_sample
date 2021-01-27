# -*- coding: utf-8 -*-

# pylint: disable=no-name-in-module

""" FBS Sample Project """

import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext, cached_property
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class AppContext(ApplicationContext):
    """ FBS App Context """

    def run(self):
        self.main_window.show()
        return self.app.exec_()

    @cached_property
    def main_window(self):      #pylint: disable=missing-function-docstring
        return MainWindow(self)


class MainWindow(QMainWindow):  # pylint: disable=too-few-public-methods
    """ Main Window """

    def __init__(self, ctx):
        super(MainWindow, self).__init__()  # pylint: disable=super-with-arguments
        self.ctx = ctx
        self.ui_path = self.ctx.get_resource('main_window.ui')
        uic.loadUi(self.ui_path, self)

        self.setWindowTitle("FBS Sample Project")
        self.show()


if __name__ == '__main__':
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)
