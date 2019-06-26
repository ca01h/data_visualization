##### 安装`matplotlib`
1. [下载](https://pypi.python.org/pypi/matplotlib/)`matplotlib`安装程序，并查找使用的Python版本匹配的wheel文件。
2. 将.whl文件复制到项目文件夹。
3. `cmd`运行命令：`python -m pip install matplotlib-xxxxx.whl`

##### 安装`Pygal`
`cmd`运行命令：`python -m pip install pygal==1.7`

##### 重点函数
- `plt.plot()`：接收一个列表作为参数，这个函数根据这些数字绘制出有意义的图像。
- `plt.show()`：打开matplotlib查看器，并显示绘制的图形。
- `plt.title()`：设置图标标题，参数fontsize可选。
- `plt.xlable()` `plt.ylabel()`：给坐标轴加上标签，参数fontsize可选。
- `plt.pick_params`：设置刻度标记的样式，其中`axis='both'`将影响x轴和y轴上的刻度，labelsize设置刻度标记的字号。
- `plt.scatter(x_values, y_values, c=point_number, cmap=plt.cm.Blues, s=15)`：第一个和第二个参数指定`x`和`y`坐标，或分别存储`x`和`y`坐标的两个列表，第三个参数`c`指定各点的绘制先后顺序，第四个参数`cmap`指定使用颜色Blues，它将在指定位置绘制一个点或多个点。
- `plt.axis([0, 1100, 0, 1100000])`: 设置每个坐标轴的取值范围。
- `plt.savefig('squares_plot.png', bbox_right='tight')`：第一个参数指定文件名，第二个参数将图表多余的空白区域裁剪掉。
- `plt.axes().get_xaxis().set_visible()` `plt.axes().get_yaxis().set_visible()`：隐藏坐标轴
- `hist = pygal.Bar()`：为创建条形图，创建`Bar()`实例。
- `hist.title` `hist.x_labels` `hist.y_labels` `hist.x_title` `hist.y_title`：同上。
- `hist.add('D6', frequencies)`：使用`add()`将一系列值添加到图表中，第一参数给添加的值指定的标签，第二个参数是一个列表，其中包含将出现在图表中的值。
- `hist.render_to_file()`：将图标渲染为一个SVG文件。
