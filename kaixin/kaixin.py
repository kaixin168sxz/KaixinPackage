# 导入模块

import datetime
import calendar
import requests
import json
import re
import urllib.request
import pickle
import pygame
import shutil
import os
import wave
from pyaudio import PyAudio, paInt16
from aip import AipSpeech
import playsound
import psutil

English_conversion = str.maketrans("abcdefghijklmnopqrstuvwxyz", "qwertyuiopasdfghjklmnbvczx")    # 加密密码
Digital_transformation = str.maketrans("0123456789", "2587413690")
English_Reverse_conversion = str.maketrans("qwertyuiopasdfghjklmnbvczx", "abcdefghijklmnopqrstuvwxyz")    # 解密密码
Digital_Reverse_conversion = str.maketrans("2587413690", "0123456789")
RECORDING, STOP = 'RECORDING', 'STOP'    # 定义两个状态，RECORDING是正在录音，STOP是停止录音
RecordType = STOP    # 定义一个记录状态的变量


# 定义获取时间类
class GetTime:
    """
    GetTime 时间类\n
    函数:\n
    get_MothDate(year, month)\n
    times()\n
    get_time(time_id)\n
    day()\n
    time()\n
    """
    def __init__(self):    # 定义一个self 类全局变量
        self.tq = datetime.datetime.now()

    @staticmethod    # 函数装饰器，在class类中可以不填self参数
    # 获取日历
    def get_MothDate(year, month):
        """
        获取year年 month月的日历
        :param year:
        :param month:
        :return:
        """
        return calendar.month(year, month)    # 返回year年、month月的日历

    # 获取日期和时间
    def times(self):
        """
        获取当前日期和时间
        :return:
        """
        return self.tq.strftime("%Y.%m.%d %H:%M")    # 返回日期和时间，使用self.tq 类全局变量

    # 自定义获取
    def get_time(self, time_id):
        """
        自定义获取\n
        time_id为时间代码(%Y%m%d%H%M)\n
        %Y是年 %m是月 %d是天 %H是时 %M是分
        :param time_id:
        :return:
        """
        return self.tq.strftime(time_id)    # 返回自定义获取得到的值，使用self.tq 类全局变量

    # 获取日期
    def day(self):
        """
        获取当前日期
        :return:
        """
        return self.tq.strftime("%Y.%m.%d")    # 返回日期，使用self.tq 类全局变量

    # 获取时间
    def time(self):
        """
        获取当前时间
        :return:
        """
        return self.tq.strftime("%H:%M")    # 返回时间，使用self.tq 类全局变量


# 定义翻译类
class Translation:
    """
    Translation 翻译类\n
    函数:\n
    translate(word)\n
    """
    @staticmethod    # 函数装饰器，在class类中可以不填self参数
    # 翻译函数（中英转换）
    def translate(word):    # word为要翻译的单词
        """
        翻译函数（中英转换）\n
        word为要翻译的单词
        :param word:
        :return:
        """
        url = 'http://fanyi.youdao.com/translate'    # 设置url网址
        data = {
            'i': word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': '16215739333345',
            'sign': '3e88e3f3e2f2bd3d1c9b9f10d1c0d7d2',
            'lts': '1621573933334',
            'bv': 'c87f7e0b8b617d7b4f4b2c7b2f1f0e31',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION',
        }    # 发送请求的内容

        response = requests.post(url, data=data)    # 发送请求，内容为data字典
        result = json.loads(response.text)    # 解析返回的 JSON 数据
        return result['translateResult'][0][0]['tgt']    # 返回结果


# 定义获取天气类
class GetWeather:
    """
    GetWeather 天气类\n
    函数:\n
    get_weather()
    """
    @staticmethod    # 函数装饰器，在class类中可以不填self参数
    # 获取天气函数（北京）
    def get_weather():
        """
        获取北京天气的函数
        :return:
        """
        try:
            urllib.request.urlopen("http://www.weather.com.cn/weather1d/101191102.shtml")    # 尝试执行：urllib.request.urlopen("http://www.weather.com.cn/weather1d/101191102.shtml")
        except urllib.error.URLError:    # 如果收到urllib.error.URLError错误执行
            return ['kaixin:URLError', 'kaixin:URLError', 'kaixin:URLError']    # 返回列表，值为：['kaixin:URLError', 'kaixin:URLError', 'kaixin:URLError']
        else:    # 如果没有异常
            res1 = urllib.request.urlopen("http://www.weather.com.cn/weather1d/101191102.shtml")    # 获取天气信息
            # 对信息进行处理
            date = res1.read().decode("utf8")    # utf-8解码
            pattern = re.compile(r'value="(.*?)" /')
            res2 = re.findall(pattern, date)
            res3 = str(res2[1]).split('  ')
            return res3    # 返回结果


