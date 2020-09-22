from bs4 import BeautifulSoup
from urllib.request import urlopen
from pandas import DataFrame

class Service:
    def __init__(self):
        pass
    
    def bugs_music(self):
        pass
    
    def naver_movie(self):
        pass

    def naver_cartoon(self,url):
        myparser = 'html.parser'
        myurl = 'https://comic.naver.com/webtoon/weekday.nhn'
        response = urlopen(myurl)
        soup = BeautifulSoup(response, myparser)
        print(type(soup))

    def create_folder_weekend(self, myweekday, mytitle):
        weekday_dict = {'mon': '월요일', 'tue': '화요일', 'wed': '수요일', 'thu': '목요일', 'fri': '금요일', 'sat': '토요일', 'sun': '일요일'}

        # shutil : shell utility : 고수준 파일 연산. 표준 라이브러리
        import os, shutil
        myfolder = 'd:\\imsi\\' # 유닉스 기반은 '/'이 구분자

        try:
            if not os.path.exists(myfolder):
                os.mkdir(myfolder)

            for mydir in weekday_dict.values():
                mypath = myfolder + mydir

                if os.path.exists(mypath):
                    # rmtree : remove tree
                    shutil.rmtree(mypath)

                os.mkdir(mypath)

        except FileExistsError as err:
            print(err)
    
    def save_data(self):
        mytarget = naver_cartoon.soup.find_all('div', attrs={'class':'thumb'})
        mylist = [] # 데이터를 저장할 리스트
        for abcd in mytarget:
            myhref = abcd.find('a').attrs['href']
            myhref = myhref.replace('/webtoon/list.nhn?', '')
            result = myhref.split('&')
            mytitleid = result[0].split('=')[1]
            myweekday = result[1].split('=')[1]

            imgtag = abcd.find('img')
            mytitle = imgtag.attrs['title'].strip()
            mytitle = mytitle.replace('?', '').replace(':', '')

            mysrc = imgtag.attrs['src']

            create_folder_weekend(mysrc, myweekday, mytitle)
            sublist = []
            sublist.append(mytitleid)
            sublist.append(myweekday)
            sublist.append(mytitle)
            sublist.append(mysrc)
            mylist.append(sublist)
        return mylist
    
    def fruit(self):
        html = open('fruits.html', 'r', encoding='utf-8') # fruits.html
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.select_one('body')
        ptag = body.find('p')
        ptag['id'] = 'apple'
        body_tag = soup.find('body')
        idx = 0
        for child in body_tag.children:
            idx += 1
            print(str(idx) + '번째 요소 :', child)
        mydiv = soup.find('div')
        print(mydiv)
        print('나의 부모는')
        print(mydiv.parent)
        mytag = soup.find('p', attrs={'class':'hard'})
        parents = mytag.find_parents()
        for p in parents:
            print(p.name)
        return ptag, ptag['class'], ptag['align'], ptag['id'], body_tag, mytag, mytag.find_parent()
    
    def exception(self):
        try:
            x = 4
            y = 0

            mydict = {'a':10}

            print(mydict['b'])

            mylist = [1, 2, 3]
            print(mylist[4])

            z = x / y
            print(z)

        except ZeroDivisionError as err:
            print('0으로 나누시면 안됩니다.')
            print(err)

        except IndexError as err:
            print('인덱스 범위 관련 오류 발생')
            print(err)

        except KeyError as err:
            print('사전에 해당 키가 없습니다')
            print('찾고자 하는 키')
            print(err)

        except Exception as err:
            print('기타 나머지 예외 발생')
            print(err)

        else:
            print('예외가 없으면 이 라인이 실행됩니다.')

        finally:
           print('예외 발생 여부와 상관이 없이 무조건 실행됩니다.')
    