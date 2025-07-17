# ValueError, ZeroDivisionError // print(10/0)

'''
try :
    print(10/0) # 예외가 발생할 것 같은 거
except:
    print('예외 발생')

try :
    num = int(input('숫자를 입력해 주세요:'))
    print(10/num)
except ValueError : #값 데이터 오류
    print('문자말고 숫자를 넣으세요')
except ZeroDivisionError :
    print('0말고 다른 거 넣으세요')
'''
from traceback import print_tb

# IndexError, ValueError
'''
try :
    my_list = [1,2,3]
    index = int(input('리스트에서 가져올 인덱스 :'))
    print(my_list[index])
except ValueError :
    print("숫자만 입력하세요")
except IndexError :
    print("존재하지 않는 인덱스입니다.")
'''

# 파일 입출력 예외 처리 : FileNotFoundError
'''
file = None

try :
    file =  open("hi.txt", "r", encoding="utf=8")
    content = file.read() # 파일의 내용을 읽어온다
    print(content)
except FileNotFoundError :
    print("그런 파일은 없음")
finally : # 오류가 뜨던 말던 무조건 실행됨
    if file is not None and not file.closed :
        file.close()
        print("정상적으로 파일이 닫혔습니다")
    elif file is None :
        print("애초에 열리지 않음")
'''

# 리스트 요소 5개 선언하고 index로 찾는 로직
# IndexError, ValueError 예외 처리
# 정상적이면 해당 리스트 값 출력 else
# 마지막은 항상 끝!! 출력 finally
'''
try :
    numlist = [1,2,3,4,5]
    index = int(input("인덱스를 입력하세요"))
    result = numlist[index]
except ValueError as message:
    print("숫자를 입력하세요")
    print(message)
except IndexError as message:
    print("잘못된 인덱스 숫자입니다.")
    print(message)
else :
    print(result)
finally:
    print("끝!")
'''

# raise 키워드 : 강제로 예외 발생시킴
# 특정 조건에서 개발자가 직접 예외를 발생시키는 데 사용
'''
try :
    age = int(input("나이 입력 : "))

    if age < 0 or age > 150 :
        raise Exception("0이상 150 미만 숫자만 입력하세요.") # 내가 직접 에러메시지 입력한 거, Exception이 상위 클래스 그래서 Value도 잡음
except Exception as e :
    print(e)
else : # 정상적이면 실행됨
    print(f"입력된 나이: {age}")
finally :
    print("끝!")
'''

# 사용자 정의 예외 클래스 / 따로 정의하는 Exception을 실행시킬 수 있음
'''
class AgeException(Exception) :
    def __init__(self):
        super().__init__("0이상 150미만 숫자만 입력하세요")

try :
    age = int(input("나이를 입력하세요"))

    if age < 0 or age > 150 :
        raise AgeException()

except AgeException as e :
    print(e)
else :
    print(f"나이 : {age}")
finally:
    print("끝!")
'''

# 출금할 때 잔액이 부족하면 발생되는 예외
# FundsError > 잔액이 부족합니다. 현재 잔액: ***원, 출금 시도 금액: ***원1
# Account 클래스 만들고 withdraw(출금)
# 출금할 때 잔액이 부족하면 FundsError를 발생

'''
class Account :
    def __init__(self, owner, money):
        self.owner = owner
        self.money = money
        print(f"현재 잔액은 {self.money}입니다.")
    def withdraw(self):
        try :
            withdraw_money = int(input('출금하실 금액을 입력하세요'))
            if withdraw_money > self.money :
                raise Exception (f"잔액이 부족합니다. 현재 잔액: {self.money} 출금 시도 금액: {withdraw_money}")
            elif withdraw_money <= 0 :
                raise Exception('잘못된 숫자임')
        except ValueError :
            print("숫자를 입력하세요")
        except Exception as e :
            print(e)
        else :
            self.money = self.money - withdraw_money
        finally:
            print(f"현재 잔액: {self.money}")


account1 = Account('고객님')
account1.withdraw()
account1.withdraw()
'''
'''
class FundsError(Exception) :
    def __init__(self, balance, amount): # 생성자에서 현재 잔액과 출금 시도 금액을 받음
        super().__init__(f"잔액이 부족합니다. 현재 잔액: {balance}원, 출금 시도 금액: {amount}원")

class BankAccount :
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        try :
            if amount > self.balance :
                raise FundsError(self.balance, amount)
        except FundsError as e :
            print(e)
        else :
            self.balance -= amount
            print(f"정상적으로 출금되었습니다. 잔액 : {self.balance}")

account1 = BankAccount(100000)
account1.withdraw(50000)
account1.withdraw(80000)
'''

# 딕셔너리 요소 찾기
# 딕셔너리 키를 입력받음(숫자로)
# result 변수에 해당 키의 값을 넣음
# 예외 처리 > 해당 키가 존재하지 않을 때 "KeyError" 처리: "해당 키는 존재하지 않습니다
# 숫자가 아닌 문자를 입력했을 때 ValueError 처리 "숫자를 입력해주세요
# 정상적으로 실행되면 해당 키의 값을 넣어둔 result 출력
# 마지막은 항상 "완료!"를 출력

poke_dict = dict({
    1: '파이리',
    2: "꼬부기",
    3: '피카츄',
    4: "라이츄"
})


try :
    key_poke_dict = int(input("key 값을 입력하세요"))
except KeyError :
    print("해당 키는 존재하지 않습니다.")
except ValueError :
    print("숫자를 입력하세요")
else :
    print(poke_dict[key_poke_dict])
finally:
    print("완료!")
















