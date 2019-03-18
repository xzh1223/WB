# coding:utf-8
from requests_html import HTMLSession

session = HTMLSession()


def get_html(url):
    ctx = {}
    url_list = []
    title_list = []
    content_list = []
    description_list = []
    date_list = []
    r = session.get(url)
    a = r.html.find('div.article-item-box')
    i = 0
    for ai in a:
        i = i + 1
        if i == 1:
            continue
        url_item = ai.find('a', first=True).attrs['href']
        r_1 = session.get(url_item)
        a_1 = r_1.html.find('div.article_content', first=True).html
        # print(a_1)
        content_list.append(a_1)
        url_list.append(ai.find('a', first=True).attrs['href'])
        title_list.append(ai.find('h4', first=True).text)
        description_list.append(ai.find('p.content>a', first=True).text)
        date_list.append(ai.find('div.info-box>p>span', first=True).text)
    ctx['url'] = url_list
    ctx['title'] = title_list
    ctx['content'] = content_list
    ctx['description'] = description_list
    ctx['date'] = date_list
    return ctx
