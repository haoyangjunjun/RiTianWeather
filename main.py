import requests
import tkinter as tk

# 获取地址

response3 = requests.get(
    'https://restapi.amap.com/v3/ip?key=4c8df2adf7141bded7d2c078e77c3473')
data3 = response3.json()
if data3['status'] == '1':
    location = data3['province'] + data3['city']
    adcode = data3['adcode']
else:
    location = "错误，无法获得api数据"

# 实时天气
url1 = 'https://restapi.amap.com/v3/weather/weatherInfo?city=' + adcode + '&key=4c8df2adf7141bded7d2c078e77c3473&extensions=base'
response = requests.get(url1)
data = response.json()
if data['status'] == '1':
    weather1 = '气温:' + data['lives'][0]['temperature'] + '℃  ' + '风向:' + data['lives'][0]['winddirection'] + '  风力:'+data['lives'][0]['windpower'] + '级  ' + '空气湿度:' + data['lives'][0]['humidity']
    weather11 = '更新时间:' + data['lives'][0]['reporttime']
else:
    weather1 = "错误，无法获得api数据"

# 天气预报

url2 = 'https://restapi.amap.com/v3/weather/weatherInfo?city=' + adcode + '&key=4c8df2adf7141bded7d2c078e77c3473&extensions=all'
response2 = requests.get(url2)
data2 = response2.json()
if data2['status'] == '1':
    weather2=''
    for item in data2['forecasts'][0]['casts']:
        weather2=weather2+'日期:' + item['date']+' 星期:'+ item['week']+'\n白天:'+ item['dayweather']+' 温度:'+ item['daytemp']+'℃'+' 风向:'+ item['daywind']+' 风力:' + item['daypower']+ '级'+'\n夜间:'+item['nightweather']+' 温度:'+ item['nighttemp']+'℃'+' 风向:'+ item['nightwind']+' 风力:' + item['nightpower'] + '级'+'\n\n'
    weather22='更新时间', data2['forecasts'][0]['reporttime']
else:
    weather2="错误，无法获得api数据"


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


window.mainloop()
