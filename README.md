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

##### 其他要点内容  
1. 可变参数与关键字参数  
**可变参数**：
我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……  
要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：
```python
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```
但是调用的时候，需要先组装出一个list或tuple：
```python
>>> calc([1, 2, 3])
14
>>> calc((1, 3, 5, 7))
84
```
如果利用可变参数，调用函数的方式可以简化成这样：
```python
>>> calc(1, 2, 3)
14
>>> calc(1, 3, 5, 7)
84
```
所以，我们把函数的参数改为可变参数：
```python
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```
定义可变参数和定义list或tuple参数相比，仅仅在参数前面加了一个\*号。在函数内部，参数`numbers`接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
```python
>>> calc(1, 2)
5
>>> calc()
0
```
如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
```python
>>> nums = [1, 2, 3]
>>> calc(nums[0], nums[1], nums[2])
14
```
这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
```python
>>> nums = [1, 2, 3]
>>> calc(*nums)
14
```
这种写法相当有用，而且很常见。  
**关键字参数**  
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：
```python
def person(name, age, **kw):
    print ('name:', name, 'age:', age, 'other:', kw)
```
函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：
```python
>>> person('Michael', 30)
name: Michael age: 30 other: {}
```
也可以传入任意个数的关键字参数：
```python
>>> person('Bob', 35, city='Beijing')
name: Bob age: 35 other: {'city': 'Beijing'}
>>> person('Adam', 45, gender='M', job='Engineer')
name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
```
关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。  
和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
```python
>>> kw = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, city=kw['city'], job=kw['job'])
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```
当然，上面复杂的调用可以用简化的写法：
```python
>>> kw = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, **kw)
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```
**参数组合**  
在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。
比如定义一个函数，包含上述4种参数：
```python
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
```
对于任意函数，都可以通过类似`func(*args, **kw)`的形式调用它，无论它的参数是如何定义的。  
**默认参数一定要用不可变对象，如果是可变对象，运行会有逻辑错误！**
