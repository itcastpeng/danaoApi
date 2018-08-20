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
#         # 编码成url格式
#         domain = parse.quote_plus(domain.strip())
#         zhidao_url = 'http://www.baidu.com/s?wd={domain}'.format(domain=domain)
#         headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)]}
#         ret_domain = requests.get(zhidao_url, headers=headers, timeout=10)
#         soup_domain = BeautifulSoup(ret_domain.text, 'lxml')
#         if soup_domain.find('div', class_='content_none'):
#             resultObj["status_code"] = ret_domain.status_code
#         else:
#             div_tags = soup_domain.find_all('div', class_='result c-container ')
#             if div_tags and div_tags[0].attrs.get('id'):
#                 panduan_url = div_tags[0].find('a')['href']
#                 f13_div = div_tags[0].find('div', class_='f13')
#                 status_code, title, ret_two_url = self.getPageInfo(panduan_url)
#                 # 解码
#                 domain = parse.unquote_plus(domain)
#                 if domain in ret_two_url or domain == ret_two_url:
#                     if f13_div.find('a'):
#                         resultObj["title"] = title
#                         resultObj["status_code"] = status_code
#                         resultObj["shoulu"] = 1
#                 else:
#                     status_code, title, ret_two_url = self.getPageInfo(domain)
#                     resultObj["title"] = title
#                     resultObj["status_code"] = status_code
#                     resultObj["shoulu"] = 0
#                 if div_tags[0].find('span', class_='newTimeFactor_before_abs'):
#                     resultObj["kuaizhao_time"] = div_tags[0].find('span',
#                         class_='newTimeFactor_before_abs').get_text().strip().replace('-', '').replace('年',
#                         '-').replace('月', '-').replace('日', '').strip()
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
#         # 编码成url格式
#         domain = parse.quote_plus(domain.strip())
#         zhidao_url = 'https://m.baidu.com/from=844b/pu=sz@1320_2001/s?tn=iphone&usm=2&word={}'.format(domain)
#         headers = {
#             'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
#         ret_domain = requests.get(zhidao_url, headers=headers, timeout=10)
#         print('zhidao_url=======> ', zhidao_url)
#
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
#                     # 解码
#                     domain_jiema = parse.unquote_plus(domain)
#                     print(domain_jiema, ret_two_url)
#                     if domain_jiema == ret_two_url or domain_jiema in ret_two_url:
#                         resultObj["status_code"] = status_code
#                         resultObj["title"] = title
#                         resultObj["shoulu"] = 1
#                     else:
#                         status_code, title, ret_two_url = self.getPageInfo(domain_jiema)
#                         resultObj["status_code"] = status_code
#                         resultObj["title"] = title
#                         resultObj["shoulu"] = 0
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
#         # 编码成url格式
#         domain = parse.quote_plus(domain.strip())
#         headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)]}
#         pc_360url = 'https://so.com/s?src=3600w&q={domain}'.format(domain=domain)
#         ret_domain = requests.get(pc_360url, headers=headers, timeout=10)
#         print('pc_360url============> ', pc_360url)
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
#                 status_code, title, ret_two_url = self.getPageInfo(data_url)
#                 # 解码
#                 domain_jiema = parse.unquote_plus(domain)
#                 print(domain_jiema, ret_two_url)
#                 if domain_jiema in ret_two_url or domain_jiema == ret_two_url:
#                     resultObj["status_code"] = status_code
#                     resultObj["title"] = title
#                     resultObj['shoulu'] = '1'
#                 else:
#                     status_code, title, ret_two_url = self.getPageInfo(domain_jiema)
#                     resultObj["status_code"] = status_code
#                     resultObj["title"] = title
#                     resultObj['shoulu'] = '0'
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
#         # 编码成url格式
#         domain = parse.quote_plus(domain.strip())
#         PC_360_url = 'https://m.so.com/s?src=3600w&q={}'.format(domain)
#         print('PC_360_url------> ', PC_360_url)
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
#                 # 解码
#                 domain = parse.unquote_plus(domain)
#                 if domain in ret_two_url or ret_two_url == domain:
#                     resultObj["status_code"] = status_code
#                     resultObj["title"] = title
#                     resultObj['shoulu'] = '1'
#                 else:
#                     status_code, title, ret_two_url = self.getPageInfo(domain)
#                     resultObj["status_code"] = status_code
#                     resultObj["title"] = title
#                     resultObj['shoulu'] = '0'
#         return resultObj
#
#     # 判断搜索引擎
#     def judgmentSearchEngine(self):
#         resultObj = {}
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
#
#         if resultObj:
#             data_dict = {
#                 'tid':self.tid,
#                 'resultObj':resultObj
#             }
#             return data_dict
# class shouluChaXun():
#     def __init__(self):
#         self.apiHost = 'http://websiteaccount.bjhzkq.com/api/'
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
#         # url = 'http://api.zhugeyingxiao.com/zhugedanao/shouluTiJiaoRenWu'
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
#     # def vpsServerQiandao(self):
#     #     print('开始签到')
#         # params_data = {
#         #     "vpsName": settings.VPS_NAME,
#         #     "task_name": "大脑链接提交收录",
#         #     "area": settings.AREA
#         # }
#         # url = self.apiHost + "vpsServer"
#         # ret = requests.get(url, params=params_data)
#         # print(ret.text)
#         # post_data = {
#         #     'redisKey': 'wailianServer'
#         # }
#         # url = 'http://yjk.bjhzkq.com/api/setBohaoLastTime'
#         # requests.post(url, data=post_data)
#
#     def main(self):
#         # print("-" * 20 + "> 开始任务")
#         # self.adsl.reconnect()
#         # try:
#         #     self.accountApiOper.vpsServerQiandao()
#         # except requests_ConnectionError:
#         #     pass
#         # self.vpsServerQiandao()
#         self.start()
#
#
#
# class fugaipc_chaxun():
#     def __init__(self, search, keyword, mohu_pipei):
#         self.search = search
#         self.keyword = keyword
#         self.mohu_pipei = mohu_pipei
#
#     # 百度pc端覆盖查询
#     def baiduFuGaiPC(self):
#         order_list = []
#         headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)], }
#         zhidao_url = 'https://www.baidu.com/s?wd={keyword}'.format(keyword=self.keyword)
#         ret = requests.get(zhidao_url, headers=headers, timeout=10)
#         soup = BeautifulSoup(ret.text, 'lxml')
#         div_tags = soup.find_all('div', class_='result c-container ')
#         for mohu_pipei in self.mohu_pipei.split(','):
#             for div_tag in div_tags:
#                 rank_num = div_tag.attrs.get('id')
#                 if not rank_num:
#                     continue
#                 tiaojian_chaxun = div_tag.get_text()
#                 panduan_url = div_tag.find('h3', class_='t').find('a').attrs['href']
#                 title = div_tag.find('h3', class_='t').get_text()
#                 if mohu_pipei in tiaojian_chaxun:  # 表示有覆盖
#                     order_num = int(rank_num)
#                     order_list.append({
#                         'paiming': order_num,
#                         'title': title,
#                         'title_url': panduan_url,
#                         'sousuo_guize': mohu_pipei,
#                         'search':self.search
#                     })
#         return order_list
#
#     # 百度移动端覆盖查询
#     def baiduFuGaiMOBIEL(self):
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
#         zhidao_url = 'https://m.baidu.com/s?word={}'.format(self.keyword)
#         ret = requests.get(zhidao_url, headers=headers, timeout=10)
#         soup_browser = BeautifulSoup(ret.text, 'lxml')
#         content_list_order = []
#         div_tags = soup_browser.find_all('div', class_='result c-result')
#         for div_tag in div_tags:
#             content_list_order.append(div_tag)
#         div_tags = soup_browser.find_all('div', class_='result c-result c-clk-recommend')
#         for div_tag in div_tags:
#             content_list_order.append(div_tag)
#         order_list = []
#         for mohu_pipei in self.mohu_pipei.split(','):
#             for data in content_list_order:
#                 if data['data-log']:
#                     dict_data = eval(data['data-log'])
#                     url_title = dict_data['mu']  # 标题链接
#                     order = dict_data['order']  # 排名
#                     pipei_tiaojian = data.get_text()
#                     if mohu_pipei in pipei_tiaojian:
#                         if data.find('div', class_='c-container').find('a'):
#                             title = data.find('div', class_='c-container').find('a').get_text()
#                             order_num = int(order)
#                             order_list.append({
#                                 'paiming': order_num,
#                                 'title': title,
#                                 'title_url': url_title,
#                                 'sousuo_guize': mohu_pipei,
#                                 'search': self.search
#                             })
#         return order_list
#
#     # 360pc端覆盖查询
#     def pcFugai360(self):
#         order_list = []
#         headers = {'User-Agent': pcRequestHeader[random.randint(0, len(pcRequestHeader) - 1)], }
#         pc_360url = 'https://so.com/s?src=3600w&q={keyword}'.format(keyword=self.keyword)
#         ret = requests.get(pc_360url, headers=headers, timeout=10)
#         soup = BeautifulSoup(ret.text, 'lxml')
#         div_tags = soup.find_all('li', class_='res-list')
#         for mohu_pipei in self.mohu_pipei.split(','):
#             for div_tag in div_tags:
#                 zongti_fugai = div_tag.get_text()
#                 if mohu_pipei in zongti_fugai:
#                     if div_tag.find('a').attrs.get('data-res'):
#                         data_res = div_tag.find('a')
#                         paiming = data_res.attrs.get('data-res')
#                         dict_data_res = json.loads(paiming)
#                         panduan_url = data_res.attrs['href']
#                         title = data_res.get_text()
#                         order_num = int(dict_data_res['pos'])
#                         order_list.append({
#                             'paiming': order_num,
#                             'title': title,
#                             'title_url': panduan_url,
#                             'sousuo_guize': mohu_pipei,
#                             'search': self.search
#                         })
#         return order_list
#
#     # 360移动端覆盖查询
#     def mobielFugai360(self):
#         PC_360_url = 'https://m.so.com/s?src=3600w&q={}'.format(self.keyword)
#         order_list = []
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
#         ret = requests.get(PC_360_url, headers=headers, timeout=10)
#         soup_browser = BeautifulSoup(ret.text, 'lxml')
#         div_tags = soup_browser.find_all('div', class_=" g-card res-list og ")
#         order = 0
#         for mohu_pipei in self.mohu_pipei.split(','):
#             for div_tag in div_tags:
#                 order += 1
#                 zongti_fugai = div_tag.get_text()
#                 if mohu_pipei in zongti_fugai:
#                     a_tag = div_tag.find('a', class_='alink')
#                     title = a_tag.find('h3').get_text()
#                     panduan_url = a_tag.attrs['href']
#                     order_num = int(order)
#                     order_list.append({
#                         'paiming': order_num,
#                         'title': title,
#                         'title_url': panduan_url,
#                         'sousuo_guize': mohu_pipei,
#                         'search': self.search
#                     })
#         return order_list
#
#
#     def qufenyinqing(self):
#         if str(self.search) == '1':
#             # print('pc端 -- 覆盖百度', int(time.time()))
#             resultObj = self.baiduFuGaiPC()
#             # 移动端百度
#         elif str(self.search) == '4':
#             # print('移动端 -- 覆盖百度', int(time.time()))
#             resultObj = self.baiduFuGaiMOBIEL()
#             # pc360
#         elif str(self.search) == '3':
#             # print('pc端 -- 覆盖360', int(time.time()))
#             resultObj = self.pcFugai360()
#             # # 移动端360
#         elif str(self.search) == '6':
#             # print('移动端 -- 覆盖360 ', int(time.time()))
#             resultObj = self.mobielFugai360()
#         return resultObj
# class fugaichaxun():
#     def __init__(self):
#         pass
#
#     def huoqurenwu(self):
#         url = 'http://127.0.0.1:8000/zhugedanao/fuGaiHuoQuRenWu'
#         ret = requests.get(url)
#         if ret.text:
#             ret_text = json.loads(ret.text)
#             return ret_text
#
#     # 开始
#     def start(self):
#         ret_text = self.huoqurenwu()
#         print('ret_text-> ',ret_text)
#         if ret_text['code'] == 200:
#             o_id = ret_text['data']['o_id']
#             search = ret_text['data']['search']
#             keyword = ret_text['data']['keyword']
#             tiaojian = ret_text['data']['tiaojian']
#             obj = fugaipc_chaxun(search, keyword, tiaojian)
#             resultObj = obj.qufenyinqing()
#             if resultObj:
#                 data_list = {
#                     'search':search,
#                     'keyword':keyword,
#                     'o_id':o_id,
#                     'resultObj':str(resultObj)
#                 }
#                 url = 'http://127.0.0.1:8000/zhugedanao/fuGaiTiJiaoRenWu'
#                 requests.post(url, data=data_list)

