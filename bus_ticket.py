class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

class Bus:
    def __init__(self, coach, driver, arrival, departure, from_des, to_des) -> None:
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to_des = to_des
        self.seat = ['Empty' for i in range(20)]

class Company:
    total_bus = 0
    total_bus_list = []

    def install(self):
        coach_no = input('Enter Coach No: ')
        flag = 1
        for bus in self.total_bus_list:
            if coach_no == bus['coach']:
                print("Bus already installed")
                flag = 0
                break
        if flag:
            driver = input('Enter Driver Name: ')
            arrival = input('Enter Bus Arrival Time: ')
            departure = input('Enter Departure Time: ')
            from_des = input('Enter Bus Start From: ')
            to_des = input('Enter Bus To Destination: ')
            self.new_bus = Bus(coach_no, driver, arrival, departure, from_des, to_des)
            self.total_bus_list.append(vars(self.new_bus))
            print("\nBus successfully installed\n")
        

class Counter(Company):
    user_list = []
    def reservation(self):
        bus_no = input('Enter Bus Number: ')
        for bus in self.total_bus_list:
            if bus_no == bus['coach']:
                passenger_name = input('Enter Your Name: ')
                seat_no = int(input('Enter Your Seat No: '))
                if seat_no-1 > 20:
                    print('Only 20 seats are available.')
                elif bus['seat'][seat_no-1] != 'Empty':
                    print('Seat Already Booked!')
                else:
                    bus['seat'][seat_no-1] = passenger_name
            else:
                print('No Bus Available.')

    def show_bus_info(self):
        bus_no = input('Enter Bus No: ')
        for bus in self.total_bus_list:
            if bus_no == bus['coach']:
                print('*'*50)
                print()
                print(f"{' '*10} {'#'*10} BUS INFO {'#'*10}")
                print(f"Bus number : {bus_no} \t\tDriver : {bus['driver']}")
                print(
                    f"Arrival : {bus['arrival']} \t\t\tDeparture Time : {bus['departure']} \nFrom : \t{bus['from_des']} \t\t\tTo : \t{bus['to_des']}")
                print()
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    print()
                print('*'*50)
            else:
                print('No Bus Available.')
                break
    def get_users(self):
        return self.user_list
    def create_account(self):
        name = input("Enter your username : ")
        password = input("Enter your password : ")
        self.new_user = User(name, password)
        self.user_list.append(vars(self.new_user))
        print("Account Created Successfully\n")
    def available_bus(self):
        if len(self.total_bus_list) == 0:
            print("No Buses available\n")
        else:
            print('*'*50)
            for bus in self.total_bus_list:
                print()
                print(f"{' '*10} {'#'*10} BUS {bus['coach']} INFO {'#'*10}")
                print(f"Bus number : {bus['coach']} \tDriver : {bus['driver']}")
                print(
                    f"Arrival : {bus['arrival']} \tDeparture Time : {bus['departure']} \nFrom : \t{bus['from_des']} \t\tTo : \t{bus['to_des']}")
                print()
            print('*'*50)


while True:
    bus_company = Company()
    bus_counter = Counter()
    print(f"\n{' '*10}Welcome to BUS TICKET BOOKING SYSTEM")
    print("1. Create an account\n2. Login to your account \n3. EXIT\n")
    user_input = int(input("Enter you choice : "))
    if user_input == 3:
        break
    elif user_input == 1:
        bus_counter.create_account()
    elif user_input == 2:
        username = input('Enter Your Username: ')
        password = input('Enter Your Password: ')
        flag = 0
        isAdmin = False
        if username == "admin" and password == "123":
            isAdmin = True
        if isAdmin == False:
            for user in bus_counter.get_users():
                if user['username'] == username and user['password'] == password:
                    flag = 1
                    break
            if flag:
                while True:
                    print(f"\n{' '*10}Welcome to BUS TICKET BOOKING SYSTEM")
                    print("1. Available Buses\n2. Show Bus Info\n3. Reservation\n4. EXIT")
                    a = int(input("Enter Your Choice : "))
                    if a == 4:
                        break
                    elif a == 1:
                        bus_counter.available_bus()
                    elif a == 2:
                        bus_counter.show_bus_info()
                    elif a == 3:
                        bus_counter.reservation()
            else:
                print("No username found")
        else:
            while True:
                print(f"\n {' '*10} HELLO ADMIN Welcome to BUS TICKET BOOKING SYSTEM\n")
                print(
                    "1. Install Bus\n2. Available Buses\n3. Show Bus Info\n4. EXIT")
                a = int(input("Enter Your Choice : "))
                if a == 4:
                    break
                elif a == 1:
                    bus_counter.install()
                elif a == 2:
                    bus_counter.available_bus()
                elif a == 3:
                    bus_counter.show_bus_info()
