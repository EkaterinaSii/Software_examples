#! usr/bin/python3

from statistics import mean


global count
count = 1
class_dict = {}


############### ADDING STUDENT ##############

def add_student():
    """ Adding new student to dictionary class_dict """

    def define_student():
        """ Asking to enter name and surname and saves it to dictionary with all grades default as None """

        global count
        name = input('Enter here name and surname: ')
        class_dict[count] = {'name':name, 'grades':{"math": {"ass": None, 'test':None, 'final_grades':None, 'letter':None},"eng": {"ass": None, 'test':None, 'final_grades':None, 'letter':None}, 'kor':{"ass": None, 'test':None, 'final_grades':None, 'letter':None},'py':{"ass": None, 'test':None, 'final_grades':None, 'letter':None}}}
        print(f'....Student is saved with id {count}.....')
        count +=1 
        add_more()
    

    def add_more():
        """ Asking if user wants to add more student, go to menu or exit """

        ask = int(input('''Would you like to:
                            1. Add another student
                            2. Go to main menu
                            3. Exit
                            Enter here: '''))

        if ask == 1: 
            define_student()
        elif ask == 2: 
            main()
        elif ask == 3: 
            exit()
        else:
            print("Something is weird...Try again")
            add_more()

    define_student()

############### ADDING GRADES ##############

def add_grade():
    """ Adding grades to the dictionary class_dict """

    def define_student():
        """ Asking id of student to add grades """

        try:
            student_id = int(input("Enter the id of student to add grade: "))
            ask_for_subject(student_id)

        except KeyError and ValueError:
            print('Student id is not found. Please enter again')
            define_student()
    

    def ask_for_subject(student_id):
        """ Asking to what subject need to add the grade """

        try:
            subject = input("""Enter here subject to grade:
                                mathematics (enter: math)
                                english (enter: eng)
                                korean (enter: kor)
                                python(enter: py):  """)

            if subject != 'math' and subject != 'eng' and subject != 'kor' and subject != 'py':
                print('Something is wrong...Try again.')
                ask_for_subject(student_id)
            else:
                ask_for_ass_or_test(student_id, subject)

        except KeyError:
            print('Something is weird...Try again.')
            ask_for_subject(student_id)


    def ask_for_ass_or_test(student_id, subject):
        """ Asking to what section add the grade (A = assignment, T = test) """

        try:
            ass_or_test = input(""" Would you like grade for assignment or test?
                                    Assignment enter: A
                                    Test enter: T 
                                    Enter: """)

            if ass_or_test != "A" and ass_or_test != 'T':
                print('Something is weird...Try again.')
                ask_for_ass_or_test(student_id,subject)
            else:
                put_grades(student_id,subject,ass_or_test)

        except KeyError:
            print('Something is weird...Try again.')
            ask_for_ass_or_test(student_id, subject)

    def put_grades(student_id,subject,ass_or_test):
        """ Asking to enter grade in one line with space like 10 20 30 and adds it to needed section """
       
        try:
            grades = []
            grades_answ = input('Enter here grade with space like: 10 20 30: ').split()

            for i in grades_answ:
                i = int(i)
                grades.append(i)

            if ass_or_test == 'A':
                class_dict[student_id]['grades'][subject]['ass'] = grades
                print('...Grades are added!...')
                calculate_average(student_id,subject)
                ask_to_add_more(student_id,subject)
            else:
                class_dict[student_id]['grades'][subject]['test'] = grades
                print('...Grades are added!...')
                calculate_average(student_id,subject)
                ask_to_add_more(student_id,subject)

        except KeyError:
            print('Something is weird...Try again')
            put_grades(student_id,subject,ass_or_test)

    def ask_to_add_more(student_id,subject):
        """ Asking if user whats to add more grades, go to menu or exit. If need to add more grades, then asking which excatly. """

        try:

            add_more = int(input('''Choose:
                                    1. Add more grades
                                    2. Go to main menu
                                    3. Exit
                                    Enter here: '''))

            if add_more == 1:
                ask = int(input('''Would you like to:
                                    1. Add grades to other student
                                    2. Add grade to same student, other subject
                                    3. Add grade same student, same subject, other category (assignment/test)
                                    Enter here: '''))

                if ask == 1: define_student()
                elif ask == 2: ask_for_subject(student_id)
                elif ask == 3: ask_for_ass_or_test(student_id, subject)
                else: 
                    print('Something is weird...Try again')
                    ask_to_add_more(student_id,subject)

            elif add_more == 2:
                print('Going...')
                main()

            elif add_more == 3:
                exit()

            else:
                print('Something is weird...Try again.')
                ask_to_add_more()

        except KeyError:
            print('Something is weird...Try again')
            ask_to_add_more(student_id,subject)


    def calculate_average(id_num,sub):
        """ Calculatig the average grade of subjects, adds the final number to key 'final_grades' and corresponding letter to key 'letter' """

        ass_grades = class_dict[id_num]['grades'][sub]['ass']
        test_grades = class_dict[id_num]['grades'][sub]['test']

        if ass_grades == None:
            ass_grades = [0]
        elif test_grades == None:
            test_grades = [0]

        average_ass = sum(ass_grades)/len(test_grades)
        average_test = sum(test_grades)/len(test_grades)
        final_grade = average_ass*0.35 + average_test*0.65
        class_dict[id_num]['grades'][sub]['final_grades'] = round(final_grade,2)

        if final_grade <= 60:
            class_dict[id_num]['grades'][sub]['letter'] = 'FAIL'
        elif final_grade >= 60 and final_grade < 70:
            class_dict[id_num]['grades'][sub]['letter'] = 'D'
        elif final_grade >= 70 and final_grade < 80:
            class_dict[id_num]['grades'][sub]['letter'] = 'C'
        elif final_grade >=80 and final_grade < 90:
            class_dict[id_num]['grades'][sub]['letter'] = 'B'
        else:
            class_dict[id_num]['grades'][sub]['letter'] = 'A'

    define_student()        
    
