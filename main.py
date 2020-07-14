"""
Create by yy on 2020/3/10
"""
import sys

from tool_yy import debug

from app import helper

if __name__ == "__main__":
    if len(sys.argv) < 2:
        debug("please input args which you want to run.")
        exit(1)
    args = sys.argv[1:2]
    if args[0] == 'translate':
        helper.translate.run()
    elif args[0] == 'read_video_2_psql':
        helper.read_video_2_psql.run()
    elif args[0] == 'get_clinkclick_game':
        helper.get_clinkclick_game.run()
    else:
        debug(args)
    # debug("ok")
    # helper.download_fitness.run()
