from bs4 import BeautifulSoup
import requests, json, random


# 收录查询
pcRequestHeader = [
    'Mozilla/5.0 (Windows NT 5.1; rv:6.0.2) Gecko/20100101 Firefox/6.0.2',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.52 Safari/537.17',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.16) Gecko/20101130 Firefox/3.5.16',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; .NET CLR 1.1.4322)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2; zh-CN; rv:1.9.0.19) Gecko/2010031422 Firefox/3.0.19 (.NET CLR 3.5.30729)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13'
]
# class shouLuPcChongCha():
#     def __init__(self,lianjie, tid, search):
#         self.lianjie = lianjie
#         self.tid = tid
#         self.search = search
#
#     # 获取页面访问状态和标题
#     def getPageInfo(self, url):
#         headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)]}
#         try:
#             ret_two = requests.get(url, headers=headers, timeout=10)
#             ret_two_url = ret_two.url
#             status_code = ret_two.status_code
#             encode_ret = ret_two.apparent_encoding
#             if encode_ret == 'GB2312':
#                 ret_two.encoding = 'gbk'
#             else:
#                 ret_two.encoding = 'utf-8'
#             soup_two = BeautifulSoup(ret_two.text, 'lxml')
#             try:
#                 title = soup_two.find('title').get_text().strip().replace('\r\n', '')
#             except AttributeError:
#                 title = ''
#         # except ConnectionError:
#         except:
#             pass
#             status_code = 500
#             title = ''
#             ret_two_url = ''
#         return status_code, title, ret_two_url
#
#     # 百度pc端收录查询
#     def baiduShouLuPC(self, domain):
#         resultObj = {
#             "shoulu": 0,
#             "kuaizhao_time": '',
#             "title": '',
#             "status_code": ''
#         }
#         domain = domain.strip()
#         zhidao_url = 'http://www.baidu.com/s?wd={domain}'.format(domain=domain)
#         headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)]}
#         ret_domain = requests.get(zhidao_url, headers=headers, timeout=10)
#         soup_domain = BeautifulSoup(ret_domain.text, 'lxml')
#         if soup_domain.find('div', class_='content_none'):
#             resultObj["status_code"] = ret_domain.status_code
#         else:
#             div_tags = soup_domain.find_all('div', class_='result c-container ')
#             if div_tags and div_tags[0].attrs.get('id'):
#                 panduan_url = div_tags[0].find('a').attrs['href']
#                 f13_div = div_tags[0].find('div', class_='f13')
#                 if f13_div.find('a'):
#                     yuming = f13_div.find('a').get_text()[:-5].split('/')[0]  # 获取域名
#                     status_code, title, ret_two_url = self.getPageInfo(panduan_url)
#                     resultObj["title"] = title
#                     resultObj["status_code"] = status_code
#                     if div_tags[0].find('span', class_='newTimeFactor_before_abs'):
#                         resultObj["kuaizhao_time"] = div_tags[0].find('span',
#                             class_='newTimeFactor_before_abs').get_text().strip().replace('-', '').replace('年',
#                             '-').replace('月', '-').replace('日', '').strip()
#                     if yuming in domain:
#                         if domain in ret_two_url:
#                             resultObj["shoulu"] = 1
#         return resultObj
#
#     # 百度移动端收录查询
#     def baiduShouLuMobeil(self, domain):
#         resultObj = {
#             "shoulu": 0,
#             "kuaizhao_time": '',
#             "title": '',
#             "status_code": ''
#         }
#         domain = domain.strip()
#         zhidao_url = 'https://m.baidu.com/from=844b/pu=sz@1320_2001/s?tn=iphone&usm=2&word={}'.format(domain)
#         headers = {
#             'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
#         ret_domain = requests.get(zhidao_url, headers=headers, timeout=10)
#         soup_domain = BeautifulSoup(ret_domain.text, 'lxml')
#         if not soup_domain.find_all('div', class_='result c-result'):
#             resultObj["status_code"] = ret_domain.status_code
#         else:
#             div_tags = soup_domain.find_all('div', class_='result c-result')
#             if div_tags:
#                 dict_data_clog = eval(div_tags[0].attrs.get('data-log'))
#                 url = dict_data_clog['mu']
#                 if url.strip():
#                     status_code, title, ret_two_url = self.getPageInfo(url)
#                     resultObj["status_code"] = status_code
#                     resultObj["title"] = title
#                     if domain == url or url[:-1] == domain:
#                         resultObj["shoulu"] = 1
#         return resultObj
#
#     # 360pc端收录查询
#     def pcShoulu360(self, domain):
#         resultObj = {
#             "shoulu": 0,
#             "kuaizhao_time": '',
#             "title": '',
#             "status_code": '',
#             "rank_num": 0
#         }
#         headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)]}
#         pc_360url = 'https://so.com/s?src=3600w&q={domain}'.format(domain=domain)
#         ret_domain = requests.get(pc_360url, headers=headers, timeout=10)
#         soup = BeautifulSoup(ret_domain.text, 'lxml')
#         if soup.find('div', class_='so-toptip'):
#             resultObj['shoulu'] = '0'
#             resultObj["status_code"] = ret_domain.status_code
#         else:
#             li_tags = soup.find_all('li', class_='res-list')
#             if len(li_tags) > 0:
#                 zongti_xinxi = li_tags[0].find('a', target='_blank')  # 获取order -- title -- title_url
#                 yuming_canshu = li_tags[0].find('p', class_='res-linkinfo')  # 域名参数
#                 if li_tags[0].find('a').attrs.get('data-url'):
#                     data_url = li_tags[0].find('a').attrs.get('data-url')
#                 else:
#                     data_url = zongti_xinxi.attrs['href']
#                 yuming = yuming_canshu.find('cite').get_text()
#                 yuming_deal = yuming.split('/')[0].rstrip('...').split('>')[0]
#                 status_code, title, ret_two_url = self.getPageInfo(data_url)
#                 resultObj["status_code"] = status_code
#                 resultObj["title"] = title
#                 if yuming_deal in domain:
#                     if domain in ret_two_url:
#                         resultObj['shoulu'] = '1'
#         return resultObj
#
#     # 360移动端收录查询
#     def mobielShoulu360(self, domain):
#         resultObj = {
#             "shoulu": 0,
#             "kuaizhao_time": '',
#             "title": '',
#             "status_code": '',
#             "rank_num": 0
#         }
#         PC_360_url = 'https://m.so.com/s?src=3600w&q={}'.format(domain)
#         headers = {
#             'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
#         ret = requests.get(PC_360_url, headers=headers, timeout=10)
#         soup = BeautifulSoup(ret.text, 'lxml')
#         if soup.find('div', class_='mso-url2link'):
#             resultObj['shoulu'] = '0'
#             resultObj["status_code"] = ret.status_code
#         else:
#             div_tags = soup.find_all('div', class_=' g-card res-list og ')
#             if len(div_tags) > 0:
#                 url_data = div_tags[0].attrs.get('data-pcurl')
#                 status_code, title, ret_two_url = self.getPageInfo(url_data)
#                 resultObj["status_code"] = status_code
#                 resultObj["title"] = title
#                 if domain in ret_two_url:
#                     resultObj['shoulu'] = '1'
#         return resultObj
#
#     # 判断搜索引擎
#     def judgmentSearchEngine(self):
#
#         # pc端百度
#         if str(self.search) == '1':
#             resultObj = self.baiduShouLuPC(self.lianjie)
#         # 移动端百度
#         elif str(self.search) == '4':
#             resultObj = self.baiduShouLuMobeil(self.lianjie)
#         # pc360
#         elif str(self.search) == '3':
#             resultObj = self.pcShoulu360(self.lianjie)
#         # 移动端360
#         elif str(self.search) == '6':
#             resultObj = self.mobielShoulu360(self.lianjie)
#         data_dict = {
#             'tid':self.tid,
#             'resultObj':resultObj
#         }
#         return data_dict
# class shouluChaXun():
#     def __init__(self):
#         pass
#
#     # 获取任务
#     def shouLuHuoQuRenWu(self):
#         # url = 'http://api.zhugeyingxiao.com/zhugedanao/shouluHuoQuRenWu'
#         url = 'http://127.0.0.1:8000/zhugedanao/shouluHuoQuRenWu'
#         ret = requests.get(url)
#         result = json.loads(ret.text)
#         print('获取收录任务-------------> ',result['data'])
#         return result
#
#     # 返回数据
#     def shouLuReturnsTheResult(self, data_dict):
#         print('resultObj_-------->',data_dict)
#         shoulu = data_dict['resultObj']['shoulu'],
#         title = data_dict['resultObj']['title'],
#         kuaizhao = data_dict['resultObj']['kuaizhao_time'],
#         status_code = data_dict['resultObj']['status_code'],
#         o_id = data_dict['tid'],
#         # url = 'http://api.zhugeyingxiao.com/zhugedanao/shouluTiJiaoRenWu'
#         content_dict = {
#             'o_id' : o_id,
#             'title' : title,
#             'kuaizhao_time' : kuaizhao,
#             'status_code' : status_code,
#             'is_shoulu' : shoulu,
#         }
#         url = 'http://127.0.0.1:8000/zhugedanao/shouluTiJiaoRenWu'
#         requests.post(url, data=content_dict)
#
#     # 开始
#     def start(self):
#         result = self.shouLuHuoQuRenWu()
#         lianjie = result['data']['url']
#         tid = result['data']['o_id']
#         search = result['data']['search']
#         result = shouLuPcChongCha(lianjie, tid, search)
#         data_dict = result.judgmentSearchEngine()
#         self.shouLuReturnsTheResult(data_dict)
#
#     def main(self):
#         # print("-" * 20 + "> 开始任务")
#         # self.adsl.reconnect()
#         # try:
#         #     self.accountApiOper.vpsServerQiandao()
#         # except requests_ConnectionError:
#         #     pass
#
#         self.start()
# # if __name__ == '__main__':
# #     objs = shouluChaXun()
# #     objs.main()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # 链接提交 收录查询
#
#
#
#
# class lianjieshoulu():
#
#     def getPageInfo(self, url):
#         headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)]}
#         try:
#             ret_two = requests.get(url, headers=headers, timeout=10)
#             ret_two_url = ret_two.url
#             status_code = ret_two.status_code
#             encode_ret = ret_two.apparent_encoding
#             if encode_ret == 'GB2312':
#                 ret_two.encoding = 'gbk'
#             else:
#                 ret_two.encoding = 'utf-8'
#             soup_two = BeautifulSoup(ret_two.text, 'lxml')
#             try:
#                 title = soup_two.find('title').get_text().strip().replace('\r\n', '')
#             except AttributeError:
#                 title = ''
#         # except ConnectionError:
#         except:
#             pass
#             status_code = 500
#             title = ''
#             ret_two_url = ''
#         return status_code, title, ret_two_url
#
#     # 百度pc端收录查询
#     def baiduShouLuPC(self, domain):
#         resultObj = {
#             "shoulu": 0,
#             "kuaizhao_time": '',
#             "title": '',
#             "status_code": ''
#         }
#         domain = domain.strip()
#         zhidao_url = 'http://www.baidu.com/s?wd={domain}'.format(domain=domain)
#         headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)]}
#         ret_domain = requests.get(zhidao_url, headers=headers, timeout=10)
#         soup_domain = BeautifulSoup(ret_domain.text, 'lxml')
#         if soup_domain.find('div', class_='content_none'):
#             resultObj["status_code"] = ret_domain.status_code
#         else:
#             div_tags = soup_domain.find_all('div', class_='result c-container ')
#             if div_tags and div_tags[0].attrs.get('id'):
#                 panduan_url = div_tags[0].find('a').attrs['href']
#                 f13_div = div_tags[0].find('div', class_='f13')
#                 if f13_div.find('a'):
#                     yuming = f13_div.find('a').get_text()[:-5].split('/')[0]  # 获取域名
#                     status_code, title, ret_two_url = self.getPageInfo(panduan_url)
#                     resultObj["title"] = title
#                     resultObj["status_code"] = status_code
#                     if div_tags[0].find('span', class_='newTimeFactor_before_abs'):
#                         resultObj["kuaizhao_time"] = div_tags[0].find('span',
#                             class_='newTimeFactor_before_abs').get_text().strip().replace('-', '').replace('年',
#                             '-').replace('月', '-').replace('日', '').strip()
#                     if yuming in domain:
#                         if domain in ret_two_url:
#                             resultObj["shoulu"] = 1
#         return resultObj
#
#     # 百度移动端收录查询
#     def baiduShouLuMobeil(self, domain):
#         resultObj = {
#             "shoulu": 0,
#             "kuaizhao_time": '',
#             "title": '',
#             "status_code": ''
#         }
#         domain = domain.strip()
#         zhidao_url = 'https://m.baidu.com/from=844b/pu=sz@1320_2001/s?tn=iphone&usm=2&word={}'.format(domain)
#         headers = {
#             'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
#         ret_domain = requests.get(zhidao_url, headers=headers, timeout=10)
#         soup_domain = BeautifulSoup(ret_domain.text, 'lxml')
#         if not soup_domain.find_all('div', class_='result c-result'):
#             resultObj["status_code"] = ret_domain.status_code
#         else:
#             div_tags = soup_domain.find_all('div', class_='result c-result')
#             if div_tags:
#                 dict_data_clog = eval(div_tags[0].attrs.get('data-log'))
#                 url = dict_data_clog['mu']
#                 if url.strip():
#                     status_code, title, ret_two_url = self.getPageInfo(url)
#                     resultObj["status_code"] = status_code
#                     resultObj["title"] = title
#                     if domain == url or url[:-1] == domain:
#                         resultObj["shoulu"] = 1
#         return resultObj
#
#     # 链接收录查询
#     def lianjieshouluchauxn(self):
#         url = 'http://api.zhugeyingxiao.com/zhugedanao/linksToSubmitShouLu '
#         # url = 'http://127.0.0.1:8000/zhugedanao/linksToSubmitShouLu '
#         ret = requests.get(url)
#         json_data = json.loads(ret.text)['data']
#         if json_data:
#             resultObjPc = self.baiduShouLuPC(json_data['url'])
#             # resultObjPc = self.baiduShouLuPC(ppp)
#             if resultObjPc['shoulu'] != 0:
#                 is_shoulu = int(resultObjPc['shoulu'])
#             else:
#                 resultObjMobiel = self.baiduShouLuMobeil(json_data['url'])
#                 # resultObjMobiel = self.baiduShouLuMobeil(ppp)
#                 is_shoulu = int(resultObjMobiel['shoulu'])
#
#             print(is_shoulu, type(is_shoulu))
#             shoulu = 3
#             if is_shoulu == 1:
#                 shoulu = 2
#
#             data_dict = {
#                 'o_id':json_data['o_id'],
#                 'is_shoulu':shoulu
#             }
#             print('返回数据 ------data_dict---> ', data_dict)
#             fanhui_url = 'http://127.0.0.1:8000/zhugedanao/linksShouLuReturnData'
#             requests.post(fanhui_url, data=data_dict)

