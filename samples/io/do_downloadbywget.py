import wget
import tempfile
import os

url = 'https://p0.ifengimg.com/2019_30/1106F5849B0A2A2A03AAD4B14374596C76B2BDAB_w1000_h626.jpg'

# 获取文件名
file_name = wget.filename_from_url(url)
print(file_name)  #1106F5849B0A2A2A03AAD4B14374596C76B2BDAB_w1000_h626.jpg

# 下载文件，使用默认文件名,结果返回文件名
file_name = wget.download(url)
print(file_name) #1106F5849B0A2A2A03AAD4B14374596C76B2BDAB_w1000_h626.jpg

# 下载文件，重新命名输出文件名
target_name = 't1.jpg'
file_name = wget.download(url, out=target_name)
print(file_name) #t1.jpg

# 创建临时文件夹，下载到临时文件夹里
tmpdir = tempfile.gettempdir()
target_name = 't2.jpg'
file_name = wget.download(url, out=os.path.join(tmpdir, target_name))
print(file_name)  #/tmp/t2.jpg
