import sys
sys.path.insert(0, '/Users/kwonhyunah/Desktop/SBAPROJECTS')
from titanic.entity import Entity
from titanic.service import Service

class Controller:
    def __init__(self):
        pass

    def preprocessing(self, train, test):
        service = self.service
        this = self.entity
        this.train = service.new_model(train) #payload
        this.test = service.new_model(test)
        return this

    def modeling(self, train, test):
        service = self.service
        this = self.preprocessing(train, test)
        print('훈련 컬럼: {this.train.columns}')
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def learning(self):
        pass

    def submit(self):
        pass
    
if __name__ == '__main__':
    api = Controller()
    service = Service()
    service.naver_cartoon('https://comic.naver.com/webtoon/weekday.nhn')