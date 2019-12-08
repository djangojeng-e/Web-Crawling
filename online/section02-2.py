# Section02-2 
# 파이썬 크롤링 기초 
# URLOPEN 함수 기초 사용법 

import urllib.request as req 
from urllib.error import URLError, HTTPError 

# 다운로드 경로 및 파일명 

path_list = ["test1.jpg", "index.html"]

# 다운로드 리소스 url 

target_url = ["http://post.phinf.naver.net/MjAxOTA2MDdfMTU0/MDAxNTU5ODcxODc3NTU0.4SFrd6PeWF62ewm21H4nu5xae67wvpvVe2VjagQzilcg.iYBSJe5CZ3E_j2wBY5dlWaLHyS2YujdK0ooqPOOvFNkg.JPEG/ILFVJ_GQGHr0HniSIzDBBbUbrjpg.jpg", "http://google.com"]

for i, url in enumerate(target_url): 
    # ㅇㅖ외처리 

    try:
        # 웹 수신 정보 읽기 
        response = req.urlopen(url) 

        # 수신 내용 
        contents = response.read()

        print("----------------------------")

    except HTTPError as e: 
        print("Download failed.")
        print("HTTPError code : ", e.code)
    except URLError as e:
        print("Download failed.")
        print("URL Error Reason: ", e.reason)

    #성공 
    else:
        print()
        print("Download Succeeded.")

    # 상태 정보 중간 출력 

    print('Header Info- {} : {}'.format(i, response.info()))
    print('HTTP Status Code: {}'.format(response.getcode()))
    print()

    with open(path_list[i], 'wb') as c:
        c.write(contents)



print("----------------------------")