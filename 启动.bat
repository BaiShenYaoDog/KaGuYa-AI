@ECHO OFF
chcp 65001
title 卡古娅AI
start 启动网页字幕打印机.bat
echo 如果不出意外,网页字幕打印机已经启动了.链接是:http://127.0.0.1:5500/index.html
start 启动语音处理.bat
echo 如果不出意外,语音处理已经启动了.链接是:http://127.0.0.1:7860
echo.
py main.py
pause