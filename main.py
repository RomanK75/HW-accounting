from application import salary
import datetime
from colorama import Fore

def main():
    print(datetime.datetime.today().strftime('%d/%m/%Y'))
    while True:
        cmd = input(Fore.LIGHTCYAN_EX +'Welcom! Type the command (calculate_salary) - ')
        if cmd == 'calculate_salary':
            salary.calculate_salary(input('type the name of worker(Anna/Vlad/Alex/Alena) - '))
        else:
            print('Error')
            break
        
if __name__ == '__main__':
    main()