# if __name__ == '__main__':
#     obj = lianjieshoulu()
#     obj.lianjieshouluchauxn()






from bs4 import BeautifulSoup
import requests, json, random
import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))
print("sys.path -->", sys.path)
from urllib import parse


# 收录查询

class shouLuPcChongCha():
    def __init__(self,lianjie, tid, search):
        self.lianjie = lianjie
        self.tid = tid
        self.search = search

    # 获取页面访问状态和标题
    def getPageInfo(self, url):
        headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)]}
        try:
            ret_two = requests.get(url, headers=headers, timeout=10)
            ret_two_url = ret_two.url
            status_code = ret_two.status_code
            encode_ret = ret_two.apparent_encoding
            if encode_ret == 'GB2312':
                ret_two.encoding = 'gbk'
            else:
                ret_two.encoding = 'utf-8'
            soup_two = BeautifulSoup(ret_two.text, 'lxml')
            try:
                title = soup_two.find('title').get_text().strip().replace('\r\n', '')
            except AttributeError:
                title = ''
        # except ConnectionError:
        except:
            pass
            status_code = 500
            title = ''
            ret_two_url = ''
        return status_code, title, ret_two_url

    # 百度pc端收录查询
    def baiduShouLuPC(self, domain):
        resultObj = {
            "shoulu": 0,
            "kuaizhao_time": '',
            "title": '',
            "status_code": ''
        }
        # 编码成url格式
        domain = parse.quote_plus(domain.strip())
        zhidao_url = 'http://www.baidu.com/s?wd={domain}'.format(domain=domain)
        headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)]}
        ret_domain = requests.get(zhidao_url, headers=headers, timeout=10)
        soup_domain = BeautifulSoup(ret_domain.text, 'lxml')
        if soup_domain.find('div', class_='content_none'):
            resultObj["status_code"] = ret_domain.status_code
        else:
            div_tags = soup_domain.find_all('div', class_='result c-container ')
            if div_tags and div_tags[0].attrs.get('id'):
                panduan_url = div_tags[0].find('a')['href']
                f13_div = div_tags[0].find('div', class_='f13')
                status_code, title, ret_two_url = self.getPageInfo(panduan_url)
                # 解码
                domain = parse.unquote_plus(domain)
                if domain in ret_two_url or domain == ret_two_url:
                    if f13_div.find('a'):
                        resultObj["shoulu"] = 1
                        resultObj["title"] = title
                        resultObj["status_code"] = status_code
                        if div_tags[0].find('span', class_='newTimeFactor_before_abs'):
                            resultObj["kuaizhao_time"] = div_tags[0].find('span',
                                class_='newTimeFactor_before_abs').get_text().strip().replace('-', '').replace('年',
                                '-').replace('月', '-').replace('日', '').strip()
                else:
                    status_code, title, ret_two_url = self.getPageInfo(domain)
                    resultObj["title"] = title
                    resultObj["status_code"] = status_code
                    resultObj["shoulu"] = 0
        return resultObj

    # 百度移动端收录查询
    def baiduShouLuMobeil(self, domain):
        resultObj = {
            "shoulu": 0,
            "kuaizhao_time": '',
            "title": '',
            "status_code": ''
        }
        # 编码成url格式
        domain = parse.quote_plus(domain.strip())
        zhidao_url = 'https://m.baidu.com/from=844b/pu=sz@1320_2001/s?tn=iphone&usm=2&word={}'.format(domain)
        headers = {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
        ret_domain = requests.get(zhidao_url, headers=headers, timeout=10)
        print('zhidao_url=======> ', zhidao_url)

        soup_domain = BeautifulSoup(ret_domain.text, 'lxml')
        if not soup_domain.find_all('div', class_='result c-result'):
            resultObj["status_code"] = ret_domain.status_code
        else:
            div_tags = soup_domain.find_all('div', class_='result c-result')
            if div_tags:
                dict_data_clog = eval(div_tags[0].attrs.get('data-log'))
                url = dict_data_clog['mu']
                if url.strip():
                    status_code, title, ret_two_url = self.getPageInfo(url)
                    # 解码
                    domain_jiema = parse.unquote_plus(domain)
                    print(domain_jiema, ret_two_url)
                    if domain_jiema == ret_two_url or domain_jiema in ret_two_url:
                        resultObj["status_code"] = status_code
                        resultObj["title"] = title
                        resultObj["shoulu"] = 1
                    else:
                        status_code, title, ret_two_url = self.getPageInfo(domain_jiema)
                        resultObj["status_code"] = status_code
                        resultObj["title"] = title
                        resultObj["shoulu"] = 0
        return resultObj

    # 360pc端收录查询
    def pcShoulu360(self, domain):
        resultObj = {
            "shoulu": 0,
            "kuaizhao_time": '',
            "title": '',
            "status_code": '',
            "rank_num": 0
        }
        # 编码成url格式
        domain = parse.quote_plus(domain.strip())
        headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)]}
        pc_360url = 'https://so.com/s?src=3600w&q={domain}'.format(domain=domain)
        ret_domain = requests.get(pc_360url, headers=headers, timeout=10)
        print('pc_360url============> ', pc_360url)
        soup = BeautifulSoup(ret_domain.text, 'lxml')
        if soup.find('div', class_='so-toptip'):
            resultObj['shoulu'] = '0'
            resultObj["status_code"] = ret_domain.status_code
        else:
            li_tags = soup.find_all('li', class_='res-list')
            if len(li_tags) > 0:
                zongti_xinxi = li_tags[0].find('a', target='_blank')  # 获取order -- title -- title_url
                yuming_canshu = li_tags[0].find('p', class_='res-linkinfo')  # 域名参数
                if li_tags[0].find('a').attrs.get('data-url'):
                    data_url = li_tags[0].find('a').attrs.get('data-url')
                else:
                    data_url = zongti_xinxi.attrs['href']
                status_code, title, ret_two_url = self.getPageInfo(data_url)
                # 解码
                domain_jiema = parse.unquote_plus(domain)
                print(domain_jiema, ret_two_url)
                if domain_jiema in ret_two_url or domain_jiema == ret_two_url:
                    resultObj["status_code"] = status_code
                    resultObj["title"] = title
                    resultObj['shoulu'] = '1'
                else:
                    status_code, title, ret_two_url = self.getPageInfo(domain_jiema)
                    resultObj["status_code"] = status_code
                    resultObj["title"] = title
                    resultObj['shoulu'] = '0'
        return resultObj

    # 360移动端收录查询
    def mobielShoulu360(self, domain):
        resultObj = {
            "shoulu": 0,
            "kuaizhao_time": '',
            "title": '',
            "status_code": '',
            "rank_num": 0
        }
        # 编码成url格式
        domain = parse.quote_plus(domain.strip())
        PC_360_url = 'https://m.so.com/s?src=3600w&q={}'.format(domain)
        print('PC_360_url------> ', PC_360_url)
        headers = {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
        ret = requests.get(PC_360_url, headers=headers, timeout=10)
        soup = BeautifulSoup(ret.text, 'lxml')
        if soup.find('div', class_='mso-url2link'):
            resultObj['shoulu'] = '0'
            resultObj["status_code"] = ret.status_code
        else:
            div_tags = soup.find_all('div', class_=' g-card res-list og ')
            if len(div_tags) > 0:
                url_data = div_tags[0].attrs.get('data-pcurl')
                status_code, title, ret_two_url = self.getPageInfo(url_data)
                # 解码
                domain = parse.unquote_plus(domain)
                if domain in ret_two_url or ret_two_url == domain:
                    resultObj["status_code"] = status_code
                    resultObj["title"] = title
                    resultObj['shoulu'] = '1'
                else:
                    status_code, title, ret_two_url = self.getPageInfo(domain)
                    resultObj["status_code"] = status_code
                    resultObj["title"] = title
                    resultObj['shoulu'] = '0'
        return resultObj

    # 判断搜索引擎
    def judgmentSearchEngine(self):
        resultObj = {}
        # pc端百度
        if str(self.search) == '1':
            resultObj = self.baiduShouLuPC(self.lianjie)
        # 移动端百度
        elif str(self.search) == '4':
            resultObj = self.baiduShouLuMobeil(self.lianjie)
        # pc360
        elif str(self.search) == '3':
            resultObj = self.pcShoulu360(self.lianjie)
        # 移动端360
        elif str(self.search) == '6':
            resultObj = self.mobielShoulu360(self.lianjie)

        if resultObj:
            data_dict = {
                'tid':self.tid,
                'resultObj':resultObj
            }
            return data_dict
class shouluChaXun():
    def __init__(self):
        self.apiHost = 'http://websiteaccount.bjhzkq.com/api/'

    # 获取任务
    def shouLuHuoQuRenWu(self):
        url = 'http://api.zhugeyingxiao.com/zhugedanao/shouluHuoQuRenWu'
        # url = 'http://127.0.0.1:8000/zhugedanao/shouluHuoQuRenWu'
        ret = requests.get(url)
        result = json.loads(ret.text)
        print('获取收录任务-------------> ',result['data'])
        return result

    # 返回数据
    def shouLuReturnsTheResult(self, data_dict):
        print('resultObj_-------->',data_dict)
        shoulu = data_dict['resultObj']['shoulu'],
        title = data_dict['resultObj']['title'],
        kuaizhao = data_dict['resultObj']['kuaizhao_time'],
        status_code = data_dict['resultObj']['status_code'],
        o_id = data_dict['tid'],
        content_dict = {
            'o_id' : o_id,
            'title' : title,
            'kuaizhao_time' : kuaizhao,
            'status_code' : status_code,
            'is_shoulu' : shoulu,
        }
        # url = 'http://api.zhugeyingxiao.com/zhugedanao/shouluTiJiaoRenWu'
        url = 'http://127.0.0.1:8000/zhugedanao/shouluTiJiaoRenWu'
        requests.post(url, data=content_dict)

    # 开始
    def start(self):
        result = self.shouLuHuoQuRenWu()
        if result['data']:
            lianjie = result['data']['url']
            tid = result['data']['o_id']
            search = result['data']['search']
            result = shouLuPcChongCha(lianjie, tid, search)
            data_dict = result.judgmentSearchEngine()
            self.shouLuReturnsTheResult(data_dict)
        else:
            return

# if __name__ == '__main__':
#     objs = shouluChaXun()
#     objs.start()




class fugaipc_chaxun():
    def __init__(self, search, keyword, mohu_pipei):
        self.search = search
        self.keyword = keyword
        self.mohu_pipei = mohu_pipei

    # 百度pc端覆盖查询
    def baiduFuGaiPC(self):
        order_list = []
        headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)], }
        zhidao_url = 'https://www.baidu.com/s?wd={keyword}'.format(keyword=self.keyword)
        # print('-=---------->', zhidao_url)
        ret = requests.get(zhidao_url, headers=headers, timeout=10)
        soup = BeautifulSoup(ret.text, 'lxml')
        div_tags = soup.find_all('div', class_='result c-container ')
        for mohu_pipei in self.mohu_pipei.split(','):
            print('mohu_pipei===> ',mohu_pipei)
            for div_tag in div_tags:
                rank_num = div_tag.attrs.get('id')
                if not rank_num:
                    continue
                tiaojian_chaxun = div_tag.get_text()
                panduan_url = div_tag.find('h3', class_='t').find('a').attrs['href']
                title = div_tag.find('h3', class_='t').get_text()
                # print('tiaojian_chaxun-------> ', mohu_pipei, tiaojian_chaxun)
                if mohu_pipei in tiaojian_chaxun:  # 表示有覆盖
                    order_num = int(rank_num)
                    order_list.append({
                        'paiming': order_num,
                        'title': title,
                        'title_url': panduan_url,
                        'sousuo_guize': mohu_pipei,
                        'search':self.search
                    })
        return order_list

    # 百度移动端覆盖查询
    def baiduFuGaiMOBIEL(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
        zhidao_url = 'https://m.baidu.com/s?word={}'.format(self.keyword)
        ret = requests.get(zhidao_url, headers=headers, timeout=10)
        soup_browser = BeautifulSoup(ret.text, 'lxml')
        content_list_order = []
        div_tags = soup_browser.find_all('div', class_='result c-result')
        for div_tag in div_tags:
            content_list_order.append(div_tag)
        div_tags = soup_browser.find_all('div', class_='result c-result c-clk-recommend')
        for div_tag in div_tags:
            content_list_order.append(div_tag)
        order_list = []
        for mohu_pipei in self.mohu_pipei.split(','):
            for data in content_list_order:
                if data['data-log']:
                    dict_data = eval(data['data-log'])
                    url_title = dict_data['mu']  # 标题链接
                    order = dict_data['order']  # 排名
                    pipei_tiaojian = data.get_text()
                    if mohu_pipei in pipei_tiaojian:
                        if data.find('div', class_='c-container').find('a'):
                            title = data.find('div', class_='c-container').find('a').get_text()
                            order_num = int(order)
                            order_list.append({
                                'paiming': order_num,
                                'title': title,
                                'title_url': url_title,
                                'sousuo_guize': mohu_pipei,
                                'search': self.search
                            })
        return order_list

    # 360pc端覆盖查询
    def pcFugai360(self):
        order_list = []
        headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)], }
        pc_360url = 'https://so.com/s?src=3600w&q={keyword}'.format(keyword=self.keyword)
        print('pc_360url--------->', pc_360url)
        ret = requests.get(pc_360url, headers=headers, timeout=10)
        soup = BeautifulSoup(ret.text, 'lxml')
        div_tags = soup.find_all('li', class_='res-list')
        for mohu_pipei in self.mohu_pipei.split(','):
            for div_tag in div_tags:
                zongti_fugai = div_tag.get_text()
                if mohu_pipei in zongti_fugai:
                    if div_tag.find('a').attrs.get('data-res'):
                        data_res = div_tag.find('a')
                        paiming = data_res.attrs.get('data-res')
                        dict_data_res = json.loads(paiming)
                        panduan_url = data_res.attrs['href']
                        title = data_res.get_text()
                        order_num = int(dict_data_res['pos'])
                        order_list.append({
                            'paiming': order_num,
                            'title': title,
                            'title_url': panduan_url,
                            'sousuo_guize': mohu_pipei,
                            'search': self.search
                        })
        print('rentur')
        return order_list

    # 360移动端覆盖查询
    def mobielFugai360(self):
        PC_360_url = 'https://m.so.com/s?src=3600w&q={}'.format(self.keyword)
        order_list = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
        ret = requests.get(PC_360_url, headers=headers, timeout=10)
        soup_browser = BeautifulSoup(ret.text, 'lxml')
        div_tags = soup_browser.find_all('div', class_=" g-card res-list og ")
        order = 0
        for mohu_pipei in self.mohu_pipei.split(','):
            for div_tag in div_tags:
                order += 1
                zongti_fugai = div_tag.get_text()
                if mohu_pipei in zongti_fugai:
                    a_tag = div_tag.find('a', class_='alink')
                    title = a_tag.find('h3').get_text()
                    panduan_url = a_tag.attrs['href']
                    order_num = int(order)
                    order_list.append({
                        'paiming': order_num,
                        'title': title,
                        'title_url': panduan_url,
                        'sousuo_guize': mohu_pipei,
                        'search': self.search
                    })
        return order_list


    def qufenyinqing(self):
        # print('search -------- > ',self.search)
        if str(self.search) == '1':
            print('pc端 -- 覆盖百度')
            resultObj = self.baiduFuGaiPC()
            # 移动端百度
        elif str(self.search) == '4':
            print('移动端 -- 覆盖百度')
            resultObj = self.baiduFuGaiMOBIEL()
            # pc360
        elif str(self.search) == '3':
            print('pc端 -- 覆盖360')
            resultObj = self.pcFugai360()
            # # 移动端360
        elif str(self.search) == '6':
            print('移动端 -- 覆盖360 ')
            resultObj = self.mobielFugai360()
        # print('resultObj-------> ',resultObj)
        return resultObj

