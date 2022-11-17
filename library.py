class User:
    def __init__(self, name, roll, password) -> None:
        self.name = name
        self.roll = roll
        self.password = password
        self.borrow_book = []
        self.return_book = []
    def __repr__(self) -> str:
        return f'Name: {self.name}\nRoll: {self.roll}'

class Library:
    def __init__(self, books) -> None:
        self.book_list = books

all_users = []
library = Library({'English': 3, 'Bangla': 2, 'Math': 4})
current_user = None

while True:
    if current_user == None:
        print('Please Log In or Create Account (L/C)')
        option = input('L/C: ')
        if option == 'L':
            pass
        else:
            pass
    else:
        print(current_user)