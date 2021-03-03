import time

from PyQt5.QtGui import QTextCursor

import global_list

def delay_us():
    for i in range(100):
        pass


def print_log(str):
    try:
        global_list.textLog.moveCursor(QTextCursor.End)
        global_list.textLog.insertPlainText(str)
        global_list.textLog.moveCursor(QTextCursor.End)
    except Exception:
        print("print_log错误了")