class fugaichaxun():
    def __init__(self):
        pass

    def huoqurenwu(self):
        url = 'http://127.0.0.1:8000/zhugedanao/fuGaiHuoQuRenWu'
        # url = 'http://api.zhugeyingxiao.com/zhugedanao/fuGaiHuoQuRenWu'
        ret = requests.get(url)
        if ret.text:
            ret_text = json.loads(ret.text)
            return ret_text

    # 开始
    def start(self):
        ret_text = self.huoqurenwu()
        print('ret_text-> ',ret_text)
        if ret_text['code'] == 200:
            o_id = ret_text['data']['o_id']
            search = ret_text['data']['search']
            keyword = ret_text['data']['keyword']
            tiaojian = ret_text['data']['tiaojian']
            # print('-----> ',o_id, search, keyword, tiaojian)
            obj = fugaipc_chaxun(search, keyword, eval(tiaojian))
            resultObj = obj.qufenyinqing()
            if resultObj:
                data_list = {
                    "search":search,
                    "keyword":keyword,
                    "o_id":o_id,
                    "resultObj":json.dumps(resultObj)
                }
                print(data_list)
                url = 'http://127.0.0.1:8000/zhugedanao/fuGaiTiJiaoRenWu'
                # url = 'http://api.zhugeyingxiao.com/zhugedanao/fuGaiTiJiaoRenWu'
                requests.post(url, data=data_list)

