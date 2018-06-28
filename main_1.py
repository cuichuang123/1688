#coding: utf-8
import time
from dataManager import DataManager
from spider import Spiser
import dataParser
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def run():
    #数据爬取器
    factory_spider = Spiser()
    #数据解析器
    json_parser = dataParser.DataParser()
    data_manager = DataManager()
    #总页数:250页
    total_page = 251
    #获取数据
    for i in range(total_page):
        print i
        pagedata = factory_spider.get_pageData(i)
        if pagedata is not None:
            factory_list = json_parser.json_parser(pagedata)
            data_manager.save_local(factory_list)
        time.sleep(1.5)

if __name__ == "__main__":
    run()