# 定义文件操作类
class Files:
    """
    Files 文件操作类\n
    函数:\n
    save_file(file_content)\n
    read_file()\n
    NameCopyFile(new_path, file_name)\n
    CopyFile(new_path)\n
    save_wave_file(data)\n
    """
    def __init__(self, file_name):    # 定义self 类全局变量
        self.file_name = file_name

    # 保存文件
    def save_file(self, file_content):
        """
        保存.kx文件\n
        file_content为要保存的内容
        :param file_content:
        :return:
        """
        global English_conversion, Digital_transformation
        data = str(pickle.dumps(file_content))
        # 对序列化后的二进制数据进行字符串替换操作
        new_data_1 = data.translate(English_conversion)
        new_data_2 = new_data_1.translate(Digital_transformation)

        # 将替换后的二进制数据写入文件
        with open(self.file_name, 'w') as file_save:
            file_save.write(new_data_2)
            file_save.flush()

    # 读取文件
    def read_file(self):
        """
        读取.kx文件\n
        :return:
        """
        global Digital_Reverse_conversion, English_Reverse_conversion
        # 从文件中读取替换后的二进制数据
        with open(self.file_name, 'r') as file_read:
            r = (file_read.read())
        # 对读取的二进制数据进行字符串替换操作，恢复原始数据
        old_data_1 = r.translate(English_Reverse_conversion)
        old_data_2 = pickle.loads(eval(old_data_1.translate(Digital_Reverse_conversion)))
        return old_data_2

    # 复制文件并重命名
    def NameCopyFile(self, new_path, file_name):
        """
        复制任何文件并重命名\n
        new_path为要复制到的路径\n
        file_name为复制后新的文件名\n
        :param new_path:
        :param file_name:
        :return:
        """
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        new_file = os.path.join(new_path, file_name)
        shutil.copy(self.file_name, new_file)    # 复制文件，原文件为self.file_name 类全局变量

    # 复制文件
    def CopyFile(self, new_path):
        """
        复制任何文件\n
        new_path为要复制到的路径\n
        :param new_path:
        :return:
        """
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        new_file = os.path.join(new_path)
        shutil.copy(self.file_name, new_file)    # 复制文件，原文件为self.file_name 类全局变量

    # 保存wav文件
    def save_wave_file(self, data):
        """
        保存wav文件\n
        data为wav文件的二进制数据\n
        :param data:
        :return:
        """
        wf = wave.open(self.file_name, 'wb')    # 保存到：self.file_name 类全局变量
        # 设置声音参数
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(16000)
        # 二进制转换
        wf.writeframes(b"".join(data))
        wf.close()    # 断开文件连接


# 定义手柄类
class Joystick:
    """
    Joystick 手柄类\n
    函数:\n
    GetNames()\n
    QuitJoystick()\n
    GetNumber()\n
    GetName()\n
    GetAxis(ButtonNumber)\n
    GetHat(HatNumber)\n
    GetButton(ButtonNumber)\n
    """
    # 连接序号为Number的手柄，并初始化Pygame，必须先执行此函数，才能运行其他函数（可多次使用，二此调用时，要先退出）
    def __init__(self, Number):
        pygame.init()    # 初始化Pygame
        self.clock = pygame.time.Clock()    # 定义Pygame时钟
        pygame.joystick.init()    # 初始化手柄
        self.joystick = pygame.joystick.Joystick(Number)    # 定义手柄对象，并实例化
        self.joystick.init()    # 初始化手柄对象

    @staticmethod    # 函数装饰器，在class类中可以不填self参数
    # 获取所有手柄名
    def GetNames():
        """
        获取所有手柄名
        :return:
        """
        names = []
        for i in range(pygame.joystick.get_count()):    # for循环手柄
            print(i)
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
            names.append(joystick.get_name())
        return names    # 返回手柄列表

    # 断开手柄连接并卸载Pygame
    def QuitJoystick(self):
        """
        退出手柄连接并卸载Pygame
        :return:
        """
        # 退出
        self.joystick.quit()
        pygame.quit()

    @staticmethod
    # 获取手柄数量
    def GetNumber():
        """
        获取手柄数量
        :return:
        """
        return pygame.joystick.get_count()

    # 获取已连接手柄名称
    def GetName(self):
        """
        获取已连接手柄名称
        :return:
        """
        return self.joystick.get_name()

    # 获取遥感、扳机的值（模拟值）
    def GetAxis(self, ButtonNumber):
        """
        ButtonNumber为摇杆序号\n
        获取遥感、扳机的值（模拟值）
        :param ButtonNumber:
        :return:
        """
        pygame.event.get()
        return '{:.3f}'.format(self.joystick.get_axis(ButtonNumber))

    # 获取按钮的值（数字值）
    def GetButton(self, ButtonNumber):
        """
        ButtonNumber为按钮序号\n
        获取按钮的值（数字值）
        :param ButtonNumber:
        :return:
        """
        pygame.event.get()
        return '{}'.format(self.joystick.get_button(ButtonNumber))

    # 获取十字键的值（列表，数字值）
    def GetHat(self, HatNumber):
        """
        HatNumber为十字键序号\n
        获取十字键的值（列表，数字值）
        """
        return '{:.3f}'.format(self.joystick.get_hat(HatNumber))