# if __name__ == '__main__':
#     obj = fugaichaxun()
#     obj.start()








import datetime


class zhongdianci_chaxun():
    def __init__(self, lianjie, detail_id, keywords, domain, search_engine):
        self.detail_id = detail_id
        self.keywords = keywords
        self.domain = domain
        self.lianjie = lianjie
        self.headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)]}
        self.search = str(search_engine)

    # 获取页面访问状态和标题
    def getPageInfo(self, url):
        headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)]}
        try:
            ret_two = requests.get(url, headers=headers, timeout=10)
            ret_two_url = ret_two.url
            status_code = ret_two.status_code
            encode_ret = ret_two.apparent_encoding
            if encode_ret == 'GB2312':
                ret_two.encoding = 'gbk'
            else:
                ret_two.encoding = 'utf-8'
            soup_two = BeautifulSoup(ret_two.text, 'lxml')
            try:
                title = soup_two.find('title').get_text().strip().replace('\r\n', '')
            except AttributeError:
                title = ''
        except:
            pass
            status_code = 500
            title = ''
            ret_two_url = ''
        return status_code, title, ret_two_url

        # 百度pc端收录查询
    def baiduShouLuPC(self, domain):
        resultObj = {
            "shoulu": 0,
            "kuaizhao_time": '',
            "title": '',
            "status_code": ''
        }
        # 编码成url格式
        domain = parse.quote_plus(domain.strip())
        zhidao_url = 'http://www.baidu.com/s?wd={domain}'.format(domain=domain)
        headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)]}
        ret_domain = requests.get(zhidao_url, headers=headers, timeout=10)
        soup_domain = BeautifulSoup(ret_domain.text, 'lxml')
        if soup_domain.find('div', class_='content_none'):
            resultObj["status_code"] = ret_domain.status_code
        else:
            div_tags = soup_domain.find_all('div', class_='result c-container ')
            if div_tags and div_tags[0].attrs.get('id'):
                panduan_url = div_tags[0].find('a')['href']
                f13_div = div_tags[0].find('div', class_='f13')
                status_code, title, ret_two_url = self.getPageInfo(panduan_url)
                # 解码
                domain = parse.unquote_plus(domain)
                if domain in ret_two_url or domain == ret_two_url:
                    if f13_div.find('a'):
                        resultObj["title"] = title
                        resultObj["status_code"] = status_code
                        resultObj["shoulu"] = 1
                else:
                    status_code, title, ret_two_url = self.getPageInfo(domain)
                    resultObj["title"] = title
                    resultObj["status_code"] = status_code
                    resultObj["shoulu"] = 0
                if div_tags[0].find('span', class_='newTimeFactor_before_abs'):
                    resultObj["kuaizhao_time"] = div_tags[0].find('span',
                        class_='newTimeFactor_before_abs').get_text().strip().replace('-', '').replace('年',
                        '-').replace('月', '-').replace('日', '').strip()
        return resultObj

        # 百度移动端收录查询
    def baiduShouLuMobeil(self, domain):
        resultObj = {
            "shoulu": 0,
            "kuaizhao_time": '',
            "title": '',
            "status_code": ''
        }
        # 编码成url格式
        domain = parse.quote_plus(domain.strip())
        zhidao_url = 'https://m.baidu.com/from=844b/pu=sz@1320_2001/s?tn=iphone&usm=2&word={}'.format(domain)
        headers = {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
        ret_domain = requests.get(zhidao_url, headers=headers, timeout=10)
        print('zhidao_url=======> ', zhidao_url)

        soup_domain = BeautifulSoup(ret_domain.text, 'lxml')
        if not soup_domain.find_all('div', class_='result c-result'):
            resultObj["status_code"] = ret_domain.status_code
        else:
            div_tags = soup_domain.find_all('div', class_='result c-result')
            if div_tags:
                dict_data_clog = eval(div_tags[0].attrs.get('data-log'))
                url = dict_data_clog['mu']
                if url.strip():
                    status_code, title, ret_two_url = self.getPageInfo(url)
                    # 解码
                    domain_jiema = parse.unquote_plus(domain)
                    print(domain_jiema, ret_two_url)
                    if domain_jiema == ret_two_url or domain_jiema in ret_two_url:
                        resultObj["status_code"] = status_code
                        resultObj["title"] = title
                        resultObj["shoulu"] = 1
                    else:
                        status_code, title, ret_two_url = self.getPageInfo(domain_jiema)
                        resultObj["status_code"] = status_code
                        resultObj["title"] = title
                        resultObj["shoulu"] = 0
        return resultObj

        # 360pc端收录查询
    def pcShoulu360(self, domain):
        resultObj = {
            "shoulu": 0,
            "kuaizhao_time": '',
            "title": '',
            "status_code": '',
            "rank_num": 0
        }
        # 编码成url格式
        domain = parse.quote_plus(domain.strip())
        headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)]}
        pc_360url = 'https://so.com/s?src=3600w&q={domain}'.format(domain=domain)
        ret_domain = requests.get(pc_360url, headers=headers, timeout=10)
        print('pc_360url============> ', pc_360url)
        soup = BeautifulSoup(ret_domain.text, 'lxml')
        if soup.find('div', class_='so-toptip'):
            resultObj['shoulu'] = '0'
            resultObj["status_code"] = ret_domain.status_code
        else:
            li_tags = soup.find_all('li', class_='res-list')
            if len(li_tags) > 0:
                zongti_xinxi = li_tags[0].find('a', target='_blank')  # 获取order -- title -- title_url
                yuming_canshu = li_tags[0].find('p', class_='res-linkinfo')  # 域名参数
                if li_tags[0].find('a').attrs.get('data-url'):
                    data_url = li_tags[0].find('a').attrs.get('data-url')
                else:
                    data_url = zongti_xinxi.attrs['href']
                status_code, title, ret_two_url = self.getPageInfo(data_url)
                # 解码
                domain_jiema = parse.unquote_plus(domain)
                print(domain_jiema, ret_two_url)
                if domain_jiema in ret_two_url or domain_jiema == ret_two_url:
                    resultObj["status_code"] = status_code
                    resultObj["title"] = title
                    resultObj['shoulu'] = '1'
                else:
                    status_code, title, ret_two_url = self.getPageInfo(domain_jiema)
                    resultObj["status_code"] = status_code
                    resultObj["title"] = title
                    resultObj['shoulu'] = '0'
        return resultObj

        # 360移动端收录查询
    def mobielShoulu360(self, domain):
        resultObj = {
            "shoulu": 0,
            "kuaizhao_time": '',
            "title": '',
            "status_code": '',
            "rank_num": 0
        }
        # 编码成url格式
        domain = parse.quote_plus(domain.strip())
        PC_360_url = 'https://m.so.com/s?src=3600w&q={}'.format(domain)
        print('PC_360_url------> ', PC_360_url)
        headers = {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
        ret = requests.get(PC_360_url, headers=headers, timeout=10)
        soup = BeautifulSoup(ret.text, 'lxml')
        if soup.find('div', class_='mso-url2link'):
            resultObj['shoulu'] = '0'
            resultObj["status_code"] = ret.status_code
        else:
            div_tags = soup.find_all('div', class_=' g-card res-list og ')
            if len(div_tags) > 0:
                url_data = div_tags[0].attrs.get('data-pcurl')
                status_code, title, ret_two_url = self.getPageInfo(url_data)
                # 解码
                domain = parse.unquote_plus(domain)
                if domain in ret_two_url or ret_two_url == domain:
                    resultObj["status_code"] = status_code
                    resultObj["title"] = title
                    resultObj['shoulu'] = '1'
                else:
                    status_code, title, ret_two_url = self.getPageInfo(domain)
                    resultObj["status_code"] = status_code
                    resultObj["title"] = title
                    resultObj['shoulu'] = '0'
        return resultObj

    # 百度pc端覆盖查询
    # def baiduFuGaiPC(self, keyword, mohu_pipei_list):
    #     order_list = []
    #     headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)], }
    #     zhidao_url = 'https://www.baidu.com/s?wd={keyword}'.format(keyword=keyword)
    #     ret = requests.get(zhidao_url, headers=headers, timeout=10)
    #     soup = BeautifulSoup(ret.text, 'lxml')
    #     div_tags = soup.find_all('div', class_='result c-container ')
    #     for mohu_pipei in mohu_pipei_list.split(','):
    #         for div_tag in div_tags:
    #             rank_num = div_tag.attrs.get('id')
    #             if not rank_num:
    #                 continue
    #             tiaojian_chaxun = div_tag.get_text()
    #             panduan_url = div_tag.find('h3', class_='t').find('a').attrs['href']
    #             title = div_tag.find('h3', class_='t').get_text()
    #             if mohu_pipei in tiaojian_chaxun:  # 表示有覆盖
    #                 order_num = int(rank_num)
    #                 order_list.append({
    #                     'paiming': order_num,
    #                     'title': title,
    #                     'title_url': panduan_url,
    #                     'sousuo_guize': mohu_pipei,
    #                 })
    #     return order_list
    # # 百度移动端覆盖查询
    # def baiduFuGaiMOBIEL(self, keyword, mohu_pipei_list):
    #     headers = {
    #         'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
    #     zhidao_url = 'https://m.baidu.com/s?word={}'.format(keyword)
    #     ret = requests.get(zhidao_url, headers=headers, timeout=10)
    #     soup_browser = BeautifulSoup(ret.text, 'lxml')
    #     content_list_order = []
    #     div_tags = soup_browser.find_all('div', class_='result c-result')
    #     for div_tag in div_tags:
    #         content_list_order.append(div_tag)
    #     div_tags = soup_browser.find_all('div', class_='result c-result c-clk-recommend')
    #     for div_tag in div_tags:
    #         content_list_order.append(div_tag)
    #     order_list = []
    #     for mohu_pipei in mohu_pipei_list.split(','):
    #         for data in content_list_order:
    #             if data['data-log']:
    #                 dict_data = eval(data['data-log'])
    #                 url_title = dict_data['mu']  # 标题链接
    #                 order = dict_data['order']  # 排名
    #                 pipei_tiaojian = data.get_text()
    #                 if mohu_pipei in pipei_tiaojian:
    #                     if data.find('div', class_='c-container').find('a'):
    #                         title = data.find('div', class_='c-container').find('a').get_text()
    #                         order_num = int(order)
    #                         order_list.append({
    #                             'paiming': order_num,
    #                             'title': title,
    #                             'title_url': url_title,
    #                             'sousuo_guize': mohu_pipei,
    #                         })
    #     return order_list
    # # 360pc端覆盖查询
    # def pcFugai360(self, keyword, mohu_pipei_list):
    #     order_list = []
    #     headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)], }
    #     pc_360url = 'https://so.com/s?src=3600w&q={keyword}'.format(keyword=keyword)
    #     ret = requests.get(pc_360url, headers=headers, timeout=10)
    #     soup = BeautifulSoup(ret.text, 'lxml')
    #     div_tags = soup.find_all('li', class_='res-list')
    #     for mohu_pipei in mohu_pipei_list.split(','):
    #         for div_tag in div_tags:
    #             zongti_fugai = div_tag.get_text()
    #             if mohu_pipei in zongti_fugai:
    #                 if div_tag.find('a').attrs.get('data-res'):
    #                     data_res = div_tag.find('a')
    #                     paiming = data_res.attrs.get('data-res')
    #                     dict_data_res = json.loads(paiming)
    #                     panduan_url = data_res.attrs['href']
    #                     title = data_res.get_text()
    #                     order_num = int(dict_data_res['pos'])
    #                     order_list.append({
    #                         'paiming': order_num,
    #                         'title': title,
    #                         'title_url': panduan_url,
    #                         'sousuo_guize': mohu_pipei,
    #                     })
    #     return order_list
    # # 360移动端覆盖查询
    # def mobielFugai360(self, keyword, mohu_pipei_list):
    #     PC_360_url = 'https://m.so.com/s?src=3600w&q={}'.format(keyword)
    #     order_list = []
    #     headers = {
    #         'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
    #     ret = requests.get(PC_360_url, headers=headers, timeout=10)
    #     soup_browser = BeautifulSoup(ret.text, 'lxml')
    #     div_tags = soup_browser.find_all('div', class_=" g-card res-list og ")
    #     order = 0
    #     for mohu_pipei in mohu_pipei_list.split(','):
    #         for div_tag in div_tags:
    #             order += 1
    #             zongti_fugai = div_tag.get_text()
    #             if mohu_pipei in zongti_fugai:
    #                 a_tag = div_tag.find('a', class_='alink')
    #                 title = a_tag.find('h3').get_text()
    #                 panduan_url = a_tag.attrs['href']
    #                 order_num = int(order)
    #                 order_list.append({
    #                     'paiming': order_num,
    #                     'title': title,
    #                     'title_url': panduan_url,
    #                     'sousuo_guize': mohu_pipei,
    #                 })
    #     return order_list

    def Baidu_Zhidao_URL_PC(self):
        # 调用查询收录
        rank_num = 0
        zhidao_url = 'https://www.baidu.com/s?wd={}'
        resultObj = self.baiduShouLuPC(self.lianjie)
        print(self.lianjie)
        if resultObj['shoulu'] == 1:
            print('zhidao_url-------> ',zhidao_url.format(self.keywords))
            ret = requests.get(zhidao_url.format(self.keywords), headers=self.headers, timeout=10)
            soup = BeautifulSoup(ret.text, 'lxml')
            # try:
            div_tags = soup.find_all('div', class_='result c-container ')
            for div_tag in div_tags:
                if div_tags and div_tag.attrs.get('id'):
                    panduan_url = div_tag.find('a').attrs['href']
                    ret_two_url = requests.get(panduan_url, headers=self.headers, timeout=10)
                    print(self.lianjie, 'ret_two_url--->', ret_two_url.url)
                    print('self.lianjie---> ',self.lianjie)
                    if self.lianjie in ret_two_url.url or self.lianjie == ret_two_url:
                        rank_num = div_tag.attrs.get('id')
                        print('rank_num========> ',rank_num)
                        break
                        # div_13 = div_tag.find('div', class_='f13')
                        # print('div_13=========> ',div_13)
                        # if div_13:
                        #     if div_13.find('a'):
            # except Exception:
            #     pass
        data_list = {
            'order': int(rank_num),
            'shoulu': resultObj['shoulu']
        }
        return data_list
    def Baidu_Zhidao_URL_MOBILE(self):
        shoulu = ''
        paiming_order = '0'
        headers = {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
        resultObj = self.baiduShouLuMobeil(self.lianjie)
        if resultObj['shoulu'] == 1:
            zhidao_url = 'https://m.baidu.com/from=844b/pu=sz@1320_2001/s?tn=iphone&usm=2&word={}'
            url = zhidao_url.format(self.keywords)
            ret_two = requests.get(url, headers=headers, timeout=10)
            soup_two = BeautifulSoup(ret_two.text, 'lxml')
            content_list_order = []
            div_tags = soup_two.find_all('div', class_='result c-result')
            for div_tag in div_tags:
                content_list_order.append(div_tag)
            div_tags = soup_two.find_all('div', class_='result c-result c-clk-recommend')
            for div_tag in div_tags:
                content_list_order.append(div_tag)
            for obj_tag in content_list_order:
                dict_data_clog = eval(obj_tag.attrs.get('data-log'))
                url = dict_data_clog['mu']
                if url:
                    try:
                        print("dict_data_clog.attrs.get('order')========> ", dict_data_clog.attrs.get('order'))
                        ret_two_url = requests.get(url, headers=headers, timeout=10)
                        # print('ret_two_url------> ',ret_two_url)
                        if ret_two_url.url == self.lianjie or self.lianjie in ret_two_url.url:
                            paiming_order = dict_data_clog['order']
                            break
                    except Exception:
                        break
        data_list = {
            'order': int(paiming_order),
            'shoulu': resultObj['shoulu'],
        }
        return data_list
    def PC_360_URL_PC(self):
        pc_360url = """https://so.com/s?src=3600w&q={keyword}""".format(keyword=self.keywords)
        order = 0
        resultObj = self.pcShoulu360(self.lianjie)
        ret_domain = requests.get(pc_360url, headers=self.headers)
        soup = BeautifulSoup(ret_domain.text, 'lxml')
        if soup.find('div', class_='so-toptip'):
            resultObj['shoulu'] = '0'
        else:
            li_tags = soup.find_all('li', class_='res-list')
            order_num = 0
            for li_tag in li_tags:
                order_num += 1
                if li_tag.find('p', class_='res-linkinfo'):
                    zongti_xinxi = li_tag.find('a', target='_blank')  # 获取order -- title -- title_url
                    yuming_canshu = li_tag.find('p', class_='res-linkinfo')  # 域名参数
                    if li_tag.find('a').attrs.get('data-url'):
                        data_url = li_tag.find('a').attrs.get('data-url')
                    else:
                        data_url = zongti_xinxi.attrs['href']
                    yuming = yuming_canshu.find('cite').get_text()
                    yuming_deal = yuming.split('/')[0].rstrip('...').split('>')[0]
                    if yuming_deal in self.lianjie:
                        ret_two_url = requests.get(data_url, headers=self.headers, timeout=10)
                        if self.lianjie in ret_two_url.url:
                            order = order_num
                            break
        data_list = {
            'order': order,
            'shoulu': resultObj['shoulu'],
        }
        return data_list
    def PC_360_URL_MOBILE(self):
        PC_360_url = 'https://m.so.com/s?src=3600w&q={}'.format(self.keywords)
        order = 0
        resultObj = self.mobielShoulu360(self.lianjie)
        headers = {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
        ret = requests.get(PC_360_url, headers=headers)
        soup = BeautifulSoup(ret.text, 'lxml')
        if soup.find('div', class_='mso-url2link'):
            resultObj['shoulu'] = '0'
        else:
            div_tags = soup.find_all('div', class_=' g-card res-list og ')
            order_num = 0
            for div_tag in div_tags:
                order_num += 1
                if div_tag.attrs.get('data-pcurl'):
                    url_data = div_tag.attrs.get('data-pcurl')
                    ret_two_url = requests.get(url_data, headers=headers, timeout=10)
                    if self.lianjie in ret_two_url.url:
                        order = order_num
                        break
        data_list = {
            'order': order,
            'shoulu': resultObj['shoulu'],
        }
        return data_list


    def ShouLu(self):
        # pc端百度
        if self.search == '1':
            data_list = self.Baidu_Zhidao_URL_PC()

        # 移动端百度
        if self.search == '4':
            data_list = self.Baidu_Zhidao_URL_MOBILE()

        # pc端360
        if self.search == '3':
            data_list = self.PC_360_URL_PC()

        # 移动端360
        if self.search == '6':
            data_list = self.PC_360_URL_MOBILE()
        return data_list
    # def FuGai(self):
    #     if self.search == '1':
    #         # print('pc端 -- 覆盖百度', int(time.time()))
    #         resultObj = self.baiduFuGaiPC(self.keywords, self.domain)
    #         # 移动端百度
    #     elif self.search == '4':
    #         # print('移动端 -- 覆盖百度', int(time.time()))
    #         resultObj = self.baiduFuGaiMOBIEL(self.keywords, self.domain)
    #         # pc360
    #     elif self.search == '3':
    #         # print('pc端 -- 覆盖360', int(time.time()))
    #         resultObj = self.pcFugai360(self.keywords, self.domain)
    #         # # 移动端360
    #     elif self.search == '6':
    #         # print('移动端 -- 覆盖360 ', int(time.time()))
    #         resultObj = self.mobielFugai360(self.keywords, self.domain)
    #     order_list = []
    #     for result in resultObj:
    #         order_list.append(result['paiming'])
    #     return order_list
def start():
    # url = 'http://api.zhugeyingxiao.com/zhugedanao/zhongDianCiChaXunDecideIsTask'
    # ret = requests.get(url)
    # print('ret.json()---------> ',ret.json())
    # url = 'http://127.0.0.1:8000/zhugedanao/HuoQuRenWuzhongDianCi'
    url = 'http://api.zhugeyingxiao.com/zhugedanao/HuoQuRenWuzhongDianCi'
    ret = requests.get(url)
    ret_text = ret.text
    json_data = json.loads(ret_text)
    if json_data['data']:
        print('json_data===========> ',json_data)
        tid = json_data['data']['tid']
        search_engine = json_data['data']['search_engine']
        keywords = json_data['data']['keywords']
        domain = json_data['data']['mohupipei']
        detail_id = json_data['data']['detail_id']
        lianjie = json_data['data']['lianjie']
        objs = zhongdianci_chaxun(lianjie, detail_id, keywords, domain, search_engine)
        if lianjie:
            resultObj = objs.ShouLu()
            data_list = {
                'tid': tid,
                'resultObj': json.dumps(resultObj),
                'judge':'shoulu'
            }
        else:
            resultObj = objs.FuGai()
            data_list = {
                'tid': tid,
                'resultObj': json.dumps(resultObj),
                'judge': 'fugai'
            }
        print('resultObj=====> ',resultObj)
        # url = 'http://127.0.0.1:8000/zhugedanao/TiJiaoRenWuzhongDianCi'
        url = 'http://api.zhugeyingxiao.com/zhugedanao/TiJiaoRenWuzhongDianCi'
        requests.post(url, data=data_list)

    else:
        print('无任务')

# if __name__ == '__main__':
#     start()






# import datetime, time
#
#
# now_date = datetime.date.today().strftime('%Y-%m-%d') # 当前年月日
#
#
# canshu = now_date + ' ' + '07:50:20'
# kaishishijian = datetime.datetime.today().strptime(canshu, "%Y-%m-%d %H:%M:%S")
#
# now = now_date + ' ' + time.strftime("%H:%M:%S")
# now_time = datetime.datetime.today().strptime(now, "%Y-%m-%d %H:%M:%S")
#
# print('kaishishijian-------> ', kaishishijian, type(kaishishijian))
# print('now_time--------> ', now_time, type(now_time))
#
# if kaishishijian < now_time:
#     kaishishijian_add1 = (kaishishijian + datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
#     print('kaishishijian_add1-> ',kaishishijian_add1)

#
# import re
# strt = '合众康桥http://www.bjhzkq.com'
# str_re = re.findall("(.*)http", strt.replace('\t', ''))
# print(str_re[0])
# print(strt.split(str_re[0]))



# url = 'http://api.zhugeyingxiao.com/zhugedanao/gonggong_exit_delete?timestamp=1534892912986&rand_str=d8ba5392b85e56d9e3631aaf1822e7d8&user_id=10'
# # url = 'http://127.0.0.1:8000/zhugedanao/gonggong_exit_delete?timestamp=1534157927644&rand_str=326e44a7eee743971a17dd69eb39e1fc&user_id=10'
#
# # url = 'http://127.0.0.1:8000/zhugedanao/shouLuChaxun/clickReturn/0?timestamp=1534892912986&rand_str=d8ba5392b85e56d9e3631aaf1822e7d8&user_id=10'
# # url = 'http://127.0.0.1:8000/zhugedanao/shouLuChaxun/clickReturn/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11'
# ret = requests.get(url)
# print(ret.status_code)
# print(json.loads(ret.text))
# import base64
# copyright = 'Copyright (c) 2012 Doucube Inc. All rights reserved.'
# bytesString = copyright.encode(encoding="utf-8")
# print(bytesString)
#
# #base64 编码
# encodestr = base64.b64encode(bytesString)
# print(encodestr)
# print(encodestr.decode())
#
# #解码
# decodestr = base64.b64decode(encodestr)
# print(decodestr.decode())
#
#
# p = '字符串'
# m = p.encode(encoding="utf-8")
# encodestr = base64.b64encode(m)
# print(encodestr.decode())
#
# decodestr = base64.b64decode(encodestr)
# print(decodestr.decode())
#
# nickname = base64.b64encode(copyright.encode(encoding='utf-8'))


# p = '按时间段按时'
# m = json.dumps(p)
# print(m)
# nickname = base64.b64encode(json.loads(m).encode(encoding='utf-8'))
#
# print(nickname)
#
# username = base64.b64decode(nickname).decode()
# print('username =-=======> ', username)



    # # 360pc端覆盖查询
    # def pcFugai360(self):
    #     order_list = []
    #     headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)], }
    #     pc_360url = 'https://so.com/s?src=3600w&q={keyword}'.format(keyword=self.keyword)
    #     print('pc_360url--------->', pc_360url)
    #     ret = requests.get(pc_360url, headers=headers, timeout=10)
    #     soup = BeautifulSoup(ret.text, 'lxml')
    #     div_tags = soup.find_all('li', class_='res-list')
    #     for mohu_pipei in self.mohu_pipei.split(','):
    #         for div_tag in div_tags:
    #             zongti_fugai = div_tag.get_text()
    #             if mohu_pipei in zongti_fugai:
    #                 if div_tag.find('a').attrs.get('data-res'):
    #                     data_res = div_tag.find('a')
    #                     paiming = data_res.attrs.get('data-res')
    #                     dict_data_res = json.loads(paiming)
    #                     panduan_url = data_res.attrs['href']
    #                     title = data_res.get_text()
    #                     order_num = int(dict_data_res['pos'])
    #                     order_list.append({
    #                         'paiming': order_num,
    #                         'title': title,
    #                         'title_url': panduan_url,
    #                         'sousuo_guize': mohu_pipei,
    #                         'search': self.search
    #                     })
    #     print('rentur')
    #     return order_list
    #
    # # 360移动端覆盖查询
    # def mobielFugai360(self):
    #     PC_360_url = 'https://m.so.com/s?src=3600w&q={}'.format(self.keyword)
    #     order_list = []
    #     headers = {
    #         'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
    #     ret = requests.get(PC_360_url, headers=headers, timeout=10)
    #     soup_browser = BeautifulSoup(ret.text, 'lxml')
    #     div_tags = soup_browser.find_all('div', class_=" g-card res-list og ")
    #     order = 0
    #     for mohu_pipei in self.mohu_pipei.split(','):
    #         for div_tag in div_tags:
    #             order += 1
    #             zongti_fugai = div_tag.get_text()
    #             if mohu_pipei in zongti_fugai:
    #                 a_tag = div_tag.find('a', class_='alink')
    #                 title = a_tag.find('h3').get_text()
    #                 panduan_url = a_tag.attrs['href']
    #                 order_num = int(order)
    #                 order_list.append({
    #                     'paiming': order_num,
    #                     'title': title,
    #                     'title_url': panduan_url,
    #                     'sousuo_guize': mohu_pipei,
    #                     'search': self.search
    #                 })
    #     return order_list


class pingtaiwajue_chaxun():
    def __init__(self, search, keyword, mohu_pipei):
        self.search = search
        self.keyword = keyword
        self.mohu_pipei = mohu_pipei

    # 百度pc端覆盖查询
    def baiduFuGaiPC(self):
        order_list = []
        headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)], }
        zhidao_url = 'https://www.baidu.com/s?wd={keyword}'.format(keyword=self.keyword)
        # print('-=---------->', zhidao_url)
        ret = requests.get(zhidao_url, headers=headers, timeout=10)
        soup = BeautifulSoup(ret.text, 'lxml')
        div_tags = soup.find_all('div', class_='result c-container ')
        for mohu_pipei in self.mohu_pipei.split(','):
            print('mohu_pipei===> ',mohu_pipei)
            for div_tag in div_tags:
                rank_num = div_tag.attrs.get('id')
                if not rank_num:
                    continue
                tiaojian_chaxun = div_tag.get_text()
                panduan_url = div_tag.find('h3', class_='t').find('a').attrs['href']
                title = div_tag.find('h3', class_='t').get_text()
                # print('tiaojian_chaxun-------> ', mohu_pipei, tiaojian_chaxun)
                if mohu_pipei in tiaojian_chaxun:  # 表示有覆盖
                    order_num = int(rank_num)
                    order_list.append({
                        'paiming': order_num,
                        'title': title,
                        'title_url': panduan_url,
                        'sousuo_guize': mohu_pipei,
                        'search':self.search
                    })
        return order_list

    # 百度移动端覆盖查询
    def baiduFuGaiMOBIEL(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
        zhidao_url = 'https://m.baidu.com/s?word={}'.format(self.keyword)
        ret = requests.get(zhidao_url, headers=headers, timeout=10)
        soup_browser = BeautifulSoup(ret.text, 'lxml')
        content_list_order = []
        div_tags = soup_browser.find_all('div', class_='result c-result')
        for div_tag in div_tags:
            content_list_order.append(div_tag)
        div_tags = soup_browser.find_all('div', class_='result c-result c-clk-recommend')
        for div_tag in div_tags:
            content_list_order.append(div_tag)
        order_list = []
        for mohu_pipei in self.mohu_pipei.split(','):
            for data in content_list_order:
                if data['data-log']:
                    dict_data = eval(data['data-log'])
                    url_title = dict_data['mu']  # 标题链接
                    order = dict_data['order']  # 排名
                    pipei_tiaojian = data.get_text()
                    if mohu_pipei in pipei_tiaojian:
                        if data.find('div', class_='c-container').find('a'):
                            title = data.find('div', class_='c-container').find('a').get_text()
                            order_num = int(order)
                            order_list.append({
                                'paiming': order_num,
                                'title': title,
                                'title_url': url_title,
                                'sousuo_guize': mohu_pipei,
                                'search': self.search
                            })
        return order_list



    def qufenyinqing(self):
        if str(self.search) == '1':
            print('pc端 -- 覆盖百度')
            resultObj = self.baiduFuGaiPC()
            # 移动端百度
        elif str(self.search) == '4':
            print('移动端 -- 覆盖百度')
            resultObj = self.baiduFuGaiMOBIEL()
            # pc360
        return resultObj



# 百度pc端覆盖查询
def baiduFuGaiPC(keyword):
    order_list = []
    headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)], }
    zhidao_url = 'https://www.baidu.com/s?wd={keyword}'.format(keyword=keyword)
    ret = requests.get(zhidao_url, headers=headers, timeout=10)
    soup = BeautifulSoup(ret.text, 'lxml')
    div_tags = soup.find_all('div', class_='result c-container ')
    for div_tag in div_tags:
        div_f13 = div_tag.find('div', class_='f13').get_text()
        yuming = div_f13.split('-')[0].strip()
    page = 1
    while True:
        a_next = soup.find('a', text='下一页>').attrs['href']
        print('a_next=== 》','https://www.baidu.com' + a_next)
        page += 1
        if page == 3:
            break















