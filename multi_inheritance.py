'''
class Mom:
    def swim(self):
        print('수영을 잘한다.')
        
class Dad:
    def run(self):
        print("달리기를 잘한다.")

class Athlete(Mom, Dad):
    def __init__(self, name):
        self.name = name
        print(f"운동 선수 {self.name}이 생성되었습니다.")
        
    def compete(self):
        print(f"{self.name}이 시합에 참가합니다.")
        
athlete1 = Athlete("철인")
athlete1.swim()
athlete1.run()
athlete1.compete()
print()
'''
'''
class Flyer :
    def fly(self):
        print("하늘을 날 수 있다.")
        
class Runner :
    def run(self):
        print("달릴 수 있다.")
        
class Pegasus(Flyer, Runner) :
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"내 이름은 {self.name}입니다.")
        
    def fly(self) :
        print(f"{self.name}이 하늘을 날 수 있습니다.")
        
pegasus1 = Pegasus("페가수스")
pegasus1.fly()
pegasus1.run()
pegasus1.introduce()
'''
# 부모클래스 > Camera, Message, Internet, Game
# shooting, sending_message, search_internet, play_game
# 사직을 찍습니다.....
# 자식 클래스 > smartphone
# 속성으로 브랜드, 모델명
# 메서드 display_info > 브랜드랑 모델명 출력

class Camera :
    def shooting(self):
        print("사진을 찍습니다.")
        
class Message :
    def sending_message(self):
        print("메시지를 보냅니다.")
        
class Internet :
    def search_internet(self):
        print("인터넷을 검색합니다.")
        
class Game :
    def playing_game(self):
        print("게임합니다.")
        
class Smartphone(Camera, Message, Internet, Game) :
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def display_info(self):
        print(f"브랜드: {self.brand}, 모델명: {self.model}")
        
    def sending_message(self):
        print('카톡을 전송합니다.')
        
    def shooting_search(self):
        self.shooting()
        self.search_internet()
        
smartphone1 = Smartphone("애플", "아이폰")
smartphone1.display_info()
smartphone1.sending_message()
smartphone1.shooting_search()
    
        

