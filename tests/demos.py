import kaixin.kaixin as kaixin   # 在调用时import kaixin就好

if __name__ == '__main__':
    translation = kaixin.Translation()
    PrintColors = kaixin.PrintColors()
    PrintColors.Print(translation.translate('Hello!'), '93', 1)
    Time = kaixin.GetTime()
    print(Time.times())
    print(Time.get_MothDate(2023, 8))
    print(Time.get_time("%Y-%m-%d %H:%M:%S"))
    print(Time.day())
    print(Time.time())
    GetWeather = kaixin.GetWeather()
    print(GetWeather.get_weather())
    print(type(GetWeather.get_weather()))
    Record = kaixin.Record(3, '.\\Hello.wav')
    Record.record()