# import base64
# data_list = []
# for name in ['客户ID230', '客户ID34', '🌻李汉杰👵', '🌿张聪', '卢俊义', '公孙胜', '秦明', '假如', '关胜', '过客❤', 'ju do it',
#              '西门庆豪|董庆豪|合众', '梦忆🍁', '吴用', '青春不散场@',
#              '诸葛营销', '武松', '刘鹏', '林敏', '张清', '柴进', '李应', '花荣', '硕子😁 🏀', '胡蓉', '夏宏伟：品牌良医', '许艳', '贺～丹', '余宏亮']:
#     encodestr = base64.b64encode(name.encode('utf-8'))
#     encode_username = str(encodestr, encoding='utf-8')
#     decode_username = base64.b64decode(encode_username)
#     username = str(decode_username, encoding='utf-8')
#     data_list.append(json.dumps(username))
#


# url = 'http://127.0.0.1:8000/zhugedanao/zhongDianCiChaXunDecideIsTask'
url = 'http://api.zhugeyingxiao.com/zhugedanao/zhongDianCiChaXunDecideIsTask'
# url = 'http://api.zhugeyingxiao.com/zhugedanao/timeToRefreshZhgongDianCi'
# ret = requests.get(url)
# print(os.getcwd())
# print(ret.text)



