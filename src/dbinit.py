
import pymysql
from config import WEIBO_SPIDER_CONFIG

def db_init():
    sql = '''
    CREATE TABLE `weibo_topdata_all` (
        `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
        `time` timestamp NULL DEFAULT NULL,
        `pos` tinyint(2) DEFAULT NULL,
        `desc` varchar(30) DEFAULT NULL,
        `desc_extr` int(10) DEFAULT NULL,
        PRIMARY KEY (`id`) USING BTREE
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
    '''
    
    sql2 = '''
    CREATE TABLE `weibo_topdata_realtime` (
        `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
        `time` timestamp NULL DEFAULT NULL,
        `pos` tinyint(2) DEFAULT NULL,
        `desc` varchar(30) DEFAULT NULL,
        `desc_extr` int(10) DEFAULT NULL,
        PRIMARY KEY (`id`) USING BTREE
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
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
        cursor.execute(sql2)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    else:
        print('ok')

if __name__ == "__main__":
    db_init()
