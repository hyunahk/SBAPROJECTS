chromdriver

현재 크롤링은 정해진 url만 처리하죠?
이런 상태를 static 입니다.

dynamic은 payload로 url을 주면 재활용해서 서로 다른 경과를 만드는 것입니다.

=================================

MVC 코딩하는 순서...

구조 (frame)를 만듭니다
1. model 을 만들고 view 를 만들어서 controller로 연결(network) 한다
model = entity + service 속성 + 기능 => 모델객체
view = Reactjs 로 전환된다

model 과 view 가 언어가 달라요...

한국인과 미국인이 만났는데 서로 언어를 모름.
통역을 불러서 data를 주고 받을 수 있다
controller가 통역의 역할을 하는데 통역하는 사람의 국적이 한국인.

python과 javascript가 만났어요. 서로 syntax가 달라요...
그래서 transfer을 불러서 data를 주고 받을 수 있다.
flask 가 transfer의 역할을 해요. 그런데 통역하는 객체의 언어가 python 입니다...

각각하는 일이 달라요...
뇌의 역할을 하는 모델이 python입니다.

플젝을 만드는데 칩을 이식하면 단기간에 성능이 올라간답니다.
유료칩(스타트업)도 있고, 무료칩도 있는데 이 중 성능이 검증된 유명한 것이 tensorflow(주 구글), 파이토치(주 페북)이 양강이라고 합니다.

이 과정은 텐서플로 사용법을 배우는 과정으로 편성되어서,

코딩 컨벤션을 결국 텐서플로에 최적화 시켜야 합니다.
그래서 객체지향(class 단위) 방식으로 바꾼 겁니다.

인공지능을 담당하는 미세조정 파트는 텐서플로에 의존한다.

이제 구조(뼈대)는 잡았으니, 디테일한 파트인 알고리즘으로

machine vs model difference

컴공 상태를 통해 구분 state
머신은 러닝을 합니다.
모델은 러닝을 하지 않아요.

우리가 모델을 만들어요.
그런데 모델을 러닝시키는 것이 아니라 머신을 러닝시킵니다.
그러면 이상하잖아요.
머신은 학습한 객체라고 했는데...

학습을 이미 한 객체일까요 학습을 할 객체일까요?

그리고 알고리즘을 공부하는 목적이 이곳에서 (머신러닝에서는) 본인이 알고리즘을 공부하는 것이 아니라
내가 만든 머신을 공부시키는 것이다란 개념을 잡고 있어야 합니다.

이 머신을 신생아(baby)로 비유할 수 있어요.
그리고 개발자의 평가는 이 baby가 똑똑해져서 내는 performance가 나의 성과가 됩니다.

허사비스가 이세돌과 바둔둔게 아니라 알파고가 바둑 둔거죠.

우리의 고민은 어떤 알고리즘을 우리가 만드는 모델에 주입을 시킬 것인가 하는 지점입니다.

이제 모델을 만들려고 합니다.
첫번째는 모델을 훈련시킬 데이터에서 쓰레기값을 제거하는 겁니다.
이 머신은 타이타닉의 정보를 통해 만약 A라는 가상의 인물이 당시 1912년 침몰 당시 타이타닉에 승선했다면 생존확률은 어찌 될 것인가?
더 나아가 현재 승객 안전을 위한 조치를 어떻게 하면 비슷한 사고 발생시 생존률을 올릴 수 있을 것인가 하는 문제로 귀결될 수도 있습니다.

우리는 단순하게 생존확률 판단 머신만 만들겠습니다.

1순위 작업은 feature를 줄이는 것.