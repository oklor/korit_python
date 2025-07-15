# Person >나이, 이메일, 이름 //name = 홍길동
# introduce 메서드 > 자신을 소개하는 메서드

class Person :
    def __init__(self, age, email, name = '홍길동'):
        self.age = age
        self.email = email
        self.name = name


    def introduce(self):
        print(f"안녕하세요 제 이름은 {self.name}입니다. 나이는 {self.age}이고 이메일은 {self.email}입니다.")

person1 = Person(26, 'python@naver.com','asdf7')

person1.introduce()

person2 = Person(20, 'gildong@naver.com')
person2.introduce()

person2.address = '부산' # person2 객체에 address라는 새로운 속성을 동적으로 추가
print(person2.address)

setattr(person1, 'address', '부산시')
print(person1.address)