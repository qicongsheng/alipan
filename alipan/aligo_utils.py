#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: qicongsheng
from aligo import Aligo
import os
import logging


def login():
    ali = Aligo(level=logging.INFO)
    user = ali.get_user()
    print('login success: ', user.nick_name)


def download(pan_file_path, local_folder):
    ali = Aligo(level=logging.INFO)
    remote_file = ali.get_file_by_path(pan_file_path)
    if remote_file.type == 'file':
        download_result = ali.download_file(file=remote_file, local_folder=local_folder)
    else:
        download_result = ali.download_folder(remote_file.file_id, local_folder=local_folder)
    print(download_result)


def upload(target_file, pan_path):
    ali = Aligo(level=logging.INFO)
    remote_folder = ali.get_file_by_path(pan_path)
    if os.path.isfile(target_file):
        upload_result = ali.upload_file(target_file, remote_folder.file_id)
    else:
        upload_result = ali.upload_folder(target_file, remote_folder.file_id)
    print(upload_result)


def ls(pan_path):
    pan_path = '' if pan_path is None else pan_path
    pan_path = pan_path.strip()
    pan_path = pan_path[0:-1] if pan_path.endswith('/') or pan_path.endswith('\\') else pan_path
    ali = Aligo(level=logging.ERROR)
    remote_folder = ali.get_file_by_path(pan_path)
    files = ali.get_file_list(remote_folder.file_id)
    # 遍历文件列表
    for f in files:
        updated_date = f.updated_at.replace('T', ' ')[:19]
        file_size = str(round(f.size / 1024.0 / 1024.0, 3)) + 'M' if f.type == 'file' else '-'
        print('%s   %s   %s  %s' % ('{0:<6}'.format(f.type), '{0:<8}'.format(file_size), updated_date, pan_path + '/' + f.name))


def mv(old_pan_file_name, new_pan_file_name):
    ali = Aligo(level=logging.ERROR)
    old_remote_pan_file = ali.get_file_by_path(old_pan_file_name)
    return ali.rename_file(old_remote_pan_file.file_id, new_pan_file_name)


def rm(pan_file_name):
    ali = Aligo(level=logging.ERROR)
    remote_pan_file = ali.get_file_by_path(pan_file_name)
    return ali.move_file_to_trash(remote_pan_file.file_id)

