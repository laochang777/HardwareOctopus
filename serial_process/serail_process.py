import time
import re
import global_list
import gui
from global_fun import print_log

LIST_OUT_SITE = 0       #输出位置
LIST_LABLE_SITE = 1     #lable位置
LIST_SEND_SITE = 2      #发送函数位置
LIST_RECV_SITE = 3      #接收函数位置
LIST_VALID_SITE = 4      #是否参与测试位置
LIST_TIME_SITE = 5      #耗时位置
LIST_COUNT_SITE = 6     #重发次数位置
LIST_TIMEOUT_SITE = 7   #超时位置

def serail_check_data(self, data):
    check_data = 0
    if data[2] >= 37:
        return 0
    for i in range(2,data[2] - 1):
        check_data += data[i]

    check_data = (0x100 - check_data) & 0xff

    if data[0] == 0xff and \
       data[1] == 0x33 and \
       data[3] == 0x03 and \
       data[data[2] - 1] == check_data:
        return 0
    return 1

def serail_data_process(self,data):
    print('serail_data_process = ',data)
    if re.match("^[a-fA-F 0-9]+$", data):
        print("Successful match at the start of the string")
        if global_list.GLOBAL_SERIAL_serial_handle:
            result = global_list.GLOBAL_SERIAL_serial_handle.write(bytes.fromhex(data))
    else:
        print("Match attempt failed")