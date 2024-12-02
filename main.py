import requests
import tkinter as tk


# 定义获取IP地理位置的函数
def get_location():
    try:
        response3 = requests.get('https://restapi.amap.com/v3/ip?key=4c8df2adf7141bded7d2c078e77c3473')
        response3.raise_for_status()  # 如果请求返回了不成功的状态码，这里会抛出HTTPError异常
        data3 = response3.json()
        if data3['status'] == '1':
            location = data3['province'] + data3['city']
            adcode = data3['adcode']
        else:
            location = "错误，无法获得api数据"
            adcode = '130800'
    except requests.exceptions.RequestException as e:
        print(f"请求IP地理位置API时发生错误: {e}")
        location = "错误，无法获得api数据"
        adcode = '130800'
    return location, adcode


# 获取位置信息和行政编码
location, adcode = get_location()


# 定义获取实时天气的函数
def get_real_time_weather(adcode):
    try:
        url1 = 'https://restapi.amap.com/v3/weather/weatherInfo?city=' + adcode + '&key=4c8df2adf7141bded7d2c078e77c3473&extensions=base'
        response = requests.get(url1)
        response.raise_for_status()
        data = response.json()
        if data['status'] == '1':
            weather1 = '气温:' + data['lives'][0]['temperature'] + '℃  ' + '风向:' + data['lives'][0][
                'winddirection'] + '  风力:' + data['lives'][0]['windpower'] + '级  ' + '空气湿度:' + data['lives'][0][
                           'humidity']
            weather11 = '更新时间:' + data['lives'][0]['reporttime']
        else:
            weather1 = "错误，无法获得api数据"
            weather11 = "错误，无法获得api数据"
    except requests.exceptions.RequestException as e:
        print(f"请求实时天气API时发生错误: {e}")
        weather1 = "错误，无法获得api数据"
        weather11 = "错误，无法获得api数据"
    return weather1, weather11


# 获取实时天气
weather1, weather11 = get_real_time_weather(adcode)


# 定义获取天气预报的函数
def get_weather_forecast(adcode):
    try:
        url2 = 'https://restapi.amap.com/v3/weather/weatherInfo?city=' + adcode + '&key=4c8df2adf7141bded7d2c078e77c3473&extensions=all'
        response2 = requests.get(url2)
        response2.raise_for_status()
        data2 = response2.json()
        if data2['status'] == '1':
            weather2 = ''
            for item in data2['forecasts'][0]['casts']:
                weather2 += '日期:' + item['date'] + ' 星期:' + item['week'] + '\n白天:' + item['dayweather'] + ' 温度:' + item[
                    'daytemp'] + '℃' + ' 风向:' + item['daywind'] + ' 风力:' + item['daypower'] + '级' + '\n夜间:' + item[
                                'nightweather'] + ' 温度:' + item['nighttemp'] + '℃' + ' 风向:' + item[
                                'nightwind'] + ' 风力:' + item['nightpower'] + '级' + '\n\n'
            weather22 = '更新时间' + data2['forecasts'][0]['reporttime']
        else:
            weather2 = "错误，无法获得api数据"
            weather22 = "错误，无法获得api数据"
    except requests.exceptions.RequestException as e:
        print(f"请求天气预报API时发生错误: {e}")
        weather2 = "错误，无法获得api数据"
        weather22 = "错误，无法获得api数据"
    return weather2, weather22


# 获取天气预报
weather2, weather22 = get_weather_forecast(adcode)

window = tk.Tk()
window.title('日天天气报')
window.geometry('700x1100')
l1 = tk.Label(window,
              text='您所在地区为:',  # 标签的文字
              bg='#DDDDDD',  # 标签背景颜色
              font=('仿宋', 18),  # 字体和字体大小
              width=100, height=2  # 标签长宽（以字符长度计算）
              )
l1.pack(pady=10)  # 固定窗口位置
l11 = tk.Label(window,
               text=location,  # 标签的文字
               fg='Blue',
               bg='#DDDDDD',  # 标签背景颜色
               font=('仿宋', 18),  # 字体和字体大小
               width=100, height=2  # 标签长宽（以字符长度计算）
               )
l11.pack(pady=10)  # 固定窗口位置
# 定义一个lable
l2 = tk.Label(window,
              text='当前天气:',  # 标签的文字
              bg='#DDDDDD',  # 标签背景颜色
              font=('仿宋', 18),  # 字体和字体大小
              width=100, height=2  # 标签长宽（以字符长度计算）
              )
l2.pack(pady=10)  # 固定窗口位置
l22 = tk.Label(window,
               fg='red',
               text=weather1,  # 标签的文字
               bg='#DDDDDD',  # 标签背景颜色
               font=('仿宋', 18),  # 字体和字体大小
               width=100, height=2  # 标签长宽（以字符长度计算）
               )
l22.pack(pady=0)  # 固定窗口位置
l22 = tk.Label(window,
               text=weather11,  # 标签的文字
               bg='#DDDDDD',  # 标签背景颜色
               font=('仿宋', 18),  # 字体和字体大小
               width=100, height=3  # 标签长宽（以字符长度计算）
               )
l22.pack(pady=0)  # 固定窗口位置
l3 = tk.Label(window,
              text='预报:',  # 标签的文字
              bg='#DDDDDD',  # 标签背景颜色
              font=('仿宋', 18),  # 字体和字体大小
              width=100, height=2  # 标签长宽（以字符长度计算）
              )
l3.pack(pady=10)  # 固定窗口位置
l33 = tk.Label(window,
               text=weather2,  # 标签的文字
               fg='DarkGoldenRod',
               bg='#DDDDDD',  # 标签背景颜色
               font=('仿宋', 18),  # 字体和字体大小
               width=100, height=18  # 标签长宽（以字符长度计算）
               )
l33.pack(pady=0)  # 固定窗口位置
l22 = tk.Label(window,
               text=weather22,  # 标签的文字
               bg='#DDDDDD',  # 标签背景颜色
               font=('仿宋', 18),  # 字体和字体大小
               width=100, height=3  # 标签长宽（以字符长度计算）
               )
l22.pack(pady=0)  # 固定窗口位置

window.mainloop()
