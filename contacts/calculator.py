class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def sum(self):
        return self.num1 + self.num2
    
    def sub(self):
        return self.num1 - self.num2
    
    def mul(self):
        return self.num1 * self.num2
    
    def div(self):
        return self.num1 / self.num2

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
    