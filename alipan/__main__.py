#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: qicongsheng
import argparse
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))
from alipan import aligo_utils


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-login", action='store_true')
    parser.add_argument("-upload", nargs=2, help='alipan -upload /tmp/test.mp4 music')
    parser.add_argument("-download", nargs='+', help='alipan -download music/test.mp4 /tmp')
    parser.add_argument("-mv", nargs=2, help='alipan -mv music/test.mp4 music/test1.mp4')
    parser.add_argument("-rm", nargs=1, help='alipan -rm music/test.mp4')
    parser.add_argument("-ls", nargs='?', type=str, default='')
    args = parser.parse_args()
    if args.login:
        aligo_utils.login()
    elif args.upload is not None:
        aligo_utils.upload(args.upload[0], args.upload[1])
    elif args.download is not None:
        local_folder = '.' if len(args.download) == 1 else args.download[1]
        aligo_utils.download(args.download[0], local_folder)
    elif args.mv is not None:
        aligo_utils.mv(args.mv[0], args.mv[1])
    elif args.rm is not None:
        aligo_utils.rm(args.rm[0])
    elif args.ls != '':
        aligo_utils.ls(args.ls)


if __name__ == "__main__":
    main()
