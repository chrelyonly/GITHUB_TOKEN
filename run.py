import requests
import sys
import time

if (len(sys.argv) >= 2):
    urls = sys.argv[1].split(',')
else:
    urls = ['https://www.antmoe.com/']
    print('你没有正确添加地址哦！默认GET作者博客呢！')
for i in range(0, len(urls)):
    req = requests.get(urls[i])
    print(f'第{i+1}号网址唤醒状态:', req, time.strftime(
        '%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
