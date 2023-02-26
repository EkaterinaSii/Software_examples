import csv

"""This is a program that allows you to manage projects and employees."""

column_name_project = ['project','total_budget','current_budget','status','employee_id']
column_name_employee = ['employee_id','name','salary','position']

x = open('projects_data.csv','w')
writer = csv.DictWriter(x,fieldnames=column_name_project)
writer.writeheader()
x.close()

y = open('employee_data.csv','a')
writer_2 = csv.DictWriter(y,fieldnames=column_name_employee)
writer_2.writeheader()
y.close()

def add_to_file(data_list,names,option='') -> None:
    """This function adds data to the file. It takes 3 arguments: data_list, names and option.
    data_list is a list of dictionaries, names is a list of column names and option is a number"""   

    if option == 1:
        x = open('projects_data.csv','a')
        writer = csv.DictWriter(x,fieldnames=names)
        for i in data_list:
            writer.writerow(i)
        x.close()
        print('\nSucessfully saved to Project file!\n')
        
    else:
        x = open('employee_data.csv','a')
        writer = csv.DictWriter(x,fieldnames=names)
        for i in data_list:
            writer.writerow(i)
        x.close()
        print('\nSucessfully saved to Employee file!\n')

def change_project_write(project,column,old_value,new_value,column_name_project) -> None:
    """This function changes the project. It takes 5 arguments: project, column, old_value, new_value and column_name_project."""

    x = open('projects_data.csv','r')
    reader = csv.DictReader(x)
    new_dict = {}
    count = 1

    for row in reader:
        new_dict[count] = row
        count +=1

    new_list=[]
    for key,values in new_dict.items():
        if values['project'] == project and values[column] == old_value:
            values[column] = new_value
            values2 = {'project':values['project'], 'total_budget':values['total_budget'], 'current_budget':values['current_budget'],'status':values['status'],'employee_id':values['employee_id']}
            new_list.append(values2)
        else:
            new_list.append(values)

    x.close()
    x = open('projects_data.csv','w')
    writer = csv.DictWriter(x,fieldnames=column_name_project)
    writer.writeheader()
    for i in new_list:
        writer.writerow(i)
    x.close()

def new_project(column_name_project) -> None:
    """This function adds new project to the file. It takes 1 argument: column_name_project."""

    print('Please enter the following information for the new project:\n')
    ask_name = input('What is the name of the project? ')
    while True:
        try:
            ask_bugdet = float(input('What is the total budget of the project? '))
            break
        except ValueError:
            print('You cannot enter anything except number')

    cond2 = True 
    while cond2:
        cond = True
        while cond:
            try:
                ask_employee = int(input('ID of employee responsible for project? If id does not exist, enter 0 to add new employee '))
                emp = open_file('employee_data.csv')
                if ask_employee == 0:
                    count = len(emp)+1
                    count = new_employee(count,column_name_employee)
                    cond = False
                else:
                    for i in emp:
                        if i['employee_id'] == str(ask_employee):
                            cond = False
                            cond2 = False
                            break

            except ValueError:
                print('You cannot enter anything except number')

            cond2 = False
        
    data_list_project = [{'project':ask_name, 'total_budget':ask_bugdet, 'current_budget':ask_bugdet,'status':'ongoing','employee_id':ask_employee}]
    
    add_to_file(data_list_project,column_name_project,1)
    reduce_budget(column_name_project,ask_name)
    check_budget(column_name_project,ask_name)

def new_employee(count,column_name_employee) -> int:
    """This function adds new employee to the file. It takes 2 arguments: count and column_name_employee."""

    print('Please enter the following information for the new employee:\n')
    
    ask_employee = input('Name of employee? ')
    
    cond = True
    while cond:
        try:
            ask_salary = float(input('What is the salary of the employee? '))
            cond = False
        except ValueError:
            print('You cannot enter anything except number')
            
    ask_position = input('What is the position of the employee? ')
    data_list_employees = [{'employee_id':count,'name':ask_employee, 'salary':ask_salary, 'position':ask_position}]
    add_to_file(data_list_employees,column_name_employee,2)
    count +=1
    return count

def open_file(file) -> list:
    """This function opens the file and returns a list of dictionaries"""
    with open(file,'r') as x:
        reader = csv.DictReader(x)
        new_dict = {}
        count = 1
        
        for row in reader:
            new_dict[count] = row
            count +=1
            
        new_list=[]
        for key,values in new_dict.items():
            new_list.append(values)
            
        return new_list

def find_project() -> tuple:
    """This function finds the project and returns the index of the project in the list, the name of the project and the list of dictionaries"""
    
    cond = True
    while cond:
        project = input('What project would you like to change? ')
        list_1 = open_file('projects_data.csv')
            
        
        for dic in list_1:
            if dic['project'] == project:
                num = list_1.index(dic)
                return num, project, list_1
                cond = False
                break
        print('The project name is not found, try again')

