import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import getopt


file_path = None
data_shrink = 1
voltage_shrink = 0.5
csv_data = None
cha_data = None
chb_data = None

def parse_args():
    global file_path
    global data_shrink
    global voltage_shrink

    argv = sys.argv[1:]
 
    try:
        opts, args = getopt.getopt(argv, "f:m:n:")  # 短选项模式
     
    except:
        print("getopt Error")
 
    for opt, arg in opts:
        if opt in ['-f']:
            file_path = arg
        elif opt in ['-m']:
            data_shrink = int(arg)
        elif opt in ['-n']:
            voltage_shrink = float(arg)
            
## handle data with    data_shrink and    voltage_shrink
def process_data(origin_list , minus=False):
    new_list = []
    
    if minus:
        for i in range(len(origin_list)):
                origin_list[i] -= voltage_shrink
        
    if data_shrink == 1:
        new_list = origin_list
    else:
        data_sum = float(0)
        data_left =  data_shrink
        data_add = 0
        data_avg = float(0)
        
        data_cnt = len(origin_list)
        for i in range(data_cnt):
            data_sum += origin_list[i]
            data_left -= 1
            data_add += 1
            
            if ( data_left == 0) or (i == (data_cnt - 1)):
                data_avg = data_sum / data_add
                new_list.append(data_avg)
                data_sum = 0
                data_add = 0
                data_left = data_shrink
            
        
    return new_list
        
 
def prepare_data():
    global file_path
    global data_shrink
    global voltage_shrink
    
    
    global cha_data
    global chb_data
    
    global csv_data
    
    # csv_data = pd.read_csv(file_path  , nrows=100)
    csv_data = pd.read_csv(file_path )


    list_cha = csv_data['CHA']
    list_chb = csv_data['CHB']

    cha_data = process_data(list_cha)
    chb_data =  process_data(list_chb , True)




def show_plt():
    global cha_data
    global chb_data
    
    x_len = range(len(cha_data)) 

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
    
    plt.plot(x_len, cha_data, color='orangered', label='CHA')
    plt.plot(x_len, chb_data, color='blueviolet',  label='CHB')
    plt.legend()  # 显示图例

    plt.show()


parse_args()
prepare_data()
show_plt()

'''
x = data['TIME']
y = data['CH1']
 
fig = plt.figure()
 
# control the settings of graph, such as font、 fontsize , and etc
plt.rc('font',family='Times New Roman')
plt.rcParams['xtick.direction']='out'   # or 'in'
plt.rcParams['ytick.direction']='out'
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
 
plt.plot(x,y,linewidth = 1,label='ia')
 
plt.xlabel('Time (s)', fontsize=12)
plt.ylabel('ia (A)', fontsize=12)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.xlim(-0.5,0.5)
plt.ylim(-3,3)
plt.grid(True, linestyle='--')
plt.legend(loc='upper center', bbox_to_anchor=(0.15, 0.99),shadow=False)
 
# control the number of ticks
# plt.locator_params('x',nbins = 5)
# plt.locator_params('y',nbins = 7)
 
# reset the coordinate scale
plt.xticks([-0.5, -0.25, 0, 0.25, 0.5],
  ['0', '0.25', '0.5', '0.75', '1'])
 
## insert the subgraph
left, bottom, width, height = 0.65,0.6,0.2,0.2
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(x,y,'r')
# ax1.set_xlabel('Time (s)')
ax1.set_xlim(0,0.2)
ax1.set_ylim(-2.5,2.5)
# control the fontsize of ticks of subgraph
# ##https://github.com/matplotlib/matplotlib/issues/12318
for tick in ax1.xaxis.get_majorticklabels():  # example for xaxis
    tick.set_fontsize(12)
for tick in ax1.yaxis.get_majorticklabels():  # example for xaxis
    tick.set_fontsize(12)
 
ax1.grid(True, linestyle='--')
# ax1.locator_params(tight=True, nbins=2)
 
plt.show()
'''