import json, requests
import threading
# def zhongDianCiTimerRefresh():
#     timer = threading.Timer(30, zhongDianCiTimerRefresh)
#     timer.start()
#     print('==========')
    # url = 'http://127.0.0.1:8000/zhugedanao/timeToRefreshZhgongDianCi'
    # requests.get(url)

# zhongDianCiTimerRefresh()

#
# url = 'http://api.zhugeyingxiao.com/zhugedanao/pingTaiWaJue/finalResult/0?timestamp=1534157927644&rand_str=17737c51d4459f40694e4740bc5a002c&user_id=11'
# ret = requests.get(url)
# print(ret.text)













def baiduShouLuPC(domain, liaojietijiao_shoulu=None):
    resultObj = {
        "shoulu": 0,
        "kuaizhao_time": '',
        "title": '',
        "status_code": ''
    }
    # 编码成url格式
    domain = parse.quote_plus(domain.strip())
    zhidao_url = 'http://www.baidu.com/s?wd={domain}'.format(domain=domain)
    headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)]}
    ret_domain = requests.get(zhidao_url, headers=headers, timeout=10)
    soup_domain = BeautifulSoup(ret_domain.text, 'lxml')
    if soup_domain.find('div', class_='content_none'):
        resultObj["status_code"] = ret_domain.status_code
    else:
        div_tags = soup_domain.find_all('div', class_='result c-container ')
        if div_tags and div_tags[0].attrs.get('id'):
            panduan_url = div_tags[0].find('a')['href']
            f13_div = div_tags[0].find('div', class_='f13')
            if liaojietijiao_shoulu:
                ret = requests.get(panduan_url, headers=headers, timeout=10)
                ret_two_url = ret.url
                if domain in ret_two_url or domain == ret_two_url:
                    if f13_div.find('a'):
                        resultObj["shoulu"] = 1
                else:
                    resultObj["shoulu"] = 0
            else:
                print('div_tags====> ',div_tags[0].find('a').get_text())
                ret = requests.get(panduan_url, headers=headers, timeout=10)
                print(ret.url)
