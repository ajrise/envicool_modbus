import serial
import time
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

"""定义地址"""
sys_db_stats = {4096: ['设备工作状态', 1, ''], 4098: ['室内风机状态', 1, ''], 4100: ['室外风机状态', 1, ''], 4102: ['压缩机状态', 1, ''], 4104: ['回风温度', 305, ''], 4110: ['冷凝器温度', 303, ''], 4114: ['内风机转速', 0, ''], 4116: ['外风机转速', 0, ''], 4120: ['直流输入电压', 542, ''], 4124: ['设备运行时间', 0, ''], 4128: ['压缩机运行时间', 0, ''], 4136: ['压缩机动作次数', '', ''], 7: ['通讯地址', '', ''], 8: ['通信速率', '', ''], 10: ['设定温度', '', ''], 12: ['设定回差', '', ''], 14: ['高温警告点', '', ''], 16: [
    '低温警告点', '', ''], 18: ['直流过压警告', '', ''], 20: ['直流过压警告', '', ''], 28: ['加热器启动温度', '', ''], 30: ['加热器启动回差', '', ''], 768: ['高温告警', '', ''], 769: ['内风机故障告警', '', ''], 770: ['外风机告警', '', ''], 771: ['压缩机故障告警', '', ''], 772: ['内回风温度传感器告警', '', ''], 773: ['系统高压力告警', '', ''], 774: ['低温告警', '', ''], 775: ['直流过压告警', '', ''], 776: ['直流欠压告警', '', ''], 780: ['蒸发器温度传感器故障', '', ''], 781: ['冷凝器温度传感器故障', '', ''], 782: ['环境温度传感器故障', '', ''], 783: ['蒸发器冻结报警', '', '']}


temper = [0X1008, 0X100E, 0X1010, 0X0A, 0X0C,
          0X0E, 0X10, 0X14, 0X1C, 0X1E]
vote = [0X1018, 0X12, 0X14]
mode = [0X1000, 0X1002, 0X1004, 0X1006]


def mod(start, num, PORT='com5'):
    red = []
    read = {}
    alarm = ""
    try:
        # 设定串口为从站
        master = modbus_rtu.RtuMaster(serial.Serial(
            port=PORT, baudrate=9600, bytesize=8, parity="N", stopbits=1))
        master.set_timeout(1)
        master.set_verbose(True)

        # 读保持寄存器
        red = master.execute(21, cst.READ_HOLDING_REGISTERS,
                             start, num)  # 这里修改需要读取的功能代码
        alarm = 0
        # print(red)
        for i in red:
            read[start] = i
            start += 1
        return read, alarm
    except Exception as exc:
        alarm = (str(exc))


def data_pro():
    """处理取到数据的显示"""
    for i in sys_db_stats:
        if i in temper:
            tt = str(sys_db_stats[i][1]/10) + '℃'  # 温度数据
            sys_db_stats[i][2] = tt
        elif i in vote:
            tt = str(sys_db_stats[i][1]/10) + 'V'  # 电压数据
            sys_db_stats[i][2] = tt
        elif i in mode:
            if sys_db_stats[i][1] == 1:
                sys_db_stats[i][2] = '待机'
            elif sys_db_stats[i][1] == 2:
                sys_db_stats[i][2] = '运行'
            elif sys_db_stats[i][1] == 3:
                sys_db_stats[i][2] = '故障'
        elif i >= 768 and i <= 784:
            if sys_db_stats[i][1] == 0:
                sys_db_stats[i][2] = '正常'
            elif sys_db_stats[i][1] == 1:
                sys_db_stats[i][2] = '告警'
        else:
            sys_db_stats[i][2] = sys_db_stats[i][1]
    return sys_db_stats


def rtu_date_read():
    """从设备读取数据并更新数据库"""
    secqus = [1, 2, 3]
    for i in secqus:
        if i == 1:
            db_stats = mod(0x1000, 41)[0]  # 读状态数据
        elif i == 2:
            db_stats = mod(0x07, 24)[0]  # 读取设置数据
        elif i == 3:
            db_stats = mod(0x300, 16)[0]  # 读取告警状态
        for i in db_stats:
            if i in sys_db_stats:
                sys_db_stats[i][1] = db_stats[i]
    data_pro()


rtu_date_read()
print(sys_db_stats)
