
import requests
import json
import time
import pymysql
from src.config import WEIBO_SPIDER_CONFIG

class WeiBoSpider:

    def __init__(self):
        self.db = pymysql.connect(
            host=WEIBO_SPIDER_CONFIG['database']['host'],
            port=WEIBO_SPIDER_CONFIG['database']['port'],
            user=WEIBO_SPIDER_CONFIG['database']['user'],
            password=WEIBO_SPIDER_CONFIG['database']['password'],
            database=WEIBO_SPIDER_CONFIG['database']['name'],
        )
        self.cursor = self.db.cursor()
        self.topdata=None
        self.time=None


    def __del__(self):
        self.db.close()


    def get_top_data(self):
        url = "https://m.weibo.cn/api/container/getIndex"
        get_params = {
            "containerid": "106003type=25&t=3&disable_hot=1&filter_type=realtimehot"
        }

        r = requests.get(url=url, params=get_params)
        self.topdata = r.json()
        self.time = str(round(time.time()))
        r.close()
        return r.status_code


    def write2db(self):        
        for i, t in enumerate(self.topdata["data"]["cards"][0]["card_group"]):
            if "desc_extr" in t:
                sql = "INSERT INTO `weibo_topdata_all`(`time`, `pos`, `desc`, `desc_extr`) VALUES (from_unixtime({0},'%Y-%m-%d %H:%i:%s'), {1}, '{2}', {3})".format(self.time, i, t["desc"], t["desc_extr"])
                try:
                    self.cursor.execute(sql)
                    self.db.commit()
                    pass
                except:
                    self.db.rollback()
                    # print("insert data to db failed")
                else:
                    # print(sql)
                    pass


    def write2db_realtime(self):
        try:
            self.cursor.execute("TRUNCATE TABLE `weibo_topdata_realtime`;")     # 截断表
            self.db.commit()
        except:
            self.db.rollback()
            # print('TRUNCATE failde')
        else:
            for i, t in enumerate(self.topdata["data"]["cards"][0]["card_group"]):
                if "desc_extr" in t:
                    sql = "INSERT INTO `weibo_topdata_realtime`(`time`, `pos`, `desc`, `desc_extr`) VALUES (from_unixtime({0},'%Y-%m-%d %H:%i:%s'), {1}, '{2}', {3})".format(self.time, i, t["desc"], t["desc_extr"])
                    try:
                        self.cursor.execute(sql)
                        self.db.commit()
                        pass
                    except:
                        self.db.rollback()
                        # print("insert data to db failed")
                    else:
                        # print(sql)
                        pass


    def run(self):
        if self.get_top_data() == 200:
            self.write2db()
            self.write2db_realtime()    # 写入存放实时数据的表
            print('done!')
        else:
            print('get data from weibo failed')
