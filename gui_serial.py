import serial
import serial.tools.list_ports

import global_list
from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5 import QtWidgets ,QtCore
import gui


def read_serial_data(self):
    self.fname = "./system_info/info_serial.data"
    try:
        f = open(self.fname, "r")                                                     #以写入的方式打开文件
        data = f.read()
    except Exception:
        f = open(self.fname, "w+")
        f.close()
    else:
        if data:
            print("data:" + data)
            b = [i for i, j in enumerate(data) if j in ['<','>']]
            global_list.GLOBAL_SERIAL_COM_STR = data[b[0] + 1 : b[1]]
            global_list.GLOBAL_SERIAL_BAUD_STR = data[b[4] + 1 : b[5]]
            global_list.GLOBAL_SERIAL_BAUD_INDEX = int(data[b[6] + 1 : b[7]])
            global_list.GLOBAL_SERIAL_DATA_BIT = int(data[b[8] + 1 : b[9]])
            global_list.GLOBAL_SERIAL_STOP_BIT = int(data[b[10] + 1 : b[11]])
            global_list.GLOBAL_SERIAL_CHECK = int(data[b[12] + 1 : b[13]])
        f.close()

def write_serial_data(self):
    self.fname = "./system_info/info_serial.data"
    try:
        f = open(self.fname, "w")                                                     #以写入的方式打开文件
    except Exception:
        f = open(self.fname, "w+")
        f.close()
    else:
        data = "com_str<" + global_list.GLOBAL_SERIAL_COM_STR + ">\n" + \
               "com_index<" + str(global_list.GLOBAL_SERIAL_COM_INDEX) + ">\n" + \
                "baud_str<" + global_list.GLOBAL_SERIAL_BAUD_STR + ">\n" + \
                "baud_index<" + str(global_list.GLOBAL_SERIAL_BAUD_INDEX) + ">\n" + \
                "data_bit<" + str(global_list.GLOBAL_SERIAL_DATA_BIT) + ">\n" + \
                "stop_bit<" + str(global_list.GLOBAL_SERIAL_STOP_BIT) + ">\n" + \
                "check<" + str(global_list.GLOBAL_SERIAL_CHECK) + ">\n"
        f.write(data)
        f.close()



def read_list_data(self):
    self.fname = "./system_info/info_list.data"
    try:
        f = open(self.fname, "r")                                                     #以写入的方式打开文件
        data = f.read()
    except Exception:
        f = open(self.fname, "w+")
        f.close()
    else:
        if data:
            for i in range(0, 72):
                global_list.GLOBAL_TEXT_ARRAY[i].setText(data.split('list' + str(i).zfill(2) + '<')[1].split('>')[0])
        f.close()

def write_list_data(self):
    self.fname = "./system_info/info_list.data"
    try:
        f = open(self.fname, "w")                                                     #以写入的方式打开文件
    except Exception:
        f = open(self.fname, "w+")
        f.close()
    else:
        data = ''
        for i in range(0,72):
            data += 'list' + str(i).zfill(2) + '<' + global_list.GLOBAL_TEXT_ARRAY[i].text() + '>\n'
        f.write(data)
        f.close()



