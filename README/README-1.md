Obejct = 기능(function) + 속성(Property, Attribute, Feature) => 파라미터(AI파트)
하나의 {...}에 같이 있음
() 라운드 

위키 Google Boo1이란 사람 검색...
T, F 판단 1850년 --> 전선 (모스부호) --> 컴퓨터

on, off의 개념이다.
요소가 존재, 비존재로 종류가 나뉜다. -> Decision Tree (Origin AI 알고리즘)

Q 객체지향 vs 함수형 프로그래밍을 구분하는 기준은 무엇이 있고 없고 인가?
A ... 속성이 있으면 객체지향, 없으면 함수형 프로그래밍

class Calculator:
    def __init__(self, num1, num2):
    # 생성자 함수 --> 인스턴스(객체) 만드는 함수 __ 언더스코어 라고 합니다. 2개를 사용,
        self.num1 = num1
        self.num2 = num2
    
if __name__ == '__main__':
    calc = Calculator(6, 2) # num1 = 4, num2 = 6
    sumResult = calc.sum()
    subResult = calc.sub()
    mulResult = calc.mul()
    divResult = calc.div()
    print('덧셈결과 {}'.format(sumResult))
    print('뺄셈결과 {}'.format(subResult))
    print('곱셈결과 {}'.format(mulResult))
    print('나눗셈결과 {}'.format(divResult))