############### DELETING STUDENT ##############

def delete_student():
    """ Deleting student """

    def define_student():
        """ Asking how to find right student to delete -  by name or id"""

        way = int(input('''Would you like to find student by:
                        1. Student ID
                        2. Student Name
                        Enter here: '''))

        if way == 1:
            delete_by_id()
        elif way == 2:
            delete_by_name()
        else:
            print('Something is weird...Try again.')
            define_student()


    def delete_by_id():
        """ Deleting student based on ID """
        
        student_id = int(input("Enter the id of student to delete: "))
        class_dict.pop(student_id)
        print(f"Student with id number {student_id} is deleted.")
        print(class_dict)
        delete_more()

    def delete_by_name():
        """ Deleting student based on name """
        student_name = input("Enter the name of the student to delete: ")
        for key, value in list(class_dict.items()):
            for key_2, value_2 in list(value.items()):
                if value_2 == student_name:
                    class_dict.pop(key)
                    print(f"Student {student_name} is deleted")
                    print(class_dict)
                    delete_more()

    def delete_more():
        """ Ask if user would like to delete more, go to menu or exit """
        ask = int(input('''Would you like to:
                            1. Delete another student
                            2. Go to main menu
                            3. Exit
                            Enter here: '''))

        if ask == 1: 
            define_student()
        elif ask == 2: 
            main()
        elif ask == 3: 
            exit()
        else:
            print("Something is weird...Try again")
            delete_more()

    define_student()

############### PRINTING GRADES ######################

