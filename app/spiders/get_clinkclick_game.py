"""
Create by yy on 2020/7/1
"""
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from tool_yy import debug, curl_data
from selenium.webdriver import Chrome


class GetClinkClickGame(object):
    def __init__(self, init_db):
        self.db = init_db('MYSQL_GAME_DOWNLOAD')
        self.driver = None
        self.host = "https://games.clinkclick.com/"

    def run(self):
        data = self.get_page_data()
        self.handle(data)

    def start_webdriver(self):
        options = Options()
        self.driver = Chrome(executable_path="chromedriver", options=options)

    def __del__(self):
        pass
        # self.driver.quit()

    def handle(self, data):
        data = BeautifulSoup(data, "html.parser")
        data_list = data.find_all("div", attrs={"class": "item"})
        for k, item in enumerate(data_list):
            insert_arr = dict()
            insert_arr["img"] = self.__get_img(item)
            insert_arr["name"] = self.__get_name(item)
            insert_arr["download_url"] = self.__get_download_url(item)
            insert_arr["category_id"] = (k % 5) + 1
            self.insert(insert_arr)

    def download_source(self):
        game_list = self.get_list()
        for game in game_list:
            debug(game)

    def __get_download_url(self, item):
        download_url = item.find("a")
        try:
            download_url = self.host + download_url.attrs["href"]
        except Exception as e:
            download_url = ""
            debug(e)
        return download_url

    def __get_name(self, item):
        name = item.find("div", attrs={"class": "fristDesc"})
        try:
            name = name.text
        except:
            name = ""
        return name

    def __get_img(self, item):
        img = item.find("img")
        try:
            src = img.attrs["src"]
            src = self.host + src
        except Exception as e:
            src = ""
            debug(e)
        return src

    def get_page_data(self):
        # self.start_webdriver()
        # request_url = "https://games.clinkclick.com/#/"
        # self.driver.get(request_url)

        # data = WebDriverWait(self.driver, 30, 0.2).until(lambda x: x.find_element_by_css_selector(".itemBox"))

        # data = self.driver.page_source

        # with open("static/spiders/get_clinkclick_game/index.html", "wb") as f:
        #     f.write(data.encode("utf-8"))
        #     f.close()
        with open("static/spiders/get_clinkclick_game/index.html", "rb") as f:
            data = f.read().decode("utf-8")
            f.close()

        return data

    def insert(self, insert_arr):
        sql = self.db.getInsertSql(insert_arr, "game_download")
        self.db.insert(sql, is_close_db=False)

    def get_list(self):
        return self.db.select({
            "table": "game_download"
        }, is_close_db=False)
