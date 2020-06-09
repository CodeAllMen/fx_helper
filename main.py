"""
Create by yy on 2020/3/10
"""
import sys

from tool_yy import debug

from app import helper

if __name__ == "__main__":
    args = sys.argv[1:2]
    if args[0] == 'translate':
        helper.translate.run()
    else:
        debug(args)
    # debug("ok")
    # helper.download_fitness.run()
