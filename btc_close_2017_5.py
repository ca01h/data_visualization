from itertools import groupby
import json
import pygal
import math

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

def draw_line(x_data, y_data, title, y_legend):
	xy_map = []
	"""
	1. zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
	2. groupby() 把迭代器中相邻的重复元素挑出来放在一起，实际上挑选规则是通过函数完成的，
	只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key
	"""
	for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
		y_list = [v for _, v in y]
		xy_map.append([x, sum(y_list) / len(y_list)])
	x_unique, y_mean = [*zip(*xy_map)]
	line_chart = pygal.Line()
	line_chart.title = title
	line_chart.xlabels = x_unique
	line_chart.add(y_legend, y_mean)
	line_chart.render_to_file(title+'.svg')
	return line_chart

idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], close[:idx_month], '收盘价月日均值（￥）', '月日均值')

idx_week = dates.index('2017-12-01')
line_chart_week = draw_line(weeks[:idx_week], close[:idx_week], '收盘价周日均值（￥）', '周日均值')
line_chart_week

wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_int =[wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekday_int, close[1:idx_week], '收盘价星期均值（￥）', '星期均值')
line_chart_weekday.xlabels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line_chart_weekday.render_to_file('收盘价星期均值（￥）.svg')
line_chart_weekday