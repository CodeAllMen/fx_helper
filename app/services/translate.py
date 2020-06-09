"""
Create by yy on 2020/6/8
"""
import getopt
import sys
from time import sleep

from tool_yy import debug

from app.tools import translate


class Translate(object):
    def __init__(self, db, log):
        """
        construct 构造函数
        :param db:
        :param log:
        """
        self.db = db
        self.log = log
        self.table = ''
        self.src_column = ''
        self.dest_column = ''
        self.src_lan = ''
        self.dest_lan = ''
        self.condition_column = ''
        self.translate = translate.Translate()

    def run(self):
        """
        init database info and got params which should need to handle
        :return:
        """
        argv = sys.argv[2:]
        self.get_info(argv)
        data = self.get_data_list()
        # 遍历进行翻译
        self.handle(data)

    def handle(self, data):
        """
        start handle data
        :param data:
        :return:
        """
        for item in data:
            update_arr = dict()
            update_arr[self.dest_column] = self.translate.translate_com(item[self.src_column], self.src_lan,
                                                                        self.dest_lan)
            self.update(update_arr, item[self.condition_column])
            # 睡眠三秒，否则接口会报错 too many requests
            # sleep three seconds, otherwise the api will return an error "too many requests"
            sleep(3)

    def update(self, update_arr, update_condition):
        """
        update data
        :param update_condition:
        :param update_arr:
        :return:
        """
        self.db.update({
            "table": self.table,
            "set": update_arr,
            "condition": ["{condition_column}={condition}".format(condition_column=self.condition_column,
                                                                  condition=update_condition)]
        })

    def get_data_list(self):
        """
        get all data which needs to handle
        :return:
        """
        return self.db.select({
            "table": self.table,
            "condition": ["{column}!=''".format(column=self.dest_column)]
        }, is_close_db=False)

    def get_info(self, argv):
        """
        get value from argv
        :param argv:
        :return:
        """
        try:
            opts, args = getopt.getopt(argv, "hd:t:p:u:s:a:sl:dl:c:",
                                       ["database=", "table=", "password=", "username=", "src_column=", "dest_column=",
                                        "src_lan=", "dest_lan=", "condition_column="])
        except Exception as e:
            debug('translate: -d <database>\n\t-t <table>\n\t-p '
                  '<password>\n\t-u <username>\n\t-s <src_column>'
                  '\n\t-a <dest_column> \n\t-sl <src_lan> \n\t-dl <dest_lan>'
                  '\n\t-c <condition_column>')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                debug('translate: -d <database>\n\t-t <table>\n\t-p '
                      '<password>\n\t-u <username>\n\t-s <src_column>'
                      '\n\t-a <dest_column> \n\t-sl <src_lan> \n\t-dl <dest_lan>'
                      '\n\t-c <condition_column>')
                sys.exit(2)
            elif opt in ('-d', '--database'):
                self.db.database = arg
            elif opt in ('-t', '--table'):
                self.table = arg
            elif opt in ('-p', '--password'):
                self.db.password = arg
            elif opt in ('-u', '--username'):
                self.db.username = arg
            elif opt in ('-s', '--src_column'):
                self.src_column = arg
            elif opt in ('-a', '--dest_column'):
                self.dest_column = arg
            elif opt in ('-sl', '--src_lan'):
                self.src_lan = arg
            elif opt in ('-dl', '--dest_lan'):
                self.dest_lan = arg
