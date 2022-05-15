#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: qicongsheng
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))
from alipan import aligo_utils, help


def main():
    action = sys.argv[1] if len(sys.argv) > 1 else 'help'
    action_arg1 = sys.argv[2] if len(sys.argv) > 2 else None
    action_arg2 = sys.argv[3] if len(sys.argv) > 3 else None
    if action == 'login':
        aligo_utils.login()
    elif action == 'logout':
        aligo_utils.logout()
    elif action == 'upload':
        aligo_utils.upload(action_arg1, action_arg2)
    elif action == 'download':
        local_folder = '.' if action_arg2 is None else action_arg2
        aligo_utils.download(action_arg1, local_folder)
    elif action == 'mv':
        aligo_utils.mv(action_arg1, action_arg2)
    elif action == 'rm':
        aligo_utils.rm(action_arg1)
    elif action == 'cd':
        aligo_utils.cd(action_arg1)
    elif action == 'pwd':
        aligo_utils.pwd()
    elif action == 'exist':
        aligo_utils.exist(action_arg1)
    elif action == 'version':
        help.print_version()
    elif action == 'help':
        help.print_help()
    elif action == 'ls':
        aligo_utils.ls(action_arg1)
    else:
        print('unsupported command: %s' % action)
        help.print_help()


if __name__ == "__main__":
    main()
