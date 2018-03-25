# search from baidu.com
import requests
import re
import sys
import threading

__author__ : "d4m1ts"
__version__ = "v0.0.2"

# 定义全局变量，用于存放所有的 subdomain
all_sub_domain = []

class crew:
    def __init__(self,url):
        '''传入关键词'''
        self.url = url

    #第一页 page_num = 0，每一页+10
    def get_sub_domain(self,page_num=0):
        '''
        rtype : generate
        rtext : all domain
        '''
        #print ('[+] 正在爬取第 %d 页'%(page_num/10+1))
        url = 'https://www.baidu.com/s?wd=site:%s&pn=%d'%(self.url,page_num)
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        content = requests.get(url,headers=headers).content

        if 'class="n">下一页' in content.decode():
            new_page_num = page_num + 10
            url = 'https://www.baidu.com/s?wd=site:%s&pn=%s'%(self.url,new_page_num)
            threading.Thread(target=self.get_sub_domain,args=(new_page_num,)).start()

        regex = '\w*\.%s'%self.url
        one_page_urls = re.findall(regex,content.decode())    # 匹配出所有的含有子域名的标签

        f = open('sub_domain.txt','a')
        for one_url in one_page_urls:
            if one_url not in all_sub_domain and self.is_alive('http://' + one_url):
                all_sub_domain.append(one_url)
                print (one_url)
                f.write(one_url + '\n')
        f.close()

    # 存活性检测
    def is_alive(self,url):
        '''
        type url : str
        parma url : Judge whether URL is alive or not

        rtype : boolean
        '''
        try:
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
            if requests.get(url,headers=headers,timeout=1).status_code == 200:
                return True
            else:
                return False
        except:
            return False

    def main(self):
        self.get_sub_domain()

if __name__ == '__main__':
    url = sys.argv[1]
    instance = crew(url)
    instance.main()
