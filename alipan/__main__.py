#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: qicongsheng
import argparse
import aligo_utils


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-login", action='store_true')
    parser.add_argument("-upload", nargs=2, help='alipan -upload /tmp/test.mp4 music')
    parser.add_argument("-download", nargs=2, help='alipan -download music/test.mp4 /tmp')
    parser.add_argument("-ls", nargs='?', type=str, default='', help='alipan -download music/test.mp4 /tmp')
    args = parser.parse_args()
    print(args)
    if args.login:
        aligo_utils.login()
    elif args.upload is not None:
        aligo_utils.upload_file(args.upload[0], args.upload[1])
    elif args.download is not None:
        aligo_utils.download(args.download[0], args.download[1])
    elif args.ls != '':
        aligo_utils.ls(args.ls)


if __name__ == "__main__":
    print('An aliyundrive client tools.')
    main()
