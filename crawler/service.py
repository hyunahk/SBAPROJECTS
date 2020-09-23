from bs4 import BeautifulSoup
from urllib.request import urlopen
from pandas import DataFrame
import os, shutil

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
        self.soup = BeautifulSoup(response, myparser)
        return type(self.soup)

    def create_folder_weekend(self, foldername):
        weekday_dict = {'mon': '월요일', 'tue': '화요일', 'wed': '수요일', 'thu': '목요일', 'fri': '금요일', 'sat': '토요일', 'sun': '일요일'}
        self.weekday_dict=weekday_dict
        # shutil : shell utility : 고수준 파일 연산. 표준 라이브러리
        
        myfolder = 'd:\\imsi\\' # 유닉스 기반은 '/'이 구분자
        self.myfolder = myfolder

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
    
    def set_target(self):
        self.mytarget = soup.find_all('div', attrs={'class':'thumb'})
        return len(mytarget)

    def save_data(self, replace_str, mycolumns, filename):
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
        mylist=self.mylist
        Service.saveas_CSV(mycolumns,mylist,filename)
    
    def saveas_CSV(self, mycolumns, mylist, filename):
        myframe = DataFrame(mylist, columns = mycolumns)

        filename = 'cartoon.csv'

        myframe.to_csv(filename, encoding='utf-8', index=False)
        print(filename + ' 파일로 저장됨')
        print('finished')

    