# 创建一个类
class gui_serial_class(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.initUI()


    def initUI(self):

        self.setObjectName("WinControl")
        self.resize(480,240)
        self.center()
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")


#串口信息表单设置
        self.tab_serial = QtWidgets.QWidget()
        self.tab_serial.setObjectName("tab_serial")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_serial)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_serial)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName("formLayout")

        #串口端口控件
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.cmbPortNum = QtWidgets.QComboBox(self.groupBox_2)
        self.cmbPortNum.setMinimumSize(QtCore.QSize(0, 0))
        self.cmbPortNum.setObjectName("cmbPortNum")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cmbPortNum)
        #刷新一下串口的列表
        self.refresh()
        self.cmbPortNum.setCurrentIndex(global_list.GLOBAL_SERIAL_COM_INDEX)

        #波特率控件
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.cmbBaudRate = QtWidgets.QComboBox(self.groupBox_2)
        self.cmbBaudRate.setObjectName("cmbBaudRate")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cmbBaudRate)
        self.cmbBaudRate.addItem('115200')
        self.cmbBaudRate.addItem('57600')
        self.cmbBaudRate.addItem('56000')
        self.cmbBaudRate.addItem('38400')
        self.cmbBaudRate.addItem('19200')
        self.cmbBaudRate.addItem('14400')
        self.cmbBaudRate.addItem('9600')
        self.cmbBaudRate.addItem('4800')
        self.cmbBaudRate.addItem('2400')
        self.cmbBaudRate.addItem('1200')
        self.cmbBaudRate.setCurrentIndex(global_list.GLOBAL_SERIAL_BAUD_INDEX)

        #数据位控件
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.cmbDataLen = QtWidgets.QComboBox(self.groupBox_2)
        self.cmbDataLen.setObjectName("cmbDataLen")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cmbDataLen)
        self.cmbDataLen.addItem('8')
        self.cmbDataLen.addItem('7')
        self.cmbDataLen.addItem('6')
        self.cmbDataLen.addItem('5')
        self.cmbDataLen.setCurrentIndex(global_list.GLOBAL_SERIAL_DATA_BIT)

        #停止位控件
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.cmbStopBit = QtWidgets.QComboBox(self.groupBox_2)
        self.cmbStopBit.setObjectName("cmbStopBit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cmbStopBit)
        self.cmbStopBit.addItem('1')
        self.cmbStopBit.addItem('1.5')
        self.cmbStopBit.addItem('2')
        self.cmbStopBit.setCurrentIndex(global_list.GLOBAL_SERIAL_STOP_BIT)

        #校验位控件
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.cmbCheckBit = QtWidgets.QComboBox(self.groupBox_2)
        self.cmbCheckBit.setObjectName("cmbCheckBit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cmbCheckBit)
        self.cmbCheckBit.addItem('NONE')
        self.cmbCheckBit.addItem('ODD')
        self.cmbCheckBit.addItem('EVEN')
        self.cmbCheckBit.setCurrentIndex(global_list.GLOBAL_SERIAL_CHECK)

        self.confirmButton = QtWidgets.QPushButton(self.groupBox_2)
        self.confirmButton.setObjectName("confirmButton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.confirmButton)
        self.confirmButton.clicked.connect(self.confirmButton_click)

        self.cancelButton = QtWidgets.QPushButton(self.groupBox_2)
        self.cancelButton.setObjectName("confirmButton")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.cancelButton)
        self.cancelButton.clicked.connect(self.cancelButton_click)
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)
#串口信息表单设置


        self.tabWidget.addTab(self.tab_serial, "")          #将串口信息表单添加到窗口中

        self.horizontalLayout.addWidget(self.tabWidget)     #两张表单处于平行位置
        self.tabWidget.setCurrentIndex(0)                   #选中一个表单
        self.setCentralWidget(self.centralwidget)           #居中显示

        self.retranslateUi(self)
        self.show()

    def retranslateUi(self, WinControl):
        _translate = QtCore.QCoreApplication.translate
        WinControl.setWindowTitle(_translate("WinControl", "串口及账号界面"))
        self.label.setText(_translate("WinControl", "串口号："))
        self.label_2.setText(_translate("WinControl", "波特率："))
        self.label_3.setText(_translate("WinControl", "数据位："))
        self.label_5.setText(_translate("WinControl", "停止位："))
        self.label_4.setText(_translate("WinControl", "校验位："))
        self.confirmButton.setText(_translate("WinControl", "确定"))
        self.cancelButton.setText(_translate("WinControl", "取消"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_serial), _translate("WinControl", "串口设置"))

    # 打开关闭串口
    def open_close(self):
        if global_list.GLOBAL_start_flag == True:
            try:
                global_list.GLOBAL_SERIAL_serial_handle = serial.Serial(global_list.GLOBAL_SERIAL_COM_STR, int(global_list.GLOBAL_SERIAL_BAUD_STR), timeout=0.1)
            except:
                QMessageBox.critical(self, ' ', '没有可用的串口或当前串口被占用')
                global_list.GLOBAL_start_flag = False
                return None
        else:
            try:
                 global_list.GLOBAL_start_flag = False
                 global_list.GLOBAL_SERIAL_serial_handle.close()
                 global_list.GLOBAL_SERIAL_serial_handle = None
            except:
                QMessageBox.critical(self, ' ', '关闭串口失败')
                global_list.GLOBAL_start_flag = False
                return None
        return "ok"


    # 刷新一下串口
    def refresh(self):
        # 查询可用的串口
        plist = list(serial.tools.list_ports.comports())
        if len(plist) <= 0:
            print("No used com!");
        else:
            self.cmbPortNum.clear()
            for i in range(0, len(plist)):
                plist_0 = list(plist[i])
                self.cmbPortNum.addItem(str(plist_0[0]))
                if str(plist_0[0]) == global_list.GLOBAL_SERIAL_COM_STR:
                    print(str(plist_0[0]),i)
                    global_list.GLOBAL_SERIAL_COM_INDEX = i


    def center(self):
        qr = self.frameGeometry()
        # 得到了主窗口大小
        cp = QDesktopWidget().availableGeometry().center()
        # 获取显示器的分辨率,然后得到中间点的位置
        qr.moveCenter(cp)
        # 然后把自己的窗口的中心点放到qr的中心点
        self.move(qr.topLeft())

    def confirmButton_click(self):
        global_list.GLOBAL_SERIAL_COM_STR = self.cmbPortNum.currentText()
        global_list.GLOBAL_SERIAL_BAUD_INDEX = self.cmbBaudRate.currentIndex()
        global_list.GLOBAL_SERIAL_BAUD_STR = self.cmbBaudRate.currentText()
        global_list.GLOBAL_SERIAL_DATA_BIT = self.cmbDataLen.currentIndex()
        global_list.GLOBAL_SERIAL_STOP_BIT = self.cmbStopBit.currentIndex()
        global_list.GLOBAL_SERIAL_CHECK = self.cmbCheckBit.currentIndex()
        write_serial_data(self)
        QMessageBox.about(self, ' ', '设置成功')

    def cancelButton_click(self):
        print("cancelButton_click")
        self.close()
