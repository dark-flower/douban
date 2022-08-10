import requests
from lxml import etree
import pymysql
sqldb = pymysql.connect(
    host='10.243.16.181',
    port=3306,
    user='root',
    password='Irs@jax234',
    database='Test',
)
cursor = sqldb.cursor()
cookies ={
    'bid': 'HQSwXiaoRrc',
    'll': '"108296"',
    'gr_user_id': '94f4749a-a9b6-4598-ab58-23d517d0e8ea',
    'viewed': '"27002046_2035179_1424314"',
    'push_doumail_num': '0',
    'push_noty_num': '0',
    'douban-fav-remind': '1',
    '_ga': 'GA1.2.1581341193.1652314972',
    '__gads': 'ID=0d028848c90e3416-2259b4b420d300e1:T=1652363988:RT=1652363988:S=ALNI_Mby0ItK0IvSE-Wqo9uCkwtnYIqwAw',
    '__yadk_uid': '1AJcX1ZJJ50zdatz96uXCun4aUC1FYsH',
    '_vwo_uuid_v2': 'DB79ADA625FD3C97E34609ADC9DE0132E|3ca63f1fba65914b286a33b19420b982',
    '_vwo_uuid_v2': 'DB79ADA625FD3C97E34609ADC9DE0132E|3ca63f1fba65914b286a33b19420b982',
    '__gpi': 'UID=00000549e8152e37:T=1652366539:RT=1656324747:S=ALNI_MZxly9sa8vGujaoySyOxoCH5JqrnQ',
    '__utmc': '30149280',
    'dbcl2': '"83647449:uN+ridoenwY"',
    'ck': 'Mx7d',
    '__utmv': '30149280.8364',
    '__utmz': '30149280.1659076376.114.13.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    '__utmc': '223695111',
    'ct': 'y',
    '__utma': '30149280.1581341193.1652314972.1659076376.1659079370.115',
    '__utmt': '1',
    '__utmb': '30149280.4.10.1659079370',
    '_pk_ref.100001.4cf6': '%5B%22%22%2C%22%22%2C1659079381%2C%22https%3A%2F%2Fwww.douban.com%2Fmisc%2Fsorry%22%5D',
    '_pk_id.100001.4cf6': '8f150069c8678129.1651838886.88.1659079381.1659076842.',
    '_pk_ses.100001.4cf6': '*',
    '__utma': '223695111.1748178438.1651838886.1659076376.1659079381.90',
    '__utmb': '223695111.0.10.1659079381',
    '__utmz': '223695111.1659079381.90.43.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/misc/sorry',
}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'bid=HQSwXiaoRrc; ll="108296"; _vwo_uuid_v2=D38696AF60AA385A64C3CFB63A1C1B2A3|2fe373ab83847bebf6c1bc403d605acc; gr_user_id=94f4749a-a9b6-4598-ab58-23d517d0e8ea; viewed="27002046_2035179_1424314"; push_doumail_num=0; push_noty_num=0; douban-fav-remind=1; _ga=GA1.2.1581341193.1652314972; __gads=ID=0d028848c90e3416-2259b4b420d300e1:T=1652363988:RT=1652363988:S=ALNI_Mby0ItK0IvSE-Wqo9uCkwtnYIqwAw; __yadk_uid=1AJcX1ZJJ50zdatz96uXCun4aUC1FYsH; __utmz=30149280.1654491806.67.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; dbcl2="83647449:L+Kssb5RQao"; __utmv=30149280.8364; ck=lF1w; __utma=30149280.1581341193.1652314972.1655107853.1655186880.85; __utmc=30149280; __utmt=1; __utmb=30149280.6.10.1655186880; __utma=223695111.1748178438.1651838886.1654849228.1655186914.73; __utmb=223695111.0.10.1655186914; __utmc=223695111; __utmz=223695111.1655186914.73.28.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1655186914%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=8f150069c8678129.1651838886.72.1655186916.1654849289.; __gpi=UID=00000549e8152e37:T=1652366539:RT=1655186916:S=ALNI_MZxly9sa8vGujaoySyOxoCH5JqrnQ',
    'Referer': 'https://movie.douban.com/subject/27046758/?from=showing',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Microsoft Edge";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

def fetch_movie_comments(movie_id):
    for i in range(0, 500):
        values_list=[]
        print('Scraping long comment page number:' + str(i + 1))
        params = {
            'sort': 'time',
            'start': str(20 * i),
        }
        suffix = 'insert into douban_movie_uid (movie_id,cid,user_name,time,rating,full_text,uid,down_vote,up_vote) values '
        response = requests.get('https://movie.douban.com/subject/'+movie_id+'/reviews', params=params, cookies=cookies, headers=headers).text
        html = etree.HTML(response)
        # print(response)
        review_list = html.xpath('.//div[@class="review-list  "]/div')
        # print(len(review_list))
        if len(review_list) == 0: break
        try:
            for item in review_list:
                cid = str(item.xpath('./@data-cid')[0])
                user_name = item.xpath('.//a[@class="name"]/text()')[0].strip().replace("'", "''")
                profile_link = item.xpath('.//a[@class="name"]/@href')[0].strip().replace("'", "''")
                uid=profile_link.split('/')[-2]
                time = item.xpath('.//span[@class="main-meta"]/text()')[0]
                rating = item.xpath('//span[contains(@class,"allstar")]/@title')[0]

                up_vote = item.xpath('.//a/span[contains(@id,"useful_count")]/text()')[0].strip()
                down_vote = item.xpath('.//a/span[contains(@id,"useless_count")]/text()')[0].strip()



                values = " ('" + str(movie_id) + "','" + str(cid) + "','" + user_name + "','" + time + "','" \
                         + rating + "','" + profile_link + "','" + uid + "','" + down_vote + "','" + up_vote + "')"
                # values_list.append(values)
                sql = suffix + values
                print(sql)
                    # pass
                cursor.execute(sql)
                sqldb.commit()
        except:
            pass

if __name__=="__main__":
    import os
    f = open('./comment_task', 'r', encoding='utf-8')
    for item in f:
        movie_id = item.strip()
        print(movie_id)
        fetch_movie_comments(movie_id)

