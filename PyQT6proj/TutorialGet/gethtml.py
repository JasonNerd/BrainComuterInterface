"""
in_project:     TutorialGet
file_name:      gethtml.py
create_by:      mrrai
create_time:    2022/12/22 15:47
description:    获取网页并编号和重命名
"""
import requests
from bs4 import BeautifulSoup
import os

root_page = "https://learnopengl-cn.github.io/"   # 教程网址
root = "./resources/"                       # 结果目录根地址
path = "openGL/"                            # 教程对应知识点

def get_pages(url, fl_root):
    # 创建结果存放目录
    fl_path = fl_root+"pages/"
    if not os.path.exists(fl_path):
        os.makedirs(fl_path)
    # 由于有目录，因此不需要一页页的翻，先获取目录以及各页链接
    res = requests.get(url).text
    content = BeautifulSoup(res, features="lxml")
    directories = content.find(class_="dropdown-menu").find_all("a")
    directories = [h.get('href') for h in directories]
    page_id = 1
    # 访问每篇介绍的url保存网页
    for d in directories:
        if d:
            url = root_page+d
            res = requests.get(url).text
            content = BeautifulSoup(res, features="lxml")
            page_name = "【"+str(page_id).zfill(4)+"】"+content.find("title").text+".html"
            with open(fl_path+page_name, "w", encoding='utf-8') as pg:
                pg.write(res)
            page_id += 1


if __name__ == '__main__':
    get_pages(root_page, root+path)