# 定义语音类
class Speech:
    """
    Speech 语音识别类\n
    函数:\n
    Print()
    """
    def __init__(self, Path, APPID, KEY, SECRET):
        self.Path = Path
        self.client = AipSpeech(APPID, KEY, SECRET)

    def Print(self):
        """
        开始识别语音
        :return:
        """
        with open(self.Path, 'rb') as f:
            audio_data = f.read()
        result = self.client.asr(audio_data,
                                 'wav', 16000, {  # 采样频率16K
                                     'dev_pid': 1537,
                                     # 1536 普通话
                                     # 1537 普通话（纯中文识别）
                                     # 1737 英语
                                     # 1637 粤语
                                     # 1837 四川话
                                 })
        val = 'result' in result.keys()
        if val:
            result_text = result["result"][0]
        else:
            result_text = None
        return result_text


# 定义声音类
class PlaySound:
    """
    PlaySound 播放声音类
    """
    def __init__(self, Music, playing=False, loops=False):
        self.Path = Music
        self.Sound = loops
        self.PlayIng = playing

    # 播放
    def Play(self):
        """
        播放
        :return:
        """
        if not self.PlayIng:
            pygame.init()
            if self.Sound:    # 无限循环
                pygame.mixer.music.load(self.Path)    # 加载音频
                pygame.mixer.music.play(loops=-1, start=0.0)   # 播放
            else:
                pygame.mixer.Sound(self.Path).play()    # 播放
        else:
            playsound.playsound(self.Path)    # 播放（线程堵塞）

    # 停止（无限循环播放专用）
    def Stop(self):
        """
        停止（无限循环播放专用）
        :return:
        """
        if not self.PlayIng:
            pygame.init()
            if self.Sound:
                pygame.mixer.music.stop()    # 停止
                pygame.mixer.music.unload()    # 取消加载
                pygame.quit()    # 卸载Pygame

    # 暂停（无限循环播放专用）
    def Pause(self):
        """
        暂停（无限循环播放专用）
        :return:
        """
        if not self.PlayIng:
            pygame.init()
            if self.Sound:
                pygame.mixer.music.pause()

    # 继续（无限循环播放专用）
    def UnPause(self):
        """
        继续（无限循环播放专用）
        :return:
        """
        if not self.PlayIng:
            pygame.init()
            if self.Sound:
                pygame.mixer.music.unpause()


# 定义录音类
class Record:
    """
    Record 录音类\n
    函数:\n
    record()
    """
    def __init__(self, time, path):    # 定义self 类全局变量
        self.time = time    # 时间
        self.path = path    # 保存路径
        self.NUM_SAMPLES = 2000

    # 录音
    def record(self):
        """
        开始录音
        :return:
        """
        global RecordType
        pa = PyAudio()
        stream = pa.open(format=paInt16,
                         channels=1,
                         rate=16000,
                         input=True,
                         frames_per_buffer=self.NUM_SAMPLES)    # 初始化
        audioBuffer = []    # 录音数据
        count = 0
        RecordType = RECORDING    # 将录音状态设为录音中
        while count < self.time * 10:    # 开始录音
            string_audio_data = stream.read(self.NUM_SAMPLES)
            audioBuffer.append(string_audio_data)
            count += 1
        Files(self.path).save_wave_file(audioBuffer)  # 保存wav
        stream.close()    # 断开连接
        RecordType = STOP    # 将录音状态设为停止


# 定义彩色输出类
class PrintColors:
    """
    PrintColors 彩色输出类\n
    函数:\n
    Print(text, color='38', bold=0)
    """
    # 定义颜色常量
    HEA_DER = '95'
    OK_BLUE = '94'
    OK_GREEN = '92'
    WARNING = '93'
    FAIL = '91'
    NONE = '0'
    BOLD = '1'
    UNDERLINE = '4m'
    # 定义颜色列表
    ColorsList = [HEA_DER, OK_BLUE, OK_GREEN, WARNING, UNDERLINE, BOLD, NONE, FAIL]

    # 输出颜色为color参数的内容text参数，bold为粗体
    def Print(self, text, color='38', bold=0):
        """
        输出颜色为color参数的内容text参数，bold为粗体\n
        :param text:
        :param color:
        :param bold:
        :return:
        """
        if color in self.ColorsList:    # 颜色是否为颜色常量（是否在颜色列表中）
            print(f"\033[{color};{str(bold)}m{text}\033[{self.NONE}m")    # 输出
        else:
            print(f"\033[{color};{str(bold)}m{text}\033[{self.NONE}m")    # 输出


# 检测参数process_name是否正在运行
def check_process_running(process_name):
    """
    检测参数process_name是否正在运行
    :param process_name:
    :return:
    """
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True    # 正在运行返回True
    return False    # 正在运行返回False


# 测试程序
if __name__ == '__main__':
    PrintColors().Print('aa', '93', 1)
