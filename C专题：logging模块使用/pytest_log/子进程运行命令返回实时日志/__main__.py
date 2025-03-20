#!/bin/bash/python3
# _*_ coding: utf-8 _*_
import subprocess

p = subprocess.Popen(
    args="pytest -v ../testcase2.py",
    bufsize=1,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    universal_newlines=True,
    shell=True,
    encoding="utf-8"
)
count = 1
for line in iter(p.stdout.readline, b''):
    if count >= 5:
        break
    if line:
        print(line)
    else:
        count += 1
