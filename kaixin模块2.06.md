2023.08.15 10:14# **kaixin模块2.06**

---

## **1. 下载*kaixin*模块**

* Windows
  在cmd中输入：```pip install kaixin```下载模块

> 其他平台使用对应pip命令即可

---

## **2. 使用*kaixin*模块**

### **1. 导入模块：**

在下载模块后，在代码开头添加

```python
import kaixin
```

也可以使用

```python
from kaixin import ???  # 如使用此代码，下面所有的kaixin.都不需要，并且只能访问填写的函数，*为所有函数
# 或使用
import kaixin as ??  # 如果使用此代码，下面所有kaixin.都替换成[??].([??]为as ??中的??)
```

> 将```???```替换为要单独导入的函数名，```??```替换成要自定义的名称

选用**其中一种方法**即可

---

### **2. 模块的所有可调用*类、函数*：**

* 所有可调用类:
  
  ```
  PrintColors, GetTime, Translation, GetWeather, Files, Joystick, Speech, PlaySound, Record
  ```

* 所有可调用函数：

```
check_process_running
```

---

### **3. 类说明：**

**1. ```GetTime```类**

**GetTime**类用于获取时间，初始化方法 ```变量名 = kaixin.GetTime```（实例化类）

所有**方法**：```get_MothDate(year, month), times(), get_time(time_id), day(), time()```

---

#### 方法说明:

* ```get_MothDate(year, month)```

函数用于**获取某年某月的日历**

函数需要两个参数```year, month```（两个参数的格式是```int```），其中```year```为某年，```month```为某月，函数会返回一个多行的```str```格式的值。

示例代码：

```python
import kaixin   # 导入kaixin模块

Time = kaixin.GetTime()  # 实例化类，并赋值给Time变量

print(Time.get_MothDate(2023, 8))   # 使用Time.get_MothDate()输出2023年8月的日历
```

cmd输出：

```
    August 2023
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31
```

---

* ```times()```

函数用于**获取日期和时间**

此函数**没有任何参数**，返回值为```str```格式。

示例代码：

```python
import kaixin   # 导入kaixin模块

Time = kaixin.GetTime()  # 实例化类，并赋值给Time变量

print(Time.times()) # 使用Time.times()输出当前日期与时间
```

cmd输出：

```
2023.08.15 10:14
```

---

* ```get_time(time_id)```

函数用于**获取time_id对应的当前时间**

```time_id```参数为```str```格式，```time_id```为时间代码(```%Y``` ```%m``` ```%d``` ```%H``` ```%M``` ```%S```)

> ```%Y```是年 ```%m```是月 ```%d```是天 ```%H```是时 ```%M```是分 ```%S```是秒，同```datetime.datetime.now().strftime('...')```

示例代码：

```python
import kaixin   # 导入kaixin模块

Time = kaixin.GetTime()  # 实例化类，并赋值给Time变量

print(Time.get_time("%Y %m %d %H: %M: %S")) # 使用Time.time()输出当前的"%Y %m %d %H: %M: %S"格式时间
```

cmd输出：

```
2023 08 15 10: 34: 51
```


