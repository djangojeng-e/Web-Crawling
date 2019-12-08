# Section02-1 
# 파이썬 크롤링 기초 
# urllib 사용법 및 기본 스크래핑 

import urllib.request as req 



# 파일 URL
img_url = 'http://cafefiles.naver.net/20120611_289/kkas_nknk55_1339391180925I3qnD_JPEG/%B0%ED%BE%E7%C0%CC9.jpg'
html_url = 'http://google.com'

# 사이트마다 소스코드를 받으면서 스크래핑 진행 
# 다운받을 경로 

save_path1 = 'test1.jpg'
save_path2 = 'index.html'

# 예외처리 

try: 
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print('Download Failed')
else:
    # Header 정보 출력 
    print(header1)
    print(header2)

# http 통신은 한번 연결후 끊기면 끝나는 구조 

