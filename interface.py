def HDL_analysis(HDL_level):
    if HDL_level >= 60:
        return 'Nromal'
    elif 40 <= HDL_level < 60:
        return 'Borderingly low'
    else :
        return 'Low'

def cholesterol_analysis():
    print('Cholesterol Anlysis')
    HDLinput = input('Enter test result: ')
    test_info = HDLinput.split('=')
    if test_info[0] == 'HDL':
        print(HDL_analysis(int(test_info[1])))

def interface():
    while 1:
        print("Cholesterol Analysis")
        print("Options:")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            cholesterol_analysis()
if __name__ == '__main__':
        interface()
