# pip install beautifulsoup4

from bs4 import BeautifulSoup

html_doc = """
<html><head>
<title id="one">The Dormouse's story</title>
</head>
<body>
<p class="story"><!--...--></p>
<p class="title">
    p标签的内容
    <b>The Dormouse's story</b>
</p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>


"""




# 1.转类型 bs4.BeautifulSoup'
soup = BeautifulSoup(html_doc, 'lxml')

# 2.通用解析方法

#  find--返回符合查询条件的 第一个标签对象
result = soup.find(name="p")
result = soup.find(attrs={"class": "title"})
result = soup.find(text="Tillie")
result = soup.find(
    name='p',
    attrs={"class": "story"},
)

# find_all--list(标签对象)
result = soup.find_all('a')
result = soup.find_all("a", limit=1)[0]
result = soup.find_all(attrs={"class": "sister"})

# select_one---css选择器
result = soup.select_one('.sister')

# select----css选择器---list
result = soup.select('.sister')  # 通过类名查找，其类属性为sister的标签
result = soup.select('#one')  # id属性选择器
result = soup.select('head title')  # 选择head标签下所有的title标签
result = soup.select('title,.title')
result = soup.select('a[id="link3"]')  # 选择a标签，其属性中存在id="link3"的所有标签

# 标签包裹的内容---list
result = soup.select('.title')[0].get_text()


# 标签的属性
# result = soup.select('#link1')[0].get('href')
print(result)





