sys_db_stats = {4096: ['设备工作状态', 1, ''], 4098: ['室内风机状态', 1, ''], 4100: ['室外风机状态', 1, ''], 4102: ['压缩机状态', 1, ''], 4104: ['回风温度', 305, ''], 4110: [
    '冷凝器温度', 303, ''], 4114: ['内风机转速', 0, ''], 4116: ['外风机转速', 0, ''], 4120: ['直流输入电压', 542, ''], 4124: ['设备运行时间', 0, ''], 4128: ['压缩机运行时间', 0, ''], 4136: ['压缩机动作次数', '', '']}
sys_db_set = {0X07: ['通讯地址', ''], 0X08: ['通信速率', ''], 0X0A: ['设定温度', ''], 0X0C: ['设定回差', ''], 0X0E: ['高温警告点', ''], 0X10: [
    '低温警告点', ''], 0X12: ['直流过压警告', ''], 0X14: ['直流过压警告', ''], 0X1C: ['加热器启动温度', ''], 0X1E: ['加热器启动回差', '']}
sys_db_wrn = {0X300: ['高温告警', ''], 0X301: ['内风机故障告警', ''], 0X302: ['外风机告警', ''], 0X303: ['压缩机故障告警', ''], 0X304: ['内回风温度传感器告警', ''], 0X305: [
    '系统高压力告警', ''], 0X306: ['低温告警', ''], 0X307: ['直流过压告警', ''], 0X308: ['直流欠压告警', ''], 0X30C: ['蒸发器温度传感器故障', ''], 0X30D: ['冷凝器温度传感器故障', ''], 0X30E: ['环境温度传感器故障', ''], 0X30F: ['蒸发器冻结报警', '']}

test = {4096: 1, 4097: 65535, 4098: 2, 4099: 65535, 4100: 3, 4101: 65535, 4102: 1, 4103: 65535, 4104: 305, 4105: 65535, 4106: 65535, 4107: 65535, 4108: 32767, 4109: 65535, 4110: 303, 4111: 65535, 4112: 308, 4113: 65535, 4114: 0, 4115: 65535,
        4116: 0, 4117: 65535, 4118: 65526, 4119: 65535, 4120: 542, 4121: 65535, 4122: 65535, 4123: 65535, 4124: 0, 4125: 0, 4126: 65535, 4127: 65535, 4128: 0, 4129: 0, 4130: 65535, 4131: 65535, 4132: 0, 4133: 0, 4134: 65535, 4135: 65535}

test1 = [1, 65535, 2, 65535, 3, 65535, 1, 65535, 305, 65535, 65535, 65535, 32767, 65535, 303, 65535, 308, 65535, 0,
         65535, 0, 65535, 65526, 65535, 542, 65535, 65535, 65535, 0, 0, 65535, 65535, 0, 0, 65535, 65535, 0, 0, 65535, 65535]

# for i in test:
#     if i in sys_db:
#         sys_db[i][1] = test[i]


# for i in sys_db:
#     print(str(sys_db[i][0]) + ':' + str(sys_db[i][1]))

for i in test:
    if i in sys_db_stats:
        sys_db_stats[i][1] = test[i]


def data_pro():
    temper = [0X1008, 0X100E, 0X1010, 0X0A, 0X0C,
              0X0E, 0X10, 0X14, 0X1C, 0X1E]
    vote = [0X1018, 0X12, 0X14]
    mode = [0X1000, 0X1002, 0X1004, 0X1006]
    for i in sys_db_stats:
        if i in temper:
            tt = str(sys_db_stats[i][1]/10) + '℃'
            sys_db_stats[i][2] = tt
        if i in vote:
            tt = str(sys_db_stats[i][1]/10) + 'V'
            sys_db_stats[i][2] = tt
        if i in mode:
            if sys_db_stats[i][1] == 1:
                sys_db_stats[i][2] = '正常'
            elif sys_db_stats[i][1] == 2:
                sys_db_stats[i][2] = '运行'
            elif sys_db_stats[i][1] == 3:
                sys_db_stats[i][2] = '故障'

    return sys_db_stats

# # print(data_pro())
# import serial
# import modbus_tk
# import modbus_tk.defines as cst
# from modbus_tk import modbus_rtu


# master = modbus_rtu.RtuMaster(serial.Serial(
#             port='com5', baudrate=9600, bytesize=8, parity="N", stopbits=1))
# master.set_timeout(1)
# master.set_verbose(True)
# s = 7

# for i in test1:
#     master.execute(21,cst.WRITE_SINGLE_REGISTER,s,output_value=i)
#     print(i)
#     s+=1

i = 0x300
o = {}
while i <= 0x310 :
    h = hex(i)
    o[i] = h
    i +=1
print(o)
