import _thread

from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
import time

import gui
from global_fun import print_log
from gui import Ui_WinControl
import sys

import global_list

from serial_process.serail_process import  serail_data_process
import keyboard


class MyThread(QThread):
    #定义一个256字节的数组，用于接收串口数据
    hex_array = [0] * 256
    #接收的数据长度
    hex_len = 0
    out_serial = ""

    cipherid = ' '
    lockname = ' '
    factarykey = ''

    count = 0

    signal = pyqtSignal(int,int)
    signal_log = pyqtSignal(str)
    isbus = '0'

    factory_result = [0, 0, 0, 0, 0, 0, 0]


    def __init__(self):
        super(MyThread, self).__init__()

    # self.textSend.toPlainText()
    def run(self):
        while True:
            if global_list.GLOBAL_start_flag == True:
                if global_list.GLOBAL_SERIAL_serial_handle != None:
                    if global_list.GLOBAL_SERIAL_serial_handle.inWaiting() > 0:
                        global_list.STRGLO = global_list.GLOBAL_SERIAL_serial_handle.read(global_list.GLOBAL_SERIAL_serial_handle.inWaiting()).hex()
                        self.hex_len = int((len(global_list.STRGLO) + 1) / 2)
                        print('global_list.STRGLO:',global_list.STRGLO,' hex_len:',self.hex_len)
                        if self.hex_len <= len(self.hex_array):
                            for i in range(0,self.hex_len):
                                self.out_serial = self.out_serial + global_list.STRGLO[i * 2 :i * 2 + 2] + ' '
                            print_log("serial recv " + str(self.hex_len).zfill(2) + " -> " + self.out_serial + "\n")

                            for i in range(0,72):
                                if self.out_serial.find(global_list.GLOBAL_TEXT_ARRAY[i].text().lower()) != -1 and global_list.GLOBAL_TEXT_ARRAY[i].text() != '':
                                    serail_data_process(self, global_list.GLOBAL_TEXT_ARRAY[i + 1].text().lower())
                            self.out_serial = ''
            time.sleep(0.05)



class MainWindow(QtWidgets.QMainWindow, Ui_WinControl):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.worker=MyThread()
        self.worker.start()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


