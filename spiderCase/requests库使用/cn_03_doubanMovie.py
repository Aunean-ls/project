import requests
import csv
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'
}


def response_url(url):
    data_list = []
    for i in range(0, 100, 20):
        params = {
            'type': 'movie',
            'tag': '热门',
            'sort': 'recommend',
            'page_limit': '20',
            'page_start': i
        }
        response = requests.get(url=url, params=params, headers=headers).json()
        # print(response)
        for movie in response['subjects']:
            title = movie['title']
            score = movie['rate']
            video_url = movie['url']
            img = movie['cover']

            # data = {
            #     'title': title,
            #     'score': score,
            #     'video_url': video_url,
            #     'img': img
            # }
            # print(data)
            # data_list.append(data)

            with open('doubanMovie.txt', 'a', encoding='utf-8') as f:
                f.writelines([title+'\t', score+'\t', video_url+'\t', img+'\n'])

            path = 'douban_img/'
            if not os.path.exists(path):
                os.makedirs(path)
            img_data = requests.get(url=img, headers=headers).content
            img_name = img.split('/')[-1]
            with open(path + img_name, 'wb') as f:
                f.write(img_data)
    # insert_csv(data_list)


# def insert_csv(data_list):
#     with open('./豆瓣.csv', 'w', encoding='utf-8', newline='') as f:
#         fieldnames = ['title', 'score', 'video_url', 'img']
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(data_list)


if __name__ == '__main__':
    url = 'https://movie.douban.com/j/search_subjects?'
    response_url(url)
