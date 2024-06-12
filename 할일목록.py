from time import sleep

loading_time = 2
user ={'noel' : 'a1234@' }

ToDoList = []
nameList=[]
checkBox = []


welcome = "--hello {} !! "
login_status = 'logout'

logIn_userName = ''


def slowPrint(message_str, endOption= '\n'):
    for i in range(len(message_str)):
        print(message_str[i], end='')
        sleep(0.01)
    print(end = endOption)
    
def slow_input(question):
    slowPrint(question + ': ', endOption='')
    answer = input()
    return answer
    
    

def loading_Question():
    answer = slow_input('Log-In(l) or Sign-up(s)')
    if answer == 'l':
        login_process()
    elif answer == 's':
        #print('This is not ready to sign-up function.')
        slowPrint('welcome. this is sign_up menu')
        
        sign_up()


def sign_up():
    yourID = slow_input('type new user name(or ID)')
    password = slow_input('type new pass-word')
    user[yourID] = password
    
    print(user)
    

def login_process():
    global login_status
    yourID = slow_input('type user name(or ID)')
    if yourID in user:

        while login_status != 'logIn':
          password = slow_input('type pass-word')
          if password == user[yourID]:
                slowPrint(welcome.format(yourID))
                login_status = 'logIn'
                logIn_userName = yourID
          else:
               slowPrint('try again! password is wrong.', endOption='\n')
    else:
         a=slow_input('are you sign_up?')
         if a == 'yes':
             sign_up()
             login_status = 'logIn'
             
         else:
             print('good bye')
        


def show_loadingImage():
    time_of_one_bread = loading_time/20
    print('loading ', end ='')
    for i in range(20):
        print('#', end='')
        sleep(time_of_one_bread)
    print('')

show_loadingImage()
loading_Question()

if login_status == 'logIn':
   answer = slow_input('1번: add new list, 2: show all list, 3: check a list')
   if answer == '1':
       newTask = slow_input('Type your new ToDo list')
       ToDoList.append(newTask)
       print(ToDoList)
       
    
    


