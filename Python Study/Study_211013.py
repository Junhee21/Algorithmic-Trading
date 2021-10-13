# 21 10 13
# 파이썬을 이용한 비트코인 자동매매 3장
# Python = 객체 지향 프로그래밍 Object Oriented Programming


class Supermario: # Supermairo라는 이름의 class 선언
    Name = "default" # 멤버변수 = 변수 = 데이터
    def __init__(self): # 멤버함수 = 함수 = method
        self.pos = 0
    def forward(self):
        self.pos = self.pos + 30

# class는 데이터와 이를 처리하는 함수를 묶어서 하나의 타입으로 정의한 것
# class 안의 데이터(변수)와 함수(method)를 통틀어 attribute(속성) 이라고 함

mario = Supermario()
# RHS : Supermario type의 객체 생성
# LHS : 생성한 객체를 변수 mario가 바인딩, mario는 supermario의 인스턴스(instance)
#인스턴스/객체/오브젝트 다 비슷한 뜻

mario.forward() # 해당 class의 attrubue 사용 가능 / 여기서 forward는 method
print(mario.pos)


print(dir(Supermario)) # class 안에 내장된 메소드, 상태 반환
print(id(Supermario))  # instance 주소값


# example
class OrderCafe:
    dessert = "none"
    def __init__(self, coffee): # __init__ : 객체 생성시 자동으로 호출되는 method
        self.coffee = coffee
        self.shot = 0 
    def add_shot(self, num): # self.add_shot을 통해 호출 <-> __init__과 차이
        self.shot += num
        self.test = "hello"
    def order_dessert(self, A):
        self.dessert = A
    def where_bathroom():
        print("There")
        
jun = OrderCafe("choco") #instance 생성
# jun.where_bathroom() error
#   jun.where_barthroom()은 자동적으로 OrderCafe.where_bathroom(jun)이 되지만
#   method 정의를 보면 전달인자가 0개다 따라서 전달인자가 초과되어 error가 난다.

print(jun.coffee)
print(jun.dessert)
jun.feeling = "happy"
print(jun.feeling)
# 변수 생성 방법
#   1. 37line  "attribute" = 기본값을 통해 선언가능
#   2. 40line  __init__ method 안에 선언가능
#   3. 45line class안에서 정의하지 않아도 객체.new속성 이런식으로 생성할 수 있다.
# print(jun.test) add_shot을 호출하지 않았기때문에 'test' attribute는 생성되지 않음

jun.dessert = "cake"
print("dessert = ", jun.dessert)
OrderCafe.order_dessert(jun, "pizza")
print("dessert = ", jun.dessert)

print("How much shot = ", jun.shot)
jun.add_shot(3)
OrderCafe.add_shot(jun, 3)
print("How much shot = ", jun.shot)
# attribue 변경 방법
#   1. 59line 객체.속성(전달인자) 로 호출
#   2. 60line 처음 method선언 시 self를 이용하면, class이름을 통해 method 호출 가능
#       여기서 self는 구체적인 객체 의미
# OrderCafe.add_shot(5)
# self를 넣지 않아서 error
# 사실 코드상으론 add_shot의 처음 인자는 self이므로 5가 self에 해당하고 num에 해당하는 인자를 넣지 않아서 error



# 상속
class ABCD:
    def hello(self):
        print("hello")
    def bye(self):
        print("bye")

class abcd(ABCD): #class 선언시 기존 class의 속성을 상속받을 수 있다.
    def bye(self):
        print("byebye")

hi = abcd()
hi.goodnight = "goodnight"

# 속성 참조 순서
# 객체 내부에서 찾기 -> 해당 객체애 대한 class -> 상속받은 class

print(hi.goodnight) #객체 내부에 goodnight 속성 존재 -> 출력
hi.bye() # 해당 객체에 대한 class에 bye가 있기 때문에 byebye 출력
ABCD.bye(hi) # ABCD의 속성도 이용가능하다
hi.hello() # class 안에 없어서 상속받은 class 참조 -> 상속받은 class 안에 속성 존재 = 이용 가능



# meta class
# type이란

print(isinstance(mario, Supermario)) #mario는 Supermario type의 instance, Supermario = class
print(isinstance(str, type)) #str은 type type의 instance, type = class
print(type(mario))
print(type(Supermario))
print(type(int))

# meta class는 class의 class를 의미하는 개념이다
# 파이썬에선 type이 metaclass 의 일종이다
# 위의 type 함수와 meta class를 의미하는 type을 혼돈할 수 있지만, 같은 글자일 뿐 다른 의미\

# meta class도 class니까 class로 객체를 만드는 것처럼 metaclass로 class를 만들 수 있다.
a_class = type('a_class', (), {"A":100})
a_instance = a_class()
print(a_instance.A)