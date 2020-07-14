"""
Create by yy on 2020/6/24
"""
from tool_yy import debug


class ReadVideo2Psql(object):
    def __init__(self, init_db, log):
        """
        :param init_db:
        :param log:
        """
        self.db = init_db("FOUR_K_VIDEO_CONFIG")
        self.log = log

    def run(self):
        url_list = self.get_data_from_file()
        video_list = self.get_list()
        self.handle(url_list, video_list)

    def handle(self, url_list, video_list):
        devide_len = len(url_list)
        for k, v in enumerate(video_list):
            key = k % devide_len
            update_arr = dict()
            update_arr["quality1080_p"] = url_list[key]
            update_arr["quality720_p"] = url_list[key]
            update_arr["quality480_p"] = url_list[key]
            update_arr["quality320_p"] = url_list[key]
            update_arr["quality240_p"] = url_list[key]
            update_id = video_list[k]["id"]
            self.update(update_arr, update_id)

    def update(self, update_arr, update_id):
        self.db.update({
            "table": "video_data",
            "set": update_arr,
            "condition": ["id='{id}'".format(id=update_id)]
        }, is_close_db=False)

    def get_data_from_file(self):
        """
        从文件获取数据
        :return:
        """
        url_list = list()

        with open('static/sexvideos.txt') as f:
            line = True

            while line:
                line = f.readline()
                if line != "":
                    url_list.append(line.replace('\n', ''))
            f.close()

        return url_list

    def get_list(self):
        return self.db.select({
            "table": "video_data",
            "columns": ['id']
        }, is_close_db=False)
