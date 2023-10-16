@ECHO OFF
chcp 65001
title 补全依赖
conda config --add channels http://mirrors.aliyun.com/anaconda/pkgs/main
conda config --add channels http://mirrors.aliyun.com/anaconda/pkgs/r
conda config --add channels http://mirrors.aliyun.com/anaconda/pkgs/msys2
conda config --set show_channel_urls yes
conda install libpython m2w64-toolchain -c msys2 -y
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
pip install -r requirements.txt