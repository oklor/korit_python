# Account 클래스 > 계좌 정보
# owner, balance > 잔액은 0으로 초기화
# deposit 메서드를 추가해 잔액을 증가시키고 증가도니 잔액을 출력
# withdraw 메서드를 추가해 잔액을 감소시키고 감소된 잔액을 출력

class Account :
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        print(f'안녕하세요 {self.owner}님 현재 잔액은 {self.balance}입니다.')

    def deposit(self, deposit_money):
        if deposit_money > 0 :
            print(f'입금하실 금액은 {deposit_money}')
            self.balance = self.balance + deposit_money
            print(f'현재 잔액은 {self.balance}입니다.')
        else :
            print('잘못된 금액입니다.')

    def withdraw(self, withdraw_money):
        if withdraw_money <= 0 :
            print('잘못된 금액입니다.')

        elif withdraw_money <= self.balance :
            print(f'출금하실 금액은 {withdraw_money}')
            self.balance = self.balance - withdraw_money
            print(f'현재 잔액은 {self.balance}입니다.')

        else : # 출금액이 0 이상이고 잔액보다 출금액이 많은 상황
            print(f"잔액이 부족합니다. 현재 잔액은 {self.balance}입니다.")



Account1 = Account('이름',50)

Account1.deposit(7)
Account1.withdraw(41)
Account1.deposit(50)