def change_project(column_name_project) -> None:
    """This function changes the project. It takes 1 argument: column_name_project."""
    
    project_id, project, list_1 = find_project()
    
    ask = int(input('''Please choose what would you like to change:
1. Name of the project
2. Total budget of the project
3. Disable the project
'''))
                
    if ask == 1:
        new_value = input('What would be new name of your project? ')
        column = 'project' 
        old_value = project
        change_project_write(project,column,old_value,new_value,column_name_project)
        
    elif ask == 2:
        while True:
            try:
                new_value = float(input('What is your total budget of the project? '))
                column = 'total_budget'
                old_value = list_1[project_id]['total_budget']
                change_project_write(project,column,old_value,new_value,column_name_project)
                break
            except ValueError:
                print('You can enter only numbers. Try again.')
                            
    elif ask == 3:
        if list_1[project_id]['status'] == 'disable':
            print('The project is already disable. Check the budget')
        else:
            new_value = 'disable'
            column = 'status'
            old_value = list_1[project_id]['status']
            change_project_write(project,column,old_value,new_value,column_name_project)
            print('Status is sucessfully changed to "disable"')
        
                
    else:
        print("You entered wrong number, try again")
        change_project(column_name_project)

def update_budget(column_name_project) -> None:
    """Update the budget of the project. If the project is disable, you can not update the budget."""

    project_id, project, list_1 = find_project()
    
    if list_1[project_id]['status'] == 'disable':
        print('The project is disable, you can not update the budget')
    else:
        while True:
            try:
                ask = input('Would you like to add or reduce the budget? ')                
                if ask == 'add':
                    new_value = float(input('How much would you like to add? '))
                    new_value = float(list_1[project_id]['current_budget']) + new_value
                elif ask == 'reduce':
                    new_value = float(input('How much would you like to reduce? '))
                    new_value = float(list_1[project_id]['current_budget']) - new_value
                else:
                    print('You can enter only "add" or "reduce"')
                    continue

                column = 'current_budget'
                old_value = list_1[project_id]['current_budget']
                change_project_write(project,column,old_value,new_value,column_name_project)
                check_budget(column_name_project,project)
                break

            except ValueError:
                print('You can enter only numbers. Try again.')

def check_budget(column_name_project,name) -> None:
    """Check if the budget is zero or negative, if yes, disable the project"""

    list_1 = open_file('projects_data.csv')
    for dic in list_1:
        if dic['project'] == name:
            if float(dic['current_budget']) <= 0:
                new_value = 'disable'
                column = 'status'
                old_value = dic['status']
                change_project_write(name,column,old_value,new_value,column_name_project)
                print('The project is disable, because the budget is zero or negative')
                break

def reduce_budget(column_name_project,name) -> None:
    """Reduce budget of the project by the salary of the employee"""

    cond= True
    while cond:
        list_1 = open_file('projects_data.csv') 
        for dic in list_1:
            if dic['project'] == name:
                list_2 = open_file('employee_data.csv')
                for dic_2 in list_2:
                    if dic['employee_id'] == dic_2['employee_id']:
                        new_value = float(dic['current_budget']) - float(dic_2['salary'])
                        column = 'current_budget'
                        old_value = dic['current_budget']
                        change_project_write(name,column,old_value,new_value,column_name_project)
                        cond = False
                        break   

def show_projects() -> None: 
    """Shows all projects, only active or only disable"""   
    try:
        ask = int(input('''Would you like to see all projects or only active?
        1. All projects
        2. Only active
        3. Only disable '''))

        if ask == 1:
            with open('projects_data.csv','r') as f:
                print('Searching for all projects...')
                reader = csv.DictReader(f)
                for row in reader:
                    print(f'Project name: {row["project"]}, total budget: {row["total_budget"]}, current budget: {row["current_budget"]}, status: {row["status"]}, employee responsible: {row["employee_id"]}')
        elif ask == 2:
            with open('projects_data.csv','r') as f:
                print('Searching for active projects...')
                reader = csv.DictReader(f)
                for row in reader:
                    if row['status'] == 'ongoing':
                        print(f'Project name: {row["project"]}, total budget: {row["total_budget"]}, current budget: {row["current_budget"]}, status: {row["status"]}, employee responsible: {row["employee_id"]}')
        elif ask == 3:
            with open('projects_data.csv','r') as f:
                print('Searching for disable projects...')
                reader = csv.DictReader(f)
                for row in reader:
                    if row['status'] == 'disable':
                        print(f'Project name: {row["project"]}, total budget: {row["total_budget"]}, current budget: {row["current_budget"]}, status: {row["status"]}, employee responsible: {row["employee_id"]}')
        else:
            print('You entered wrong number, try again')
            show_projects()

    except ValueError:
        print('You can enter only numbers. Try again.')
        show_projects()

def main() -> None:
    """ Main function"""  

    count = 1
    cond = True
    while cond:
        try:
            ask_main = int(input('''\nWelcome! Please choose what would you like to do:
        !!! Please add employee first !!!

        1. Add new employee
        2. Add new project
        3. Change projects' details
        4. Update the budget
        5. Show projects
        6. Exit
        \n'''))

            if ask_main == 1:
                count = new_employee(count,column_name_employee)
            elif ask_main == 2:
                new_project(column_name_project)
            elif ask_main == 3:
                change_project(column_name_project)
            elif ask_main == 4:
                update_budget(column_name_project)
            elif ask_main == 5:
                show_projects()
            elif ask_main == 6:
                print('Exiting...')
                cond = False
                exit()
                break
            else:
                print('You entered wrong number, try again.')
                main()
                break

        except ValueError:
            print('You entered something wrong. Try again')
            main()

if __name__ == '__main__':
    main()