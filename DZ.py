class Schedule:
    def __init__(self, time, subject, group, room, student_count):
        self.time = time
        self.subject = subject
        self.group = group
        self.room = room
        self.student_count = student_count
    def __str__(self):
        return f"""
        {self.time} - time
        {self.subject} - subject
        {self.group} - group
        {self.room} - room
        {self.student_count} - student_count
"""
lessons = []

class Admin:
    def __init__(self, lessons):
        self.lessons = lessons

    def Show_schedule(self):
        for i in self.lessons:
            print("--------------------------------------------------------")
            print(i)

    def Add_schedule(self):
        while True:
            want = input("xotite prodoljit?")
            if want == "no":
                break
            time = input("vvedite time - ")
            subject = input("vvedite subject - ")
            group = input("vvedite group - ")
            room = input("vvedite room - ")
            student_count = input("vvedite student_count - ")
            a = Schedule(time, subject, group, room, student_count)
            self.lessons.append(a)

    def update_room(self,time, room):
        for i in self.lessons:
            if i.time == time:
                i.room = room
                break
            print("takogo net")
            break

    def remove_schedule(self,subject):
        for i in self.lessons:
            if i.subject == subject:
                self.lessons.remove(i)
                break
            print("takogo net")
            break

    def search_by_time(self,time):
        for i in self.lessons:
            if i.time == time:
                print(i)
                break
            print("takogo net")
            break

    def log_out(self):
        print("bye bye admin")


# lesson1 = Schedule("10.00","Python","5e62178",8,13)
# lessons.append(lesson1)
class User:
    def __init__(self,lessons):
        self.lessons = lessons

    def Show_schedule(self):
        for i in self.lessons:
            print("--------------------------------------------------------")
            print(i)

    def search_by_time(self,time):
        for i in self.lessons:
            if i.time == time:
                print(i)
                break
            print("takogo net")
            break

    def log_out(self):
        print("bye bye moy dorogoy drug")


def Choise():
    Admin1 = Admin(lessons)
    user1 = User(lessons)
    while True:
        who = input("Kak vi hotite zayti")
        login = "yakrutoyadminyee@gmail.com"
        password = "1234567890"
        if who == "admin":
            log = input("Vvedite login")
            passw = input("Vvedite parol")
            if log == login and passw == password:
                while True:
                    choise = input("""
                    1. add
                    2. update
                    3. show
                    4. remove
                    5. search
                    6. log out
                    """)

                    if choise == "1":
                        Admin1.Add_schedule()
                    elif choise == "2":
                        time = input("kakoy time menyat xocew")
                        new_room = input("Vvedite noviy kabinet")
                        Admin1.update_room(time,new_room)
                    elif choise == "3":
                        Admin1.Show_schedule()
                    elif choise == "4":
                        subject = input("Vvedite nazvanie predmeta")
                        Admin1.remove_schedule(subject)
                    elif choise == "5":
                        time = input("kakoy time xocew nayti")
                        Admin1.search_by_time(time)
                    elif choise == "6":
                        Admin1.log_out()
                        break
                    else:
                        print("Neverno")

            else:
                print("Neverno poprobuy zanovo")
        elif who == "user":
            while True:
                choise = input("""
                1. show
                2. search
                3. log out
                """)
                if choise == "1":
                    user1.Show_schedule()
                elif choise == "2":
                    time = input("kakoy time xocew nayti")
                    user1.search_by_time(time)
                elif choise == "3":
                    user1.log_out()
                    break
                else:
                    print("Neverno")
        elif who == "exit":
            break
        else:
            print("Neverno")
Choise()
print("ura")