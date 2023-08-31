# **KaixinPackage1.0.1**

> **此模块仅使用Windows系统进行测试过，*其它平台报错或无效属于正常现象***, 如果在*其他平台*或在*Windows系统*上发现**程序报错**或发现***此说明书*的错误**，**请及时联系, 邮件地址:kaixin168KX@163.com**

[GitHub项目地址](https://github.com/kaixin168sxz/KaixinPackage)

---

## **1. 下载*kaixin*模块**

> 此模块仅支持版本>=python3.8的python
>
> 依赖包：```['datetime','calendar','requests','json','re','urllib','pickle','pygame','shutil','os','wave','pyaudio','aip','playsound','psutil']```

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

* **类*初始化*方法 ```变量名 = kaixin.类()```（*实例化*类）**

**1. ```GetTime```类**

> &#95;&#95;init&#95;&#95;()**没有任何要填的参数**

**GetTime**类用于获取时间

所有**方法**：```get_MothDate(year, month), times(), get_time(time_id), day(), time()```

---

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

---

* ```day()```

函数用于**获取当前日期**
此函数**没有任何参数**，会返回一个```str```格式的值

示例代码：

```python
import kaixin   # 导入kaixin模块

Time = kaixin.GetTime()  # 实例化类，并赋值给Time变量

print(Time.day())	# 使用Time.day()输出当前日期
```

cmd输出：

```
2023.08.15
```

---

* ```time()```

函数用于**获取当前时间**

此函数**没有任何参数**，会返回一个```str```格式的值

示例代码：

```python
import kaixin   # 导入kaixin模块

Time = kaixin.GetTime()  # 实例化类，并赋值给Time变量

print(Time.time())	# 使用Time.time()输出当前时间
```

cmd输出：

```
14:51
```

---

**2. ```Translation```类**

> &#95;&#95;init&#95;&#95;()**没有任何要填的参数**

**Translation**类是翻译类**（需联网）**，只有一个函数：```translate(word)```

---

* ```translate(word)```

函数用于**中英互译**，有一个参数```word```为要中英互译的字符串，为```str```格式，此函数返回值为```str```格式

示例代码：

```python
import kaixin   # 导入kaixin模块

Translation = kaixin.Translation()  # 实例化类，并赋值给Translation变量

print(Translation.translate('你好！'))	# 使用Translation.translate()将'你好！'翻译成英文并输出
```

cmd输出：

```
Hello!
```

---

**3. ```GetWeather```类**

> &#95;_init__()**没有任何要填的参数**

**GetWeather**类是获取天气类**（需联网）**，同```Translation```类，也只有一个函数：```get_weather()```

---

* ```get_weather()```

函数用于**获取*中国北京* 的天气**，此函数**没有任何参数**，返回值为```list```格式

示例代码：

```python
import kaixin   # 导入kaixin模块

GetWeather = kaixin.GetWeather()  # 实例化类，并赋值给GetWeather变量

weather = GetWeather.get_weather()  # 获取当前中国北京的天气，并赋值给变量weather

# 输出
print(weather)
print('\n------------------------------------\n')
print(weather[0])
print(weather[1])
print(weather[2])
```

cmd输出：

```
['08月15日08时 周二', '晴', '33/26°C']

------------------------------------

08月15日08时 周二
晴
33/26°C
```

> cmd输出列表的0值为当前中国北京的**时间**，1值为当前中国北京的**天气**，2值为当前中国北京的**温度**

---

**3. ```Files```类**

> &#95;_init__()**有一个要填的参数：```file_name```**
>
> ```file_name```为要操作文件的路径，```str```格式

**Files**类是用于操作文件的类

所有**方法**：```save_file(file_content), read_file(), NameCopyFile(new_path, file_name), CopyFile(new_path), save_wave_file(data)```

---

* ```save_file(file_content)```

函数用于**保存.kx格式的加密文件在```file_name```路径**，**不返回任何数据**，此函数**有一个参数**```file_content```是要保存的内容，```str```格式

> 如果```file_name```路径中的文件不存在，就新建文件

文件目录：

```
主文件夹
|_ File.kx
|_ main.py
```

示例代码：

```python
import kaixin   # 导入kaixin模块

Files = kaixin.Files('.\\File.kx')  # 实例化类，并赋值给Files变量

Files.save_file('Hello!')
```

File.kx**解密后的内容**:

* 原来:

  ```
  H
  ```
* 执行代码后：

  ```
  Hello!

  ```

如果没有找到```'.\\File.kx'```那就会自动在主文件夹下**新建**一个File.kx后再将内容设为```Hello!```

---

* ``` read_file()```

函数用于**读取.kx格式的加密文件在```file_name```路径**，此函数**没有任何参数**，返回```file_name```路径文件的解密后的内容，返回值为```str```格式

文件目录：

```
主文件夹
|_ File.kx
|_ main.py
```

File.kx**解密后的内容**:

```
What day is it today?
```

示例代码：

```python
import kaixin   # 导入kaixin模块

Files = kaixin.Files('.\\File.kx')  # 实例化类，并赋值给Files变量

print(Files.read_file())
```

cmd输出：

```
What day is it today?
```

---

* ```NameCopyFile(new_path, file_name)```

函数用于**复制```self.file_name```路径的文件到```new_path```路径的文件并将文件名设为```file_name```**。**有两个参数```new_path, file_name```**，```new_path```是要复制到的新路径，```file_name```是复制后的新文件名。

文件目录：

```
主文件夹
|_ 1文件夹
|  |_ a.txt
|_ 2文件夹
|_ main.py
```

示例代码：

```python
import kaixin   # 导入kaixin模块

Files = kaixin.Files('.\\1文件夹\\a.txt')  # 实例化类，并赋值给Files变量

Files.NameCopyFile('.\\2文件夹', 'aa.txt')	# 复制.\\1文件夹\\a.txt到.\\2文件夹，并将文件重命名为aa.txt
```

文件目录（运行程序后）：

```
主文件夹
|_ 1文件夹
|  |_ a.txt
|_ 2文件夹
|  |_ aa.txt
|_ main.py
```

---

* ```CopyFile(new_path)```

函数用于**复制```self.file_name```路径的文件到```new_path```路径的文件**，**有一个参数```new_path```**，```new_path```是要复制到的新路径。

文件目录：

```
主文件夹
|_ 1文件夹
|  |_ a.txt
|_ 2文件夹
|_ main.py
```

示例代码：

```python
import kaixin   # 导入kaixin模块

Files = kaixin.Files('.\\1文件夹\\a.txt')  # 实例化类，并赋值给Files变量

Files.CopyFile('.\\2文件夹')	# 复制.\\1文件夹\\a.txt到.\\2文件夹
```

文件目录（运行程序后）：

```
主文件夹
|_ 1文件夹
|  |_ a.txt
|_ 2文件夹
|  |_ a.txt
|_ main.py
```

---

* ```save_wave_file(data)```

**不建议使用**

说明：```save_wave_file(data)```可以将**二进制数据作为*wav格式文件*** 保存到```file_name```的路径文件下

> 二进制数据为```list```格式，如：```[b'\x00\x00\x00\...']```

---

**4 ```Joystick```类**

> &#95;_init__()**有一个要填的参数：```Number```**
>
> ```Number```为要连接的手柄序号，```int```格式

**Joystick**类是用于连接手柄

所有**方法**：```GetNames(), QuitJoystick(), GetNumber(), GetName(), GetAxis(ButtonNumber), GetHat(HatNumber), GetButton(ButtonNumber)```

---

* ```GetNames()```

获取**所有已连接手柄**的名称，**没有任何参数**，返回值为```list```格式

* ```QuitJoystick()```

**退出**手柄连接并**卸载```Pygame```**

* ```GetNumber()```

获取**手柄数量**，返回值为```int```格式

* GetName()

获取**当前连接手柄**的名称

---

* ```GetAxis(ButtonNumber)```是获取模拟值类型（遥感，扳机），```ButtonNumber```为要获取值的编号
* ```GetHat(HatNumber)```是获取十字键，```HatNumber```为十字键的编号（一般是0）
* ```GetButton(ButtonNumber)```是获取数字值（按钮），```ButtonNumber```为要获取值的编号

> 查看手柄按键编号可以使用```print(kaixin.GetButton(0))``` ```print(kaixin.GetButton(1))```...来慢慢测试或使用[此代码](https://pan.baidu.com/s/120GTmnLOWBtFZZTWuq8qBw?pwd=kx06 )（代码来自：[Pygame详解（十七）：joystick 模块_pygame joystick_来自江南的你的博客-CSDN博客](https://blog.csdn.net/qq_41556318/article/details/86305263)）

---

**5 ```Speech```类**

> &#95;_init__()**有三个要填的参数：```Path, APPID, KEY, SECRET```**
>
> ```Path```为要识别的wav格式文件，```str```格式
>
> ```APPID, KEY, SECRET```为[百度密钥](https://cloud.baidu.com/product/speech)参数

**Speech**类用于语音识别**（需联网）**，只有一个```Print()```函数

---

* ```Print()```

```Print()```为**开始语音识别**，可以搭配```Record```类实现录音并语音转文字，也可以识别提前录制好的音频，此函数**没有任何参数**，会返回**语音识别出的值**

> 音频文件要是**wav格式**

---

**6 `PlaySound`类**

> &#95;&#95;init&#95;&#95;()**有三个要填的参数：```Music, playing=False, loops=False```**
>
> ```Music```为音频的路径，```playing```为是否堵塞线程，```loops```为是否循环播放

**`PlaySound`类**用于播放音频，所有函数：```Play(), Stop(), Pause(), UnPause()```（***全部* 没有任何参数**）

---

* ```Play()``` 用于开始播放音频
* ```Stop()``` 停止**（无限循环播放专用）**
* ```Pause()``` 暂停**（无限循环播放专用）**
* ```UnPause()```继续**（无限循环播放专用）**

---

**7 `Record`类**

> &#95;&#95;init&#95;&#95;()**有两个要填的参数：```time, path```**
>
> ```time```为要录制的时间，```path```是保存录音的文件路径（没有会自动创建）

**Record**类用于录音，只有一个```record()```函数

---

* ```record()```

此函数**没有任何参数**，用于**开始录制音频**，**在录制```time```参数指定的时间后会*自动停止运行***

> 使用前请**检查电脑是否有麦克风或其他声音输入装置**

---

**8 `PrintColors`类**

> 此类**没有&#95;&#95;init&#95;&#95;()函数**

此类**用于在控制台输出彩色字符**，**在有些电脑上*可能会失效***。只有一个函数：```Print(text, color='38', bold=0)```

---

* ```Print(text, color='38', bold=0)```

函数**有三个参数：```text, color='38', bold=0```**，```text```参数为要输出的内容，```color```为要输出的颜色，```bold```为是否粗体（必须是```int```格式的```0```和```1```，不能是```True```或```False```）

类**有几个设定好的颜色**：```HEA_DER, OK_BLUE, OK_GREEN, WARNING, UNDERLINE, BOLD, NONE, FAIL```，**可以通过```kaixin.PrintColors().颜色```使用**

> **其他颜色可以去网上查询```python print 颜色编码```**

---

## **4. 函数说明：**

* ```check_process_running(process_name)```

> **仅适用于Windows**

函数用于**检测某个线程是否正在运行**，参数：```process_name```为要检测线程的名称，返回值为```True```或```False```

---

Copyright (c) 2023 SongXinZhe
