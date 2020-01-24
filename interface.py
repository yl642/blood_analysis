def HDL_analysis(HDL_level):
    if HDL_level >= 60:
        return 'Nromal'
    elif 40 <= HDL_level < 60:
        return 'Borderline low'
    else :
        return 'Low'

def LDL_analysis(LDL_level):
    if LDL_level <= 130:
        return 'Nromal'
    elif 130 < LDL_level <= 159:
        return 'Borderline high'
    elif 160 <= LDL_level <189 :
        return 'High'
    elif 190 <= LDL_level:
        return 'Very high'


def cholesterol_analysis():
    print('Cholesterol Analysis')
    HDLinput = input('Enter test result: ')
    test_info = HDLinput.split('=')
    if test_info[0].strip() == 'HDL':
        print(HDL_analysis(int(test_info[1])))
    elif test_info[0].strip() == 'LDL':
        print(LDL_analysis(int(test_info[1])))

def interface():
    while 1:
        print("Cholesterol Analysis")
        print("Options:")
        print("1 - Cholesterol Check")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            cholesterol_analysis()
if __name__ == '__main__':
        interface()
