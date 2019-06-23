import pygal
from die import Die

# 创建两个D6骰子
die1 = Die()
die2 = Die()

# 掷骰子
# results = []
# for roll_num in range(1000):
# 	result = die1.roll() + die2.roll()
# 	results.append(result)
results = [die1.roll() + die2.roll() for roll_num in range(1000)]

# 分析结果
# frequencies = []
max_result = die1.num_sides + die2.num_sides
# for value in range(1, max_result+1):
# 	frequency = results.count(value)
# 	frequencies.append(frequency)
frequencies = [results.count(value) for value in range(1, max_result+1)]

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Result of rolling two D6 1000 times"
hist.x_labels = [str(n) for n in range(2, 13)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')