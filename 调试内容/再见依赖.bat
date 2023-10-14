@ECHO OFF
chcp 65001
title 一键删除所有当前py库
pip freeze>modules.txt
pip uninstall -r modules.txt -y
