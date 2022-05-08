#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: qicongsheng
def get_version():
    return '1.2.28'


def print_help():
    print('''alipan %s
Commandline tools for aliyundrive.
Usage: alipan [ACTION] [ARGUMENT]...

ACTION
  login           login alipan
                  example: alipan login
  logout          logout alipan
                  example: alipan logout
  upload          upload file[folder] to alipan
                  example: alipan upload c:/a.txt /remote/folder/path
  download        download file[folder] from alipan
                  example: alipan download /remote/file/path/foo.mp4 c:/backup
  mv              rename alipan file[folder]
                  example: alipan mv /remote/file/path/foo.mp4 foo2.mp4
  rm              delete alipan file[folder]
                  example: alipan rm /remote/file/path/foo.mp4
  cd              change work dictory
                  example: alipan cd /remote/folder/path
  ls              show folder file list
                  example: alipan ls
  pwd             show current work dictory
                  example: alipan pwd
  exist           show file[folder] exist or not
                  example: alipan exist /remote/file/path/foo.mp4
    ''' % get_version())