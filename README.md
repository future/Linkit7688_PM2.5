# Linkit7688 PM2.5

----

![](https://lh3.googleusercontent.com/jRHinLgC4BNJ-yVddwrFx5nOCK5EXK63MtQLZeTJEL-oxW98mAiihmaivr0_o7TBAiu_4XTUv2P5zd2d4uNnB5Iobtx0HOuxQEk3vMzhgRlihKss3OPi22Bx0eVp-yJ-9VAOYsNWlioTDH_dSwImEu0w9Z2wwgTRnZ-pvi6G1dw8JDe0A3L60PB5C91nKiYUhcYvcXcZCNi9nXLipL7flICvuZ1rV6L_NFvMoH5bjkgnRHfM-MUYClCrRDLYJogUSjQzqxUwPuk6jthd8o08wKhEDhhQttHKWDKJTmmorh9lcjSQrlGDFH--aJZASvWAi0vx67Y1iB28rXh5x9saFZW16ZFy_ogOcVmIpgjy3eJHxDqI3cjRcQo5CM8gEyYhnxQ1jjSuxmSGo3bX09JXR-XnM-QzIjHF3TJ3oWbtM2A4RgtTBVYoR6v6lPA4u53VvkARIEci9GeqoMbUSfssNW6rMnez1GxrMDIaNmpP7iZlr8YL6dqbpDndX-ogKgsRjYCkPp72HnLXlaMjXTdtu0duFgAqPf1oCLhOkPSE441MpuvtTB35snOrTIUTMREpwQRqPA=w956-h574-no)

[範例照片](https://goo.gl/photos/au6QQ4f2c8oMzxvv5)




利用 Linkit 7688 量測 PM 1.0/2.5/10 空氣品質及溫濕度， 並在網頁即時顯示數據



# 硬體

|元件|說明|
|:---|:---|
|linkit 7688|處理器
|G3| 空氣品質偵測器|
|SHT2x|溫度、濕度偵測器(SHT20/21/2x皆可)|

# 預安裝

使用到 paho-mqtt package
須在 Linkit 7688 上安裝

> pip install paho-mqtt


# 安裝

1. 從git 上 clone 到 7688 裡，或是從電腦將程式目錄傳進 7688 中
2. 進入目錄後執行 python air.py

# 顯示

1. 將 web 目錄複製到 web server 目錄中，或是電腦中  
2. 用瀏覽器連接 web server 上的 air.html，或是在瀏覽器直接打開 air.html
3. 連接上mqtt broker 後 10 秒內，就會看到數據顯示
4. 每隔10秒會自動更新數據一次

# 範例

[即時數據網頁](http://iot.sparkfuture.io/static/air.html)
[影片](https://www.youtube.com/watch?v=wfXE5XBoCEo)  

