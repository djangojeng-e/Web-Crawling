import requests
from bs4 import BeautifulSoup


counter = 0

html = open('webtoon_list.html', 'rt').read()
soup = BeautifulSoup(html)

def get_webtoon_detail(title_name):     # 웹툰 디테일 찾기 
    html = open('episode_list.html', 'rt').read()
    soup = BeautifulSoup(html)
    print(f'# 정보 ({title_name})')
    div_comicinfo = soup.select_one('div.comicinfo')
    div_detail = div_comicinfo.select_one('div.detail')

    title = div_detail.select_one('h2').contents[0]
    author = div_detail.select_one('span.wrt_nm').get_text(strip=True)
    description = div_detail.select_one('p.txt').get_text('\n', strip=True)

    # genre, age
    div_detail_info = div_detail.select_one('p.detail_info')
    genre = div_detail_info.select_one('span.genre').get_text(strip=True)
    age = div_detail_info.select_one('span.age').get_text(strip=True)

    print(f'Title : {title}\n Description : {description}\nAuthor : {author}\nGenre : {genre}\nAge : {age}')

    print("0 : 이전으로 돌아가기")

    command = int(input("커맨드를 입력하세요 : "))
    if command == 0: 
        return      

def webtoon_search():                   # 웹툰 찾기 
    title = input("웹툰명을 입력하세요 : ")
    soup = BeautifulSoup(open('webtoon_list.html', 'rt').read())

    a_list = soup.select('a.title[title*="{}"]'.format(title))

    title_list = []         # TITLE명을 가지는 리스트를 생성 
    print("# 정보를 가져올 웹툰 선택")

    for a in a_list: 
        title = a.get_text(strip=True)
        title_list.append(title)        # Title명을 리스트에 추가

    title_list = set(title_list)        # 중복되는 원소 제거 
    title_list = list(title_list)       # 중복되는 원소 제거 
    


    title_dict = {}                     # title의 키와 벨류를 가지는 사전 생성 

    for index, titles in enumerate(title_list, 1):
        title_dict[index] = titles     # 사전에 원소를 추가 
        print(index, titles)

    # 사전에 모든 요소를 추가했으니, 이제 키 벨류를 가지고 다음 함수로 넘길 인자를 
    # 마음대로 access 할수 있습니다. 
        
    print("0 : 이전으로 가기")

    command = int(input("명령키를 입력하세요 : "))

    if command == 0:
        global counter 
        counter = 0 
    else:
        show_title = title_dict[command]
        get_webtoon_detail(show_title)


def episode_list():                     # 에피소드 리스트 찾기 
    title_id = 651673 
    url = f'https://comic.naver.com/webtoon/list.nhn?titleId={title_id}'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html)
    
    results = []
    table = soup.select_one('table.viewList')
    tr_list = table.select('tr')
    for tr in tr_list:
        # title클래스를 가진 td
        td_title = tr.select_one('td.title')
        # 가 없으면 넘어간다
        if not td_title:
            continue

        title = td_title.get_text(strip=True)

        td_rating = tr.select_one('td:nth-child(3)')
        rating = td_rating.select_one('strong').get_text(strip=True)

        td_date = tr.select_one('td.num')
        date = td_date.get_text(strip=True)

        episode = {
            'title': title,
            'rating': rating,
            'date': date,
        }
        results.append(episode)
    print(results)
    

def webtoon_search_episodes():          # 웹툰 에피소드 찾기 위해 웹툰명 검색 
    title = input("웹툰명을 입력하세요 : ")
    soup = BeautifulSoup(open('webtoon_list.html', 'rt').read())

    a_list = soup.select('a.title[title*="{}"]'.format(title))

    title_list = []         # TITLE명을 가지는 리스트를 생성 
    print("# 정보를 가져올 웹툰 선택")

    for a in a_list: 
        title = a.get_text(strip=True)
        title_list.append(title)        # Title명을 리스트에 추가

    title_list = set(title_list)        # 중복되는 원소 제거 
    title_list = list(title_list)       # 중복되는 원소 제거 
    


    title_dict = {}                     # title의 키와 벨류를 가지는 사전 생성 

    for index, titles in enumerate(title_list, 1):
        title_dict[index] = titles     # 사전에 원소를 추가 
        print(index, titles)

    # 사전에 모든 요소를 추가했으니, 이제 키 벨류를 가지고 다음 함수로 넘길 인자를 
    # 마음대로 access 할수 있습니다. 
        
    print("0 : 이전으로 가기")
    command = int(input("명령을 입력하세요 : "))
    if command == 0:
        return 
    else:
        episode_list()

      
while counter == 0:
    print("## 웹툰 크롤러 ##\n1.정보\n2.에피소드 목록\n0. 나가기")
    command = int(input("입력 : "))
    if command == 0: 
        break
    elif command == 1: 
        webtoon_search()
    elif command == 2: 
        webtoon_search_episodes()

