#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: qicongsheng
from aligo import Aligo
import os

def login():
    ali = Aligo()
    user = ali.get_user()
    print('login success: ', user.nick_name)


def download(pan_file_path, local_folder):
    ali = Aligo()
    remote_file = ali.get_file_by_path(pan_file_path)
    if remote_file.type == 'file':
        download_result = ali.download_file(file=remote_file, local_folder=local_folder)
    else:
        download_result = ali.download_folder(remote_file.file_id, local_folder=local_folder)
    print(download_result)


def upload_file(target_file, pan_path):
    ali = Aligo()
    remote_folder = ali.get_file_by_path(pan_path)
    if os.path.isfile(target_file):
        upload_result = ali.upload_file(target_file, remote_folder.file_id)
    else:
        upload_result = ali.upload_folder(target_file, remote_folder.file_id)
    print(upload_result)


def ls(pan_path):
    pan_path = '' if pan_path is None else pan_path
    ali = Aligo()
    remote_folder = ali.get_file_by_path(pan_path)
    files = ali.get_file_list(remote_folder.file_id)
    # 遍历文件列表
    for f in files:
        print(f.file_id, f.name, f.type)
