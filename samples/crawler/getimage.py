import requests
import urllib.request
import os
from pyquery import PyQuery as pq
import re
from requests_html import HTMLSession


session = HTMLSession()

url1='http://www.comtrans.com.cn/about/honor.html'  #源网址


r=session.get(url1)
pic1=r.html.xpath('//img/@src')
print('图片的数量： ',len(pic1))
for i in range(len(pic1)):
    print('获取图片的网址：',pic1[i])
    if 'http' in pic1[i]:
        y=requests.get(pic1[i])
        path = os.getcwd() +  pic1[i].split("/")[-1]
        print(path)
        with open(path,"wb") as f:
            f.write(y.content)
    # else:
    #     print('不完整的http： ',pic1[i])



# def extract_img(tag) :
#     preg_match_all('/(id|alt|title|src)=("[^"]*")/i', tag, matches);
#     $ret = array();
#     foreach($matches[1] as $i => $v) {
#         $ret[$v] = $matches[2][$i];
#     } 
#     return $ret;
# }
 
# $img_tag = '<img src="/images/honor_img8.jpg" width="173" height="130" alt="公司营业执照" onerror="lods(this)">';
 
# $atts = extract_img($img_tag);
# print_r($atts)