# Linkit7688 PM2.5

----

![](https://photos.google.com/share/AF1QipOdNxFdgJxoIQfrlDCm36iawRvFZQl2u-WpoVXe0YuBvoyH2v3VSfMspybUm-ww3g/photo/AF1QipPzVmsW-COx_3f0POcq2Sp3tcjkdMRbC0YxD0sM?key=TVd5eGxnc01DSE5LWENNSmtnbUNzTXd6ck9tZkFR)

![](https://photos.google.com/share/AF1QipOdNxFdgJxoIQfrlDCm36iawRvFZQl2u-WpoVXe0YuBvoyH2v3VSfMspybUm-ww3g/photo/AF1QipME8E03x6xfOMuza3crk1nXeOMhDeUGHpMoqysN?key=TVd5eGxnc01DSE5LWENNSmtnbUNzTXd6ck9tZkFR)




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

[即時數據網頁](iot.sparkfuture.io/static/air.html)
[影片](https://www.youtube.com/watch?v=wfXE5XBoCEo)  

