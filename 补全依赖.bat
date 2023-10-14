@ECHO OFF
chcp 65001
title 补全依赖
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
pip install -r requirements.txt