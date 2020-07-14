"""
Create by yy on 2020/3/10
"""

__all__ = ["helper"]

from psql_yy import PsqlDB
from tool_yy import Helper

from .log import Log
from .services.read_video_2_psql import ReadVideo2Psql
from .services.translate import Translate
from .spiders.get_clinkclick_game import GetClinkClickGame
from .tools.utils import get_file_name


class HelperInstance(Helper):
    __slots__ = ("redis", "log", "psql")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def translate(self):
        return Translate(self.psql, self.log)

    @property
    def read_video_2_psql(self):
        return ReadVideo2Psql(self.psql, self.log)

    @property
    def get_clinkclick_game(self):
        return GetClinkClickGame(self.init_db)

    # @property
    # def download_fitness(self):
    #     return DownloadFitness(self.log)


def create_helper():
    helper_instance = HelperInstance()
    helper_instance.set_config("app.config.secure")
    helper_instance.set_config("app.config.settings")

    file_name = "{file_path}/{file_name}".format(
        file_path=helper_instance.config["LOG_FILE_PATH"],
        file_name=get_file_name()
    )
    helper_instance.log = Log(file_name, helper_instance.config["DEBUG"])

    PsqlDB().init_helper(helper_instance)

    return helper_instance


helper = create_helper()
