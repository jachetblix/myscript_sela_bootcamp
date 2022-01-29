import script
def welcome_func():
    print('Hello  my name is Artyom Egorov', end='\n')
    print("I, don't wanna conquer the world like Pinky and Brain", end='\n')
    print('I belive i can change the world by creating something special', end='\n')
    print('You can check my linkedin account: ' + " https://www.linkedin.com/in/artem-egorov-4804a5193/", end='\n')



if __name__ == '__main__':
    welcome_func()
    a = input()
    script.find_string(a)