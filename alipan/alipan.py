#!/usr/bin/python
# -*- coding: UTF-8 -*-
from aligo import Aligo

if __name__ == '__main__':
    ali = Aligo()  # 第一次使用，会弹出二维码，供扫描登录
    user = ali.get_user()  # 获取用户信息
    print(user.user_name)
    print(user.status)
    ll = ali.get_file_list()  # 获取网盘根目录文件列表
    # 遍历文件列表
    for file in ll:
        print(file.file_id, file.name, file.type)
    remote_folder = ali.get_file_by_path('乱件')
    upload_result = ali.upload_file('D:/backup/vms/win10_clean_vmware.zip', remote_folder.file_id)
    print(upload_result)

