import json
import pygal
import math
"""对数变换剔除非线性趋势"""

# 创建5个列表，分别存储日期和收盘价
dates = []
months = []
weeks = []
weekdays = []
close = []

# 将数据加载到一个列表中
filename = 'btc_close_2017.json'
with open(filename) as f:
	btc_data = json.load(f)

for btc_dict in btc_data:
	dates.append(btc_dict['date'])
	months.append(int(btc_dict['month']))
	weeks.append(int(btc_dict['week']))
	weekdays.append(btc_dict['weekday'])
	close.append(int(float(btc_dict['close'])))

# x_label_ratation: x轴上的日期标签顺时针旋转20°
# show_minor_x_labels: 不用显示所有的x轴标签
# x_label_major: 让x坐标轴每个N天显示一次
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价对数变换（￥）'
line_chart.x_labels = dates
N = 20 # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('log收盘价', close_log)
line_chart.render_to_file('收盘价对数变换折线图（￥）.svg')