#coding: utf-8
#页面内容解析器
import json
from lxml import etree


class DataParser(object):
    def __init__(self):
        pass
    #将jsonp类型的数据换成json
    def jsonp_parser(self,json_str):
        json_data = json_str.replace("jQuery18306774939526616679_1511922432325(","")
        res = json_data.replace(")","")
        return res
    def json_parser(self,json_str):
        res = self.jsonp_parser(json_str)
        # 商家的店铺链接、
        # 商家名称loginId/ shortName、
        # 公司名称companyName、
        # 地点companyLocation、
        # memberid、
        # 类目deepTag/取name显示,忽略ID/ extCategory
        json_dic = json.loads(res)
        content = json_dic.get('content')
        factorys = content.get('data')
        factory_list = []
        for factory  in factorys:
            loginId = factory.get('loginId')
            winportLink = factory.get('winportLink')
            companyLocation = factory.get('companyLocation')
            shortName = factory.get("shortName")
            companyName = factory.get("companyName")
            memberId = factory.get("memberId")
            deepTag = factory.get("deepTag")
            extCategory = factory.get("shopFactorySecondPageSearch.extCategory")
            line = loginId,winportLink,companyLocation,shortName,companyName,memberId,deepTag,extCategory
            factory_list.append(line)
        return factory_list
    #根据公司黄页内容，提取其中的联系方式等有用信息
    def get_company_data(self,page_data,page_shop1,page_shop2,url):
        #==============解析page_data======================
        try:
            page_html = etree.HTML(page_data)
            man_xpath = '//div[@class="contact-name"]/text()'
            companyname_xpath = '//b[@class="compay-name"]/text()'
            wangwang_xpath = '//div[@class="contact-name"]/a/@data-alitalk'
            man_data = page_html.xpath(man_xpath)
            companyname_data = page_html.xpath(companyname_xpath)
            wangwang_data  = page_html.xpath(wangwang_xpath)
            man = man_data[0].strip()
            companyname= companyname_data[0]
            wangwang = wangwang_data[0]
        except Exception,e:
            man = None
            companyname = None
            wangwang = None
            print 'error公司黄页',url
            print e

        try:
            cate_xpath = '//tbody/tr[@class="content-info"]/td[@class="title"]/p/text()'
            cate =  page_html.xpath(cate_xpath)
            num = len(cate)
            phone = None
            address = None
            cellphone = None
            for i in range(num):
                cate_xpath = '//tbody/tr[' + str(i + 2) + ']/td[1]/p/text()'
                cate_content_xpath = '//tbody/tr['+str(i+2)+']/td[2]/p/text()'
                cate = page_html.xpath(cate_xpath)
                cate_content = page_html.xpath(cate_content_xpath)
                if cate[0] == '电话 :':
                    phone = cate_content[0]
                elif cate[0] == '地址 :':
                    address = cate_content[0]
                elif cate[0] == '移动电话 :':
                    cellphone = cate_content[0].strip()
        except Exception,e:
            print e,u'获取电话地址失败'
            phone = None
            address = None
            cellphone = None
        try:
            companyUrl_xpath = '//tr[@class="content-info"]/td[@class="info"]/p/a/@href'
            company_url_data = page_html.xpath(companyUrl_xpath)
            company_url = company_url_data[0]
        except Exception,e:
            print e,u'获取公司链接失败'
            company_url = None

        #===============解析page_shop1====================
        page_html1 = etree.HTML(page_shop1)
        try:
            phone1_xpath = '//div[@class="m-content"]/div[@class="content"]/table/tbody/tr[1]/td/text()'
            phone1_data = page_html1.xpath(phone1_xpath)
            phone1 = phone1_data[0].strip()

        except Exception,e:
            print e,'phone1获取失败',url
            phone1 = None
        #===============解析page_shop2====================
        page_html2 = etree.HTML(page_shop2)
        try:
            phone2_xpath = '//dl[@class="m-mobilephone"]/dd/text()'
            phone2_data = page_html2.xpath(phone2_xpath)
            phone2 = phone2_data[0].strip()
        except Exception,e:
            print e,'phone2获取失败',url
            phone2 = None
        try:
            tel_cate_xpath = '//div[@class="contcat-desc"]/dl[1]/dt/text()'
            telphone_xpath = '//div[@class="contcat-desc"]/dl[1]/dd/text()'
            tel_cate = page_html2.xpath(tel_cate_xpath)
            if tel_cate[0] == '电      话：':
                print '获取电话号码'
                telphone_data = page_html2.xpath(telphone_xpath)
                telphone = telphone_data[0]
            else:
                telphone = None
        except Exception,e:
            print e,'电话号码获取失败',url
            telphone = None
        line = man,companyname,address,cellphone,company_url,phone,phone1,phone2,telphone,url,wangwang
        return line