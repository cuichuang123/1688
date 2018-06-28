#coding: utf-8
import time
from dataManager import DataManager
from spider import Spiser
import dataParser
import sys
from urlManager import UrlManager
reload(sys)
sys.setdefaultencoding('utf8')

def run():
    #数据爬取器
    factory_spider = Spiser()
    #数据解析器
    data_parser = dataParser.DataParser()
    data_manager = DataManager()
    url_manager = UrlManager()
    #获取到三个url列表,均为需要爬取的数据
    url_list, shopurl1_list, shopurl2_list = url_manager.tel_url()
    total_num = len(url_list)
    crawred_url = url_manager.crawred_url()
    company_dataList = []

    for i in range(total_num):
        url = url_list[i]
        shopurl1 = shopurl1_list[i]
        shopurl2 = shopurl2_list[i]

        if url not in crawred_url:
            page_data = factory_spider.get_urlpage(url)
            page_shop1 = factory_spider.get_urlpage(shopurl1)
            page_shop2 = factory_spider.get_urlpage(shopurl2)
            #使用解析器，解析三个页面的数据
            companydata = data_parser.get_company_data(page_data,page_shop1,page_shop2,url)
            #将解析后的数据元组保存至列表
            company_dataList.append(companydata)
            time.sleep(1.1)
        # elif url in crawred_url:
        #     print '已经爬取过了',url

        # 将爬取结果保存至本地csv文件,爬5家店铺保存一次
        print '=========',i,'=========='
        if i % 10 == 0 and len(company_dataList)>0:
            data_manager.save_local_tel(company_dataList)
            company_dataList = []
            time.sleep(10)
if __name__ == "__main__":
    run()