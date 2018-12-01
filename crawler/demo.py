import urllib.request
import gzip



url = 'http://www.meituba.com/xinggan/'

response = urllib.request.urlopen(url)
packed_format = response.info()['Content-Encoding']  # 获取压缩方式
if packed_format == "gzip":
    response_bytes = response.read()
    res = gzip.zlib.decompress(response_bytes, 16 + gzip.zlib.MAX_WBITS)  # 解压
    print(res.decode('utf-8'))