import re
# domain = 'https://wenda.so.com/q/1373013967063537'
# baiduShouLuPC(domain)


# re.search('window.location.replace', ret.text)
# print(ret.text.split('window.location.replace'))

# domain = 'http://news.100yiyao.com/detail/193538320.html'
# baiduShouLuPC(domain)
            #     status_code, title, ret_two_url = getPageInfo(panduan_url)
            #     # 解码
            #     domain = parse.unquote_plus(domain)
            #     if domain in ret_two_url or domain == ret_two_url:
            #         if f13_div.find('a'):
            #             resultObj["shoulu"] = 1
            #             resultObj["title"] = title
            #             resultObj["status_code"] = status_code
            #             if div_tags[0].find('span', class_='newTimeFactor_before_abs'):
            #                 resultObj["kuaizhao_time"] = div_tags[0].find('span',
            #                     class_='newTimeFactor_before_abs').get_text().strip().replace('-', '').replace('年',
            #                     '-').replace('月', '-').replace('日', '').strip()
            #     else:
            #         status_code, title, ret_two_url = getPageInfo(domain)
            #         resultObj["title"] = title
            #         resultObj["status_code"] = status_code
            #         resultObj["shoulu"] = 0

    # return resultObj






def baiduShouLuMobeil(domain, liaojietijiao_shoulu=None):
    resultObj = {
        "shoulu": 0,
        "kuaizhao_time": '',
        "title": '',
        "status_code": ''
    }
    # 编码成url格式
    domain = parse.quote_plus(domain.strip())
    zhidao_url = 'https://m.baidu.com/from=844b/pu=sz@1320_2001/s?tn=iphone&usm=2&word={}'.format(domain)
    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
    ret_domain = requests.get(zhidao_url, headers=headers, timeout=10)
    print('zhidao_url=======> ', zhidao_url)
    soup_domain = BeautifulSoup(ret_domain.text, 'lxml')
    if not soup_domain.find_all('div', class_='result c-result'):
        resultObj["status_code"] = ret_domain.status_code
    else:
        div_tags = soup_domain.find_all('div', class_='result c-result')
        if div_tags:
            dict_data_clog = eval(div_tags[0].attrs.get('data-log'))
            url = dict_data_clog['mu']
            if url.strip():
                domain_jiema = parse.unquote_plus(domain)
                if liaojietijiao_shoulu:
                    ret = requests.get(url, headers=headers, timeout=10)
                    ret_two_url = ret.url
                    if domain_jiema == ret_two_url or domain_jiema in ret_two_url:
                        resultObj["shoulu"] = 1
                    else:
                        resultObj["shoulu"] = 0
                else:
                    ret = requests.get(url, headers=headers, timeout=10)
                    if domain_jiema == ret.url or domain_jiema in ret.url:
                        resultObj["status_code"] = ret.status_code
                        if ret.status_code == 200 :
                            resultObj["title"] = div_tags[0].find('a').get_text()
                            resultObj["shoulu"] = 1
                    else:
                        ret = requests.get(url, headers=headers, timeout=10)
                        resultObj["status_code"] = ret.status_code
                        resultObj["shoulu"] = 0
    print('resultObj======> ',resultObj)
    # return resultObj




def pcShoulu360(domain):
    resultObj = {
        "shoulu": 0,
        "kuaizhao_time": '',
        "title": '',
        "status_code": '',
        "rank_num": 0
    }
    # 编码成url格式
    domain = parse.quote_plus(domain.strip())
    headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)]}
    pc_360url = 'https://so.com/s?src=3600w&q={domain}'.format(domain=domain)
    ret_domain = requests.get(pc_360url, headers=headers, timeout=10)
    print('pc_360url============> ', pc_360url)
    soup = BeautifulSoup(ret_domain.text, 'lxml')
    if soup.find('div', class_='so-toptip'):
        resultObj['shoulu'] = '0'
        resultObj["status_code"] = ret_domain.status_code
    else:
        li_tags = soup.find_all('li', class_='res-list')
        if len(li_tags) > 0:
            zongti_xinxi = li_tags[0].find('a', target='_blank')  # 获取order -- title -- title_url
            yuming_canshu = li_tags[0].find('p', class_='res-linkinfo')  # 域名参数
            if li_tags[0].find('a').attrs.get('data-url'):
                data_url = li_tags[0].find('a').attrs.get('data-url')
            else:
                data_url = zongti_xinxi.attrs['href']
            # status_code, title, ret_two_url = getPageInfo(data_url)
            ret = requests.get(data_url, headers=headers, timeout=10)
            # # 解码
            domain_jiema = parse.unquote_plus(domain)
            if domain_jiema in ret.url or domain_jiema == ret.url:
                resultObj["status_code"] = ret.status_code
                if ret.status_code == 200:
                    resultObj["title"] = li_tags[0].find('a').get_text()
                    resultObj['shoulu'] = 1
            else:
                ret = requests.get(data_url, headers=headers, timeout=10)
                resultObj["status_code"] = ret.status_code
                resultObj['shoulu'] = 0
    print(resultObj)
    return resultObj

def mobielShoulu360(domain):
    resultObj = {
        "shoulu": 0,
        "kuaizhao_time": '',
        "title": '',
        "status_code": '',
        "rank_num": 0
    }
    # 编码成url格式
    domain = parse.quote_plus(domain.strip())
    PC_360_url = 'https://m.so.com/s?src=3600w&q={}'.format(domain)
    print('PC_360_url------> ', PC_360_url)
    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
    ret = requests.get(PC_360_url, headers=headers, timeout=10)
    soup = BeautifulSoup(ret.text, 'lxml')
    if soup.find('div', class_='mso-url2link'):
        resultObj["status_code"] = ret.status_code
    else:
        div_tags = soup.find_all('div', class_=' g-card res-list og ')
        if len(div_tags) > 0:
            url_data = div_tags[0].attrs.get('data-pcurl')
            # # 解码
            domain = parse.unquote_plus(domain)
            ret = requests.get(url_data, headers=headers, timeout=10)
            if domain in ret.url or ret.url == domain:
                resultObj["status_code"] = ret.status_code
                if ret.status_code == 200:
                    resultObj["title"] = div_tags[0].find('a').get_text()
                    resultObj['shoulu'] = 1
            else:
                ret = requests.get(url_data, headers=headers, timeout=10)
                resultObj["status_code"] = ret.status_code
                resultObj['shoulu'] = 0
    print(resultObj)
    return resultObj



headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)]}
import re

ret = requests.get('http://www.baidu.com/link?url=49bGpZx-NhCEdpw8XvicGvqI0htNiQ4esXfsP1UlgRpQSxm7Zz5t6YTGkWesSSIOYJ3yML6VovtqKzkt5YjMkq', headers=headers, timeout=5, allow_redirects=False)
if ret.status_code == 200:
    pattern = re.compile(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    zhixing_url = re.findall(pattern, ret.text)
    if len(zhixing_url) > 1:
        zhixing_url = zhixing_url[0]
if ret.status_code == 302:
    zhixing_url = ret.headers['location']

pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # 匹配模式
url = re.findall(pattern, ret.text)
if len(url) > 1:
    url = url[0]

# print('url========> ',url)

# import ast
#
# chrfiles = "9, 2, 10, 4, 3, 65, 7"
# paiming_detail =set(eval(chrfiles))
# paiming_detail_sort = sorted(paiming_detail)
# ls2 = [str(i) for i in paiming_detail_sort]
#
# # print(','.join(ls2))
# # print(" ".join(paiming_detail_sort))
#
#
#
# p = '{"q":"北京","p":"false","s":["北京时间","北京天气","北京爱情故事","北京地铁","北京地图","北京爱情故事电影版","北京天气预报","北京车展","北京空气质量指数","北京移动"]}'
# print(json.loads(json.dumps(p)), type(json.loads(json.dumps(p))))
#
# print(ast.literal_eval(p), type(ast.literal_eval(p)))




# import requests
#
# # url = 'http://news.100yiyao.com/detail/193538318.html'
# url = 'https://m.so.com/jump?u=https%3A%2F%2Fsh.qihoo.com%2Fctranscode%3Ftitle%3D%25E7%2596%25AF%25E7%258B%2582%25E9%25BE%2599%25E5%258D%259A%25E5%25A3%25AB%25E5%25A5%25BD%25E4%25B8%258D%25E5%25A5%25BD%253F%25E5%2580%25BC%25E5%25BE%2597%25E6%2582%25A8%25E9%2580%2589%25E6%258B%25A9%25E7%259A%2584%25E5%25A5%25BD%25E7%259A%2584%25E6%2595%2599%25E8%2582%25B2%25E5%2593%2581%25E7%2589%258C%26u%3Dhttp%253A%252F%252Fnews.chinabyte.com%252Fcsgg%252F332%252F14375332.shtml%26m%3D476772c07b815a5ff071862baa87086fd1eb5233%26q%3Dhttp%253A%252F%252Fnews.chinabyte.com%252Fcsgg%252F332%252F14375332.shtml&m=1d66a5&from=m.so.com'
# ret = requests.get(url, timeout=10, allow_redirects=False)
# print('ret===========> ', ret.text)
# print('ret===========> ', ret.headers)
# print('ret===========> ', ret.text)
# print(ret.status_code)


# print('\033[1;35;0m字体变色，但无背景色 \033[0m')  # 有高亮 或者
# print('\033[1;35m字体有色，但无背景色 \033[0m')



# import redis
# # r = redis.Redis(host='redis://redis_host', port=6379, db=4, decode_responses=True)
# rc = redis.Redis(host='192.168.100.20', port=6379, db=4, decode_responses=True)
#
# rc.set('name', 'zhangsan', ex=None, px=None, nx=False, xx=False)
#
# p = rc.get('name')
# print(p )


# from requests.exceptions import ConnectionError
#
# p = 'http://www.jiacom/hy==='
#
# pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # 匹配模式
# url = re.findall(pattern, p)
# if url:
#     print('=-==', url)
#     try:
#         ret = requests.get(url[0])
#     except ConnectionError:
#         print('==-----')


# 爬虫2018-09-10
# from openpyxl.styles import Font, Alignment
# from openpyxl import Workbook
# date = datetime.datetime.now().strftime('%Y-%m-%d')
#
# wb = Workbook()
# ws = wb.active
# ws.cell(row=1, column=1, value="久久网站爬取").font = Font(b=True, size=15)
# ws.cell(row=3, column=1, value="医院名称")
# ws.cell(row=3, column=2, value="医院电话")
# ws.cell(row=3, column=3, value="医院科室")
# ws.cell(row=3, column=4, value="医院地址")
# create_date = ws.cell(row=1, column=5, value="创建时间:{date}".format(date=date))
# create_date.font = Font(b=True, size=13, color='DC143C')
#
# # 合并单元格        开始行      结束行       用哪列          占用哪列
# ws.merge_cells(start_row=1, end_row=2, start_column=1, end_column=4)
# ws.merge_cells(start_row=1, end_row=3, start_column=5, end_column=7)
#
#
# # print('设置列宽')
# ws.column_dimensions['A'].width = 30
# ws.column_dimensions['B'].width = 30
# ws.column_dimensions['C'].width = 30
# ws.column_dimensions['D'].width = 30
#
#
# # print('文本居中')
# ws['A1'].alignment = Alignment(horizontal='center', vertical='center')
# ws['A3'].alignment = Alignment(horizontal='center', vertical='center')
# ws['B3'].alignment = Alignment(horizontal='center', vertical='center')
# ws['C3'].alignment = Alignment(horizontal='center', vertical='center')
# ws['D3'].alignment = Alignment(horizontal='center', vertical='center')
# ws['E1'].alignment = Alignment(horizontal='center', vertical='center')

# wb.save('./1.xlsx')


# 三元表达式 实现斐波那契额数列
# def fn(n):
#     return n if n < 2 else fn(n-1)+fn(n-2)
# n = 5
# p = fn(n)
# print(p)



# 搜狗浏览器爬虫测试
import requests
from bs4 import BeautifulSoup
import requests, json, random
from urllib import parse
import os,sys
import re
sys.path.append(os.path.dirname(os.getcwd()))
from requests.exceptions import ConnectTimeout
from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectionError




# headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)]}
# domain = 'http://www.bjhzkq.com'
# souGouURL = 'https://www.sogou.com/web?query={domain}'.format(domain=domain)
# ret = requests.get(souGouURL, headers=headers)
# soup = BeautifulSoup(ret.text, 'lxml')
# linkhead = soup.find('div', class_='linkhead')
# if linkhead:
#     if '未收录' in linkhead.get_text():
#         print('无收录')
#     else:
#         resultTag = soup.find('div', id='rb_0')
#         panduanUrl = resultTag.find('a').get('href')
#         if 'http' not in panduanUrl:
#             panduanUrl  = 'https://www.sogou.com/' + panduanUrl
#         left_down_url = resultTag.find('div', class_='fb').find('cite').find('b').get_text()
#         left_down_url = left_down_url.strip().split('...')[0]
#         if '>' in left_down_url:
#             left_down_url = left_down_url.split('>')[0]
#         if not left_down_url.startswith('http'):
#             left_down_url = 'http://' + left_down_url
#         urlparse_obj = parse.urlparse(left_down_url.rstrip('.'))
#         left_down_domain = urlparse_obj.netloc
#         if left_down_domain in domain:
#             if domain in panduanUrl or domain == panduanUrl:
#                 print('===========')
#             else:
#                 zhixing_url = getSiteUrl(domain, panduanUrl, headers)
#                 if zhixing_url:
#                     print('============')
#                 else:
#                     print('无收录')


# p = [1,2,3,4,5,6,7,8,9]
#
# print(random.sample(p, 5))



# 获取链接标题 状态码 解密url
def getSiteUrl(domain, panduan_url, headers, mobeil=None):
    try:
        print('------------> ',panduan_url)
        ret = requests.get(panduan_url, headers=headers, timeout=5, allow_redirects=False)
        # print('ret.text===========> ', ret.text)
        flag = 0
        https_domain = ''


        if domain.startswith('http'):
            https_domain = domain.replace('http', 'https')
        if ret.status_code == 200:
            pattern = re.compile(
                r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
            zhixing_url = re.findall(pattern, ret.text)
            if len(zhixing_url) > 1:
                if len(zhixing_url) >= 2:
                    zhixing_url = zhixing_url[0]
                # print('--zhixing_url--> ', domain, zhixing_url)
                if domain in zhixing_url or domain == zhixing_url or https_domain in zhixing_url or https_domain == zhixing_url:
                    flag = 1
        else:
            zhixing_url = ret.headers['location']
            if domain in zhixing_url or domain == zhixing_url or https_domain in zhixing_url or https_domain == zhixing_url:
                flag = 1
            else:
                ret = requests.get(panduan_url, headers=headers, timeout=5)
                ret_url = ret.url
                if domain in ret_url or domain == ret_url or https_domain in ret_url or https_domain == ret_url:
                    flag = 1
        if mobeil:
            if 'http://m' in zhixing_url:
                zhixing_url = zhixing_url.split('http://m')[1]
            if 'https://m' in zhixing_url:
                zhixing_url = zhixing_url.split('https://m')[1]
            if domain in zhixing_url or domain == zhixing_url:
                flag = 1

        return flag
    except ConnectTimeout:
        pass

def shenma(domain):
    url = 'https://m.sm.cn/s?q={}'.format(domain)
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36'}
    ret = requests.get(url, headers=headers)
    soup = BeautifulSoup(ret.text, 'lxml')
    resultsTag = soup.find('div', id='results')
    div_tags = resultsTag.find_all('div', class_='sc c-container')
    if len(div_tags) > 1:
        panduan_url = div_tags[0].find('a').get('href')
        page_link = div_tags[0].get('data-sc')
        if 'null' in page_link:
            page_link = page_link.replace('null', '0')
        pageLinkEval = eval(page_link)
        order = pageLinkEval.get('pg')
        if domain == panduan_url:
            print('Shoulu')
        flag = getSiteUrl(domain, panduan_url, headers)
        print(flag)




domain = 'http://m.360xh.com/201712/04/37409.html'
shenma(domain)




















