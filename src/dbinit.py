
import pymysql
from config import WEIBO_SPIDER_CONFIG

def db_init():
    sql = '''
    CREATE TABLE `weibo_topdata_all`  (
    `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `time` timestamp(0) NULL DEFAULT NULL,
    `pos` tinyint(2) NULL DEFAULT NULL,
    `desc` varchar(30) CHARACTER SET gb2312 COLLATE gb2312_chinese_ci NULL DEFAULT NULL,
    `desc_extr` int(10) NULL DEFAULT NULL,
    PRIMARY KEY (`id`) USING BTREE
    ) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;
    '''

    db = pymysql.connect(
        host=WEIBO_SPIDER_CONFIG['database']['host'],
        port=WEIBO_SPIDER_CONFIG['database']['port'],
        user=WEIBO_SPIDER_CONFIG['database']['user'],
        password=WEIBO_SPIDER_CONFIG['database']['password'],
        database=WEIBO_SPIDER_CONFIG['database']['name'],
    )
    cursor = db.cursor()

    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    else:
        print('ok')

if __name__ == "__main__":
    db_init()
