import pygal
from die import Die

# 创建两个D6骰子
die = Die()

# 掷骰子
# results = []
# for roll_num in range(1000):
# 	result = die.roll()
# 	results.append(result)
results = [die.roll() for roll_num in range(1000)]

# 分析结果
# frequencies = []
# for value in range(1, die.num_sides+1):
# 	frequency = results.count(value)
# 	frequencies.append(frequency)
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Result of rolling one D6 1000 times"
hist.x_labels = [str(n) for n in range(1, 7)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')