#coding: utf-8
import csv

from dataManager import DataManager


class UrlManager(object):
    def __init__(self):
        self.data_manager = DataManager()
    #拼接公司黄页的链接
    def tel_url(self):
        memberId_list, shop_url = self.data_manager.read_local()
        url_list = []
        shopurl1_list = []
        shopurl2_list = []
        for memberId in memberId_list:
            url = 'https://corp.1688.com/page/index.htm?memberId='+str(memberId)+'&fromSite=company_site&tab=companyWeb_contact'
            url_list.append(url)
        for shopurl in shop_url:
            url1 = shopurl + '/page/merchants.htm'
            url2 = shopurl + '/page/contactinfo.htm??smToken=d6f92a6aadd34fa3aef88809a6d9f7d1&smSign=ADUiGA9MZ4pScu4JQD9FWg%3D%3D'
            shopurl1_list.append(url1)
            shopurl2_list.append(url2)
        return url_list,shopurl1_list,shopurl2_list
    #从本地获取已经爬取过的url，不要再爬第二次
    # 从本地读取数据
    def crawred_url(self):
        crawred_url = []
        try:
            with open('D:\\data\\1688factory_tel.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    crawred_url.append(row['url'])
        except Exception,e:
            print '未发现电话记录保存文件'
        return crawred_url

