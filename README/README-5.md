variable (변하는 상태) vs constant (변하지 않는 상태)

그중에서 variable은 분류가 가능합니다.
분류기준을 두고, 나누는데

크게 2분하면 category, nominal(=: name)
다시 cate는 ordinal(=: order), numeric (=: number)

그래서 결국은
ordinal, numeric, norminal
변수의 편집방향은 곧 위 3중에 한가지 선택사항으로 주관식 -> 객관식

이곳(확률통계코딩)은 정답보다는 적합하다. 라는 개념입니다.

embarked부터 할게요.
교과서 138보면 누락된 값 처리 방식이 나옵니다.
지금 이 embarked 지우면 안되고 즉 dropna를 쓰면 안되고 139페이지 대체하는 방식을 사용해야 합니다.

여기서 null값을 무엇으로 넣을 것인가?
평균값을 넣자고 책에 나와있음.

그러나 이 예제는 str, 평균을 구할 수 없음.
그래서 이렇게들 합니다.
가장 많이 승선한 항구로 대체하자.
물론 통계를 왜곡할 수 있지만 그 null의 수가 적으니 무시하자.
왜냐하면 빈값이 있으면 아예 그 변수를 사용할 수 없어서 그것보다는 차선을 택하자는 생각입니다.

이 예제에서는 사우스햄튼에서 승선객의 비율이 높아서 S로 대체하기로 합니다.

변수명은 ['변수명'], 변수값은 ['변수명':'변수값']

@staticmethod
    def sex_norminal(this) -> object:
        #male = 0, female = 1
        this.train['Sex'] = this.train['Sex'].map({'male': 0, 'female': 1})
        this.test['Sex'] = this.test['Sex'].map({'male': 0, 'female': 1})
        return this

코딩은 반복된 코드를 싫어합니다.

@staticmethod
    def sex_norminal(this) -> object:
        #male = 0, female = 1
        combine = [this.train, this.test] #train과 test가 묶입니다.
        sex_mapping = {'male':0, 'female':1}
        for dataset in combine:
            dataset['Sex'] = dataset['Sex'].map(sex_mapping)

        this.train = this.train
        this.test = this.test
        return this

Data 수집
- 방법론
- 정형 (csv) = 스키마구조 존재. computer 인식
- 비정형 () = 스키마구조 존재하지 않다. computer 인식불가
- 웹 -> 웹 클로링 ~> 브라우저, RE 정규표현식
- 문서 -> 텍스트 마이니 ~> RE 정규표현식
Data 정제, 정형화
Modeling
Learning
Machine
Evaluation

########  정규표현식 re  ########

?: unique
*: all
+: not null
{n} : counting