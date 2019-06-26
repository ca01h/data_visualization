import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中获取日期、最高气温、最低气温
# filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv' # 有部分数据缺失，需要特殊处理
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# for index, column_header in enumerate(header_row):
	# 	print(index, column_header)

	highs, dates, lows = [], [], []
	# 如果有部分数据缺失，需要抛出异常
	for row in reader:
		try:
			current_date = datetime.strptime(row[0], "%Y-%m-%d")
			high = int(row[1])
			low = int(row[3])
		except ValueError as e:
			print(current_date, 'missing date')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(8, 5))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图像格式
plt.title("Daily high temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()