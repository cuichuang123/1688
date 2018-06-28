#coding: utf-8
#爬虫
import os
import requests
import time
from selenium import webdriver

# 初始化（打开浏览器和网页）
def openUrl():
    url = 'https://www.1688.com/?spm=a260j.18362.0.d5.55525860IIvIiC'
    chromedriver = "C:\Program Files (x86)\Google\Chrome\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)  # 打开网页
    print '请登录'
    time.sleep(60)
    return driver

class Spiser(object):
    def __init__(self):
        self.driver = openUrl()
    def get_pageData(self,page_num):
        req_url = 'https://dcms.1688.com/open/query.json?app=DCMS&dataId=330&to=3000&sk0=798ba2e42d49cb746ca42403b21ce617&callback=jQuery18306774939526616679_1511922432325&deepTagIds=0&categoryId1s=0&n=20&pageNo=' + str(page_num) + '&categoryId2s=0&_=1511922433126'
        res = requests.get(req_url)
        pagedata = res.text
        if pagedata.startswith('jQuery18306774939526616679'):
            print '本页数据获取成功'
            return pagedata
        else:
            print '本页数据获取失败'
            time.sleep(30)
            return None
    def get_urlpage(self,req_url):
        print '获取页面数据',req_url
        time.sleep(2.2)
        self.driver.get(req_url)
        # 鼠标滚轮滑动至页面底部
        page_h = self.driver.find_element_by_xpath('/html/body').get_attribute("scrollHeight")
        for i in range(int(page_h) / 250):
            self.driver.execute_script("window.scrollBy(0, 250)", "")
            time.sleep(0.15)
        # 获取当前页面的地址，判断是否挑至验证页面
        cur_url = self.driver.current_url
        if 'sec.1688' in cur_url:
            print '进入验证页面'
            print '手动输入验证码'
            while (True):
                time.sleep(10)
                # cur_url = self.driver.current_url
                # self.driver.get('https://corp.1688.com/page/index.htm?memberId=b2b-2000958677&fromSite=company_site&tab=companyWeb_contact')
                # time.sleep(1)
                # self.driver.get(req_url)
                # time.sleep(2)
                if 'sec.1688.com' not in cur_url:
                    print '验证成功,恢复正常'
                    break
        page_data = self.driver.page_source
        return page_data
