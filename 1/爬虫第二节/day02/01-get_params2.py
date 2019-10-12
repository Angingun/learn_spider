import urllib.request
import urllib.parse
import string


def get_params():
    url = "http://www.baidu.com/s?"

    params = {"wd": "中文", "key": "zhang", "value": "san"}
    str_params = urllib.parse.urlencode(params)  # 连接+转译
    print(str_params)
    final_url = url + str_params
    print(final_url)

    response = urllib.request.urlopen(final_url)

    data = response.read().decode("utf-8")

    print(data)


get_params()
