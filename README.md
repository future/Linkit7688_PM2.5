# Linkit7688 PM2.5

----


![](https://lh3.googleusercontent.com/jNeAnuH9PihmFhcGknX2BAY9ZPpuTbKmEextvnl7Y6hmNM237HuixPncjGsIm5SkeYHdGzZIpkXy1Xba88NGRtTWnVloQv-Zn5QS-BcMMbdkXroonRK6H6j5PaQe_6i6vqZohHc7SUKm2jvkW6gTDJgQatPWRmgp6TpMpf6m711IgQsjKF9GEgD8O72oviuAvFGPNI32i5kGP-tWssoJJAu-cvjamcQ97wXXK31c_CzQ5KocdHRYgCIHLMNBUk3yA58i6ZWcHCKh_iLJKScmuFp_YiHNPBqeAE9HWv7NpfuGLkxOSEHxR5013bTIptgGm_TVP_VoJ8ols-0W7KXSx3DaF0xL3kJHBrzWqFQxb6rj6OY1q_XM0NlcpdiFdi5ZomHpw1S142676fWQIRs7azfs7ZNq1hJ1sbMYDTnzYFjPjp4XiHX28PBOB64hiwH_hMvJHAIWKFu7p9VeP13ovujTeXB7_1KdClAyfNvhiy-JGH1mL0EydwjzrF-dJfyvF7lLyw_gVKEMtz7IHS89AFzqb85HCYXee84i94CtvBsQGEZ98ropoFcCP_7k-IpMGk_F_A=w800-h486-no)



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

[影片](https://www.youtube.com/watch?v=wfXE5XBoCEo)  