def show_grades():
    
    def asking_what_to_print():
        """ Asking if need to print grades of specific student or full class """

        what_to_print = int(input('''What would you like to print?
                                        1. Grades of a student
                                        2. Grades of a whole class
                                        Enter here:  '''))

        if what_to_print == 1 or what_to_print == 2:
            print_sub_or_all(what_to_print)
        else:
            print('Something is weird...Try again.')
            asking_what_to_print()

    def print_sub_or_all(what_to_print):
        """ Asking if needed to pring all subjects or specific. If specific - which one. """

        sub_or_all = int(input('''Would you like to print:
                                    1. Specific subject
                                    2. All subjects
                                    Enter here: '''))
        
        if sub_or_all == 1:
            which_sub = input('''What subject would you like to print?:
                                mathematics (enter: math)
                                english (enter: eng)
                                korean (enter: kor)
                                python(enter: py):  
                                Enter here: ''')
            
        elif sub_or_all == 2:
            which_sub = 'all'
        else:
            print('Something is weird...Try again')
            print_sub_or_all(what_to_print)

        if what_to_print == 1: print_student(which_sub)
        else: print_class(which_sub)



    def print_student(sub_or_all):
        """ If user chose to print student, asking how to find - by name or ID and prints by choosen way"""

        way = int(input('''Would you like to find student by:
                        1. Student ID
                        2. Student Name
                        Enter here: '''))

        if way == 1:

            id_num = int(input('Enter student id here: '))
            if sub_or_all == 'all':

                print(f"""{class_dict[id_num]['name']}'s grades are: 
                            Mathematics: assignment - {class_dict[id_num]['grades']['math']['ass']}, test - {class_dict[id_num]['grades']['math']['test']}
                                The average of Mathematics is {class_dict[id_num]['grades']['math']['final_grades']}
                                The letter grade is {class_dict[id_num]['grades']['math']['letter']}

                            English: assignment - {class_dict[id_num]['grades']['eng']['ass']}, test - {class_dict[id_num]['grades']['eng']['test']}
                                The average of English is {class_dict[id_num]['grades']['eng']['final_grades']}
                                The letter grade is {class_dict[id_num]['grades']['eng']['letter']}

                            Korean: assignment - {class_dict[id_num]['grades']['kor']['ass']}, test - {class_dict[id_num]['grades']['kor']['test']}
                                The average of Korean is {class_dict[id_num]['grades']['kor']['final_grades']}
                                The letter grade is {class_dict[id_num]['grades']['kor']['letter']}

                            Python: assignment - {class_dict[id_num]['grades']['py']['ass']}, test - {class_dict[id_num]['grades']['py']['test']}
                                The average of Python is {class_dict[id_num]['grades']['py']['final_grades']}
                                The letter grade is {class_dict[id_num]['grades']['py']['letter']}
                            """)
            else:
                print(f"""{class_dict[id_num]['name']}'s grades for {sub_or_all}: 
                            assignment - {class_dict[id_num]['grades'][sub_or_all]['ass']} 
                            test - {class_dict[id_num]['grades'][sub_or_all]['test']}
                            The average is {class_dict[id_num]['grades'][sub_or_all]['final_grades']}
                            The letter grade is {class_dict[id_num]['grades'][sub_or_all]['letter']}""")

        elif way == 2:
            name_student = input('Enter student name here: ')
            if sub_or_all == 'all':

                for key, value in class_dict.items():
                    for key_2, value_2 in value.items():
                        if value_2 == name_student:
                            print(f"""{value_2}'s grades are: 
                                        Mathematics: assignment - {class_dict[key]['grades']['math']['ass']}, test - {class_dict[key]['grades']['math']['test']}
                                            The average of Mathematics is {class_dict[key]['grades']['math']['final_grades']}
                                            The letter grade is {class_dict[key]['grades']['math']['letter']}

                                        English: assignment - {class_dict[key]['grades']['eng']['ass']}, test - {class_dict[key]['grades']['eng']['test']}
                                            The average of English is {class_dict[key]['grades']['eng']['final_grades']}
                                            The letter grade is {class_dict[key]['grades']['eng']['letter']}

                                        Korean: assignment - {class_dict[key]['grades']['kor']['ass']}, test - {class_dict[key]['grades']['kor']['test']}
                                            The average of Korean is {class_dict[key]['grades']['kor']['final_grades']}
                                            The letter grade is {class_dict[key]['grades']['kor']['letter']}

                                        Python: assignment - {class_dict[key]['grades']['py']['ass']}, test - {class_dict[key]['grades']['py']['test']}
                                            The average of Python is {class_dict[key]['grades']['py']['final_grades']}
                                            The letter grade is {class_dict[key]['grades']['py']['letter']}

                                        """)
            else:

                for key, value in class_dict.items():
                    for key_2, value_2 in value.items():
                        if value_2 == name_student:
                            print(f"""{value_2}'s grades for {sub_or_all}: 
                                        assignment - {class_dict[key]['grades'][sub_or_all]['ass']} 
                                        test - {class_dict[key]['grades'][sub_or_all]['test']}
                                        The average is {class_dict[key]['grades'][sub_or_all]['final_grades']}
                                        The letter grade is {class_dict[key]['grades'][sub_or_all]['letter']}
                                        """)
        else:
            print('Something is weird...Try again.')
            print_student(sub_or_all)

        print_more()
    

    def average_of_class():
        """ Calculating the average of the class by subjects' final grades. If grades are None ->> = 0 """

        m_ave = 0
        e_ave = 0
        k_ave = 0
        p_ave = 0

        for key,value in class_dict.items():
            math = class_dict[key]['grades']['math']['final_grades']
            eng = class_dict[key]['grades']['eng']['final_grades']
            kor = class_dict[key]['grades']['kor']['final_grades']
            py = class_dict[key]['grades']['py']['final_grades']

            if math == None:
                math = 0
            if eng == None:
                eng = 0
            if kor == None:
                kor = 0
            if py == None:
                py = 0
            
            m_ave += math
            e_ave += eng
            k_ave += kor
            p_ave += py

        print(f"""The average grade of the class:
                Mathematics: {m_ave}
                English: {e_ave}
                Korean: {k_ave}
                Python: {p_ave}\n""")


    def print_class(sub_or_all):
        """ Printing grades of all class (all subjects or some) + average grades of the class """

        if sub_or_all == 'all':
            for key, value in class_dict.items():
                print(f"""{class_dict[key]['name']}'s grades are: 
                                Mathematics: assignment - {class_dict[key]['grades']['math']['ass']}, test - {class_dict[key]['grades']['math']['test']}
                                    The average of Mathematics is {class_dict[key]['grades']['math']['final_grades']}
                                    The letter grade is {class_dict[key]['grades']['math']['letter']}

                                English: assignment - {class_dict[key]['grades']['eng']['ass']}, test - {class_dict[key]['grades']['eng']['test']}
                                    The average of English is {class_dict[key]['grades']['eng']['final_grades']}
                                    The letter grade is {class_dict[key]['grades']['eng']['letter']}

                                Korean: assignment - {class_dict[key]['grades']['kor']['ass']}, test - {class_dict[key]['grades']['kor']['test']}
                                    The average of Korean is {class_dict[key]['grades']['kor']['final_grades']}
                                    The letter grade is {class_dict[key]['grades']['kor']['letter']}

                                Python: assignment - {class_dict[key]['grades']['py']['ass']}, test - {class_dict[key]['grades']['py']['test']}
                                    The average of Python is {class_dict[key]['grades']['py']['final_grades']}
                                    The letter grade is {class_dict[key]['grades']['py']['letter']}
        
                                        """)
    
            average_of_class()

        elif sub_or_all != 'all':
            for key, value in class_dict.items():
                print(f"""{class_dict[key]['name']}'s grades for {sub_or_all}: 
                                    assignment - {class_dict[key]['grades'][sub_or_all]['ass']} 
                                    test - {class_dict[key]['grades'][sub_or_all]['test']}
                                    The average is {class_dict[key]['grades'][sub_or_all]['final_grades']}
                                    The letter grade is {class_dict[key]['grades'][sub_or_all]['letter']}
                                    """)
                average_of_class()

        else:
            print('Something is weird...Try again.')
            print_class(sub_or_all)

        print_more()


    def print_more():
        """ Asking student if needed to print something else, go to menu or exit """
        ask = int(input("""Would you like: 
                            1. Print something else
                            2. Go to main menu
                            3. Exit
                            Enter here: """))

        if ask == 1: 
            show_grades()
        elif ask == 2: 
            main()
        elif ask == 3: 
            exit()
        else:
            print("Something is weird...Try again")
            print_more()
    

    asking_what_to_print()

############### EXITING ###############
def exit():
    """ Exiting """
    print('Exiting...')


def main():
    """ Asking user what action need to be done and reference to right function """
    
    global count

    action = input(''' What would you like to do:
                                        1. Add student
                                        2. Add grade
                                        3. Delete student
                                        4. Show grade
                                        5. Exit
                                        Enter number here: ''')

    if action == '1':
        add_student()

    elif action == '2': 
        add_grade()

    elif action == '3': 
        delete_student()

    elif action == '4':
        show_grades()

    elif action == '5':
        exit()

    else: 
        print('Something weird happened....Try again')
        main()



if __name__ == '__main__':
    main()