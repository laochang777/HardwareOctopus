GLOBAL_SERIAL_COM_STR = "COM1"  #串口号字符串
GLOBAL_SERIAL_COM_INDEX = 0      #串口号索引号
GLOBAL_SERIAL_BAUD_STR = 0       #波特率
GLOBAL_SERIAL_BAUD_INDEX = 0     #波特率
GLOBAL_SERIAL_DATA_BIT = 0       #数据位
GLOBAL_SERIAL_STOP_BIT = 0       #停止位
GLOBAL_SERIAL_CHECK = 0          #校验位

GLOBAL_PARA_LOCK_MODEL = ''
GLOBAL_PARA_ADC_UPPER = ''
GLOBAL_PARA_ADC_FLOOR = ''
GLOBAL_PARA_ELE_UPPER = ''
GLOBAL_PARA_ELE_FLOOR = ''
GLOBAL_PARA_NFCRC_UPPER = 0
GLOBAL_PARA_NFCRC_FLOOR = 0
GLOBAL_PARA_RSSI_UPPER = ''
GLOBAL_PARA_RSSI_FLOOR = ''
GLOBAL_PARA_VERSION = ''
GLOBAL_PARA_LOCKNAME = ''

GLOBAL_ACCOUT_IPADDR = "api2.intel-space.com:8844"
GLOBAL_ACCOUT_APPKEY = "307823166"
GLOBAL_ACCOUT_APPSECRET = "tqeJNEl4rz7fKUIPqxF4yefShTC568r3"
GLOBAL_ACCOUT_USERPHONE = "17888888889"
GLOBAL_ACCOUT_USERPASSWORD = "e10adc3949ba59abbe057f20f883e"
GLOBAL_ACCOUT_SIGN = "BD99FD05A372A599A4A29E91C0F006B2B268B6E7"

GLOBAL_process = 0


lcd_sum = None
lcd_pass = None
lcd_faild = None

GLOBAL_pass = 0
GLOBAL_faild = 0

GLOBAL_factoryToken = None
GLOBAL_lockId = None
GLOBAL_chiperID = None
GLOBAL_isBusiness = '0'
GLOBAL_cipherid_int = [0] * 256
GLOBAL_Factory = None
GLOBAL_decnum = 0

GLOBAL_label_signal = None
GLOBAL_SERIAL_serial_handle = None
STRGLO = 0
GLOBAL_list_number = 0
textLog = None
GLOBAL_textBar = None
GLOBAL_start_flag = False        #开始停止按键状态
GLOBAL_start_test = False        #开始停止按键状态

GLOBAL_link_list = None
GLOBAL_link_list_serial = None

GLOBAL_LABLE_ARRAY1_50 = None
GLOBAL_LABLE_ARRAY = [GLOBAL_LABLE_ARRAY1_50] * 100

GLOBAL_TEXT_ARRAY_50 = None
GLOBAL_TEXT_ARRAY = [GLOBAL_TEXT_ARRAY_50] * 100

GLOBAL_lblresult = None

GLOBAL_step_time = 0
GLOBAL_total_time = 0


cmd_test_USB_power       = 'FF 33 07 03 07 00'
cmd_test_init_power      = 'FF 33 07 03 07 01'
cmd_test_erase_eeprom    = 'FF 33 07 03 07 03'
cmd_test_motor_zheng     = 'FF 33 07 03 07 07'
cmd_test_motor_fan       = 'FF 33 07 03 07 08'
cmd_test_locked_in       = 'FF 33 07 03 07 09'
cmd_test_fangqiao        = 'FF 33 07 03 07 0A'
cmd_test_set_key         = 'FF 33 07 03 07 0B'
cmd_test_clear_key       = 'FF 33 07 03 07 0C'
cmd_test_oblique         = 'FF 33 07 03 07 0D'
cmd_test_nfc             = 'FF 33 07 03 07 0E'
cmd_test_voice           = 'FF 33 07 03 07 10'
cmd_test_backlight_led   = 'FF 33 07 03 07 11'
cmd_test_get_electric    = "FF 33 0B 03 07 15"
cmd_test_red_led         = 'FF 33 07 03 07 16'
cmd_test_get_ble_rssi    = 'FF 33 07 03 07 17'
cmd_test_get_ble_echo    = 'FF 33 07 03 07 18'
cmd_test_nfc_rc          = "FF 33 07 03 07 43"
cmd_test_get_version     = "FF 33 07 03 07 44"
cmd_test_start_self      = 'FF 33 07 03 07 45'
cmd_test_ble             = 'FF 33 07 03 07 3C'
cmd_test_eeprom          = 'FF 33 07 03 07 3E'
cmd_test_finger          = 'FF 33 07 03 07 3F'
cmd_test_flash           = 'FF 33 07 03 07 40'
cmd_test_adc             = 'FF 33 07 03 07 42'
cmd_write_result         = 'FF 33 07 03 08 80'

cmd_test_get_factory     = 'FF 33 13 03 09'
cmd_test_check_ble_init  = 'FF 33 06 03 0A'
cmd_test_get_lockname    = 'FF 33 07 03 0B FF'
cmd_test_get_ble_mac     = 'FF 33 06 03 04'
cmd_test_get_result      = 'FF 33 06 03 0C'
cmd_test_enter           = 'FF 33 06 03 00'
cmd_normal_enter         = 'FF 33 06 03 01'
