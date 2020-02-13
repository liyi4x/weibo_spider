
from src.spider import WeiBoSpider

if __name__ == "__main__":
    weibo = WeiBoSpider()
    weibo.run()
    del weibo