#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: qicongsheng
from aligo import Aligo
import os
import logging
from pathlib import Path


def login():
    ali = Aligo(level=logging.INFO)
    user = ali.get_user()
    write_aligo_env('/')
    print('login success: ', user.nick_name)


def logout():
    aligo_tmp_file = Path.home().joinpath('.aligo').joinpath('aligo_tmp.json')
    aligo_config_file = Path.home().joinpath('.aligo').joinpath('aligo.json')
    os.remove(aligo_tmp_file)
    os.remove(aligo_config_file)
    print('logout success!')


def download(pan_file_path, local_folder='./'):
    pan_file_path = pan_file_path.strip()
    pan_file_path = pan_file_path if pan_file_path.startswith('/') else get_work_dir() + pan_file_path
    ali = Aligo(level=logging.INFO)
    remote_file = ali.get_folder_by_path(pan_file_path)
    if remote_file is not None and remote_file.type != 'file':
        download_result = ali.download_folder(remote_file.file_id, local_folder=local_folder)
    else:
        remote_file = ali.get_file_by_path(pan_file_path)
        download_result = ali.download_file(file=remote_file, local_folder=local_folder)
    print(download_result)


def upload(target_file, pan_path=None):
    pan_path = pan_path if pan_path is not None else get_work_dir()
    pan_path = pan_path.strip()
    pan_path = pan_path if pan_path.startswith('/') else get_work_dir() + pan_path
    ali = Aligo(level=logging.INFO)
    remote_folder = ali.get_folder_by_path(pan_path)
    if os.path.isfile(target_file):
        upload_result = ali.upload_file(target_file, remote_folder.file_id)
    else:
        upload_result = ali.upload_folder(target_file, remote_folder.file_id)
    print(upload_result)


def ls(pan_path=None):
    pan_path = get_work_dir() if pan_path is None else pan_path
    pan_path = pan_path.strip()
    pan_path = pan_path if pan_path.endswith('/') else pan_path + '/'
    pan_path = pan_path if pan_path.startswith('/') else get_work_dir() + pan_path
    if not exist(pan_path):
        print('%s not exist' % pan_path[:-1])
        return
    ali = Aligo(level=logging.ERROR)
    remote_folder = ali.get_folder_by_path(pan_path)
    if remote_folder is None or remote_folder.type == 'file':
        print('%s is not a folder' % pan_path[:-1])
        return
    files = ali.get_file_list(remote_folder.file_id)
    # 遍历文件列表
    for f in files:
        updated_date = f.updated_at.replace('T', ' ')[:19]
        file_size = str(round(f.size / 1024.0 / 1024.0, 3)) + 'M' if f.type == 'file' else '-'
        file_name = f.name[1:] if f.name.startswith('/') else f.name
        print('%s   %s   %s  %s' % ('{0:<6}'.format(f.type), '{0:<8}'.format(file_size), updated_date, pan_path + file_name))


def mv(old_pan_file_name, new_pan_file_name):
    old_pan_file_name = old_pan_file_name.strip()
    old_pan_file_name = old_pan_file_name if old_pan_file_name.startswith('/') else get_work_dir() + old_pan_file_name
    ali = Aligo(level=logging.ERROR)
    old_remote_pan_file = ali.get_file_by_path(old_pan_file_name)
    if old_remote_pan_file is None:
        print('%s not exist' % old_pan_file_name)
        return
    mv_result = ali.rename_file(old_remote_pan_file.file_id, new_pan_file_name)
    return mv_result


def rm(pan_file_name):
    pan_file_name = pan_file_name.strip()
    pan_file_name = pan_file_name if pan_file_name.startswith('/') else get_work_dir() + pan_file_name
    ali = Aligo(level=logging.ERROR)
    remote_pan_file = ali.get_file_by_path(pan_file_name)
    if remote_pan_file is None:
        print('%s not exist' % remote_pan_file)
        return
    return ali.move_file_to_trash(remote_pan_file.file_id)


def cd(pan_path):
    pan_path = '/' if pan_path is None else pan_path.strip()
    pan_path = pan_path if pan_path.startswith('/') else get_work_dir() + pan_path
    pan_path = pan_path if pan_path.endswith('/') else pan_path + '/'
    if not exist(pan_path):
        print('%s not exist' % pan_path[:-1])
        return
    ali = Aligo(level=logging.ERROR)
    remote_pan_file = ali.get_folder_by_path(pan_path)
    if remote_pan_file is None or remote_pan_file.type == 'file':
        print('%s is not a folder' % pan_path[:-1])
        return
    if remote_pan_file is not None and remote_pan_file.type == 'folder':
        write_aligo_env(pan_path)
        print(pan_path[:-1] if pan_path != '/' else '/')


def exist(pan_path):
    pan_path = '/' if pan_path is None else pan_path.strip()
    pan_path = pan_path if pan_path[0] == '/' else '/' + pan_path
    pan_path = pan_path[:-1] if pan_path.endswith('/') else pan_path
    pan_pathes = pan_path.split('/')
    pan_pathes[0] = '/'
    ali = Aligo(level=logging.ERROR)
    target_path = ''
    for i, path_check in enumerate(pan_pathes):
        if i == len(pan_pathes) - 1:
            break
        if i == 0:
            target_path = target_path + path_check
        else:
            target_path = target_path + '/' + path_check
        remote_target_path = ali.get_folder_by_path(target_path)
        files = ali.get_file_list(remote_target_path.file_id)
        is_exist = False
        for f in files:
            if f.name == pan_pathes[i + 1]:
                is_exist = True
                break
        if not is_exist:
            return False
    return True


def pwd():
    pwd_path = read_aligo_env()
    pwd_path = '/' if pwd_path is None else pwd_path
    pwd_result = pwd_path[:-1] if pwd_path != '/' else '/'
    print(pwd_result)
    return pwd_result


def read_aligo_env():
    aligo_tmp_file = Path.home().joinpath('.aligo').joinpath('aligo_tmp.json')
    try:
        with open(aligo_tmp_file, 'r') as file_object:
            return file_object.read()
    except:
        login()
        return read_aligo_env()


def write_aligo_env(content):
    aligo_tmp_file = Path.home().joinpath('.aligo').joinpath('aligo_tmp.json')
    with open(aligo_tmp_file, 'w+') as file_object:
        file_object.write(content)


def get_work_dir():
    tmp_content = read_aligo_env()
    return tmp_content

