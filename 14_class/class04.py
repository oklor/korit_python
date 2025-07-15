# Book 클래스
# 제목과 저자 > title, author
# display_info > '제목:[제목], 저자: [저자]'
# Book 클래스의 객체 두 개 이상 하고 display 호출

class Book :
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f'제목: [{self.title}], 저자: [{self.author}]')

    def __del__(self) :
        print(f'[{self.title}]의 객체가 소멸되었습니다.')

book1 = Book('햇님 달님', '작자 미상')
book2 = Book('선녀와 나무꾼', '작자 미상')

book1.display_info()
book2.display_info()