# if __name__ == '__main__':
#     obj = fugaichaxun()
#     obj.start()











# import base64
# s = '啥积分呢'
#
# p = base64.b16encode(s.encode('utf-8'))
# print(p)
#
# base64.b16decode(p, 'utf-8')




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
                    resultObj['shoulu'] = 1
                else:
                    status_code, title, ret_two_url = self.getPageInfo(domain_jiema)
                    resultObj["status_code"] = status_code
                    resultObj["title"] = title
                    resultObj['shoulu'] = 0
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
        data_dict = {
            'tid':self.tid,
            'resultObj':resultObj
        }
        return data_dict

class shouluChaXun():
    def __init__(self):
        pass
        # self.apiHost = 'http://websiteaccount.bjhzkq.com/api/'

    # 获取任务
    def shouLuHuoQuRenWu(self):
        # url = 'http://api.zhugeyingxiao.com/zhugedanao/shouluHuoQuRenWu'
        url = 'http://127.0.0.1:8000/zhugedanao/shouluHuoQuRenWu'
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
        # url = 'http://api.zhugeyingxiao.com/zhugedanao/shouluTiJiaoRenWu'
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
        print(result)
        if result:
            lianjie = result['data']['url']
            tid = result['data']['o_id']
            search = result['data']['search']
            result = shouLuPcChongCha(lianjie, tid, search)
            data_dict = result.judgmentSearchEngine()
            self.shouLuReturnsTheResult(data_dict)

    # def vpsServerQiandao(self):
    #     print('开始签到')
    #     params_data = {
    #         "vpsName": settings.VPS_NAME,
    #         "task_name": "大脑收录查询",
    #         "area": settings.AREA
    #     }
    #     url = self.apiHost + "vpsServer"
    #     ret = requests.get(url, params=params_data)
    #     print(ret.text)
        # post_data = {
        #     'redisKey': 'wailianServer'
        # }
        # url = 'http://yjk.bjhzkq.com/api/setBohaoLastTime'
        # requests.post(url, data=post_data)

    def main(self):
        # print("-" * 20 + "> 开始任务")
        # self.adsl.reconnect()
        # try:
        #     self.accountApiOper.vpsServerQiandao()
        # except requests_ConnectionError:
        #     pass
        # self.vpsServerQiandao()
        self.start()


if __name__ == '__main__':
    objs = shouluChaXun()
    objs.main()
