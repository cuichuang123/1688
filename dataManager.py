#coding: utf-8
#处理结果保存器
import codecs
import csv

class DataManager(object):
    def __init__(self):
        pass
    #将页面获取到的json文本直接保存,文件写入文本并保存在本地
    def save_local(self,data):
        # headers = ['loginId', 'winportLink', 'companyLocation','shortName', 'companyName', 'memberId','deepTag', 'extCategory']
        #data为需要被写入的数据(可以为数据元组存放于列表的形式，也可以为字典数据)
        with open('D:\\data\\1688factory_json.csv', 'ab+') as f:
            f.write(codecs.BOM_UTF8)# 防止乱码
            f_csv = csv.writer(f)
            # f_csv.writerow(headers)
            f_csv.writerows(data)

    # 将页面获取到的json文本直接保存,文件写入文本并保存在本地
    def save_local_tel(self, data):
        # headers = ['name', 'companyname', 'address', 'cellphone','company_url', 'phone','phone1','phone2','telphone','url']
        # data为需要被写入的数据(可以为数据元组存放于列表的形式，也可以为字典数据)
        with open('D:\\data\\1688factory_tel.csv', 'ab+') as f:
            f.write(codecs.BOM_UTF8)  # 防止乱码
            f_csv = csv.writer(f)
            # f_csv.writerow(headers)
            f_csv.writerows(data)
    #从本地读取数据
    def read_local(self):
        memberId_list = []
        shop_url = []
        with open('D:\\data\\1688_factory.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # print row[' memberId']
                memberId_list.append(row['memberId'])
                shop_url.append(row['winportLink'])
        return memberId_list,shop_url
