import traceback

from student import Student


class StudentManager:
    def __init__(self):
        """init"""
        self.student_list = []


    def run(self):
        self.load_student()
        while 1:
            self.show_menu()
            menu_num = int(input("请输入功能序号 : "))
            if menu_num == 1:
                self.add_student()
            elif menu_num == 2:
                self.del_student()
            elif menu_num == 3:
                self.update_student()
            elif menu_num == 4:
                self.search_student()
            elif menu_num == 5:
                self.show_student()
            elif menu_num == 6:
                self.save_student()  # 保存学员信息
            elif menu_num == 7:
                break                # 如果之后客户输入了其他的不输入这里的东西 还需要做判断 是否退出


    @staticmethod
    def show_menu():
        print("student management system")
        print("**" * 30)
        print("1 : 添加学员")
        print("2 : 删除学员")
        print("3 : 更新学员信息")
        print("4 : 查询学员信息")
        print("5 : 显示所有学员信息")
        print("6 : 保存学员信息")
        print("7 : 退出系统")
        print("**" * 30)

    def add_student(self):
        name = input("输入名字 : ")
        gender = input("输入性别 : ")
        tel = input("输入电话 : ")

        student = Student(name, gender, tel)
        self.student_list.append(student)
        print("**" * 20)
        print("添加的信息如下 : ")
        print(student)
        print("**" * 20)

    def del_student(self):
        del_name = input("输入要删除的学员姓名：")
        for stu in self.student_list:
            if del_name == stu.name:
                self.student_list.remove(stu)
                print(f"删除{stu.name}成功")
                break
        else:
            print(f"删除失败 不存在名字为{stu.name}的学员")
        print("**" * 20)

    def update_student(self):
        update_name = input("输入要修改学员的姓名 ： ")
        for stu in self.student_list:
            if update_name == stu.name:
                stu.name_tmp = input("输入修改后的学员姓名：")
                stu.gender_tmp = input("输入修改后的学员性别：")
                stu.tel_tmp = input("输入修改后的手机号：")
                if stu.name_tmp != "":
                    stu.name = stu.name_tmp
                if stu.gender_tmp != "":
                    stu.gender = stu.gender_tmp
                if stu.tel_tmp != "":
                    stu.tel = stu.tel_tmp
                print(f"修改后的信息 ： {stu.name}, {stu.gender}, {stu.tel}")
        print("**" * 30)
    def search_student(self):
        search_name = input("输入要查询的学员的姓名 ： ")
        for stu in self.student_list:
            if search_name == stu.name:
                print(stu)
                break
        else:
            print(f"查询错误 不存在名字为{search_name}的学员")

        print("**" * 30)
    def show_student(self):
        name = "姓名"
        gender = "性别"
        tel = "电话号码"
        print(f"{name:<11} | {gender:<7} | {tel:<10}")
        for stu in self.student_list:
            # print(stu, type(stu))                                                # 花样展示
            print(f"{stu.name:<12} | {stu.gender:<8} | {stu.tel:<10}")
        print("**" * 30)

    def save_student(self):
        with open("student.data", "w", encoding="utf-8") as f:
            new_list = []
            for stu in self.student_list:
                # print(stu)
                # name: zhangsan , gender: nan  , tel: 12321
                # print(stu.__dict__ , type(stu), type(stu.__dict__))
                # {'name': 'qq', 'gender': 'nan ', 'tel': '12'} <class 'student.Student'> <class 'dict'>
                new_list.append(stu.__dict__)
                # print(new_list)
            f.write(str(new_list))
        print("**" * 30)


    def load_student(self):
        try:
           with open("student.data", "r", encoding="utf-8")  as file_reader:
               data = file_reader.read()
               # print(data)
               new_list = eval(data)  # 转换成列表
               for stu in new_list:
                   new_student = Student(stu["name"], stu["gender"], stu["tel"])
                   self.student_list.append(new_student)
        except IOError:
            traceback.print_exc()
        print("**" * 20)




















