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


def TOT_analysis(TOT_level):
    if TOT_level < 200:
        return 'Nromal'
    elif 200 <= TOT_level <= 239:
        return 'Borderline high'
    elif 240 <= TOT_level:
        return 'High'


def cholesterol_analysis():
    print('Cholesterol Check')
    HDLinput = input('Enter test result: ')
    test_info = HDLinput.split('=')
    if test_info[0].strip() == 'HDL':
        print(HDL_analysis(int(test_info[1])))
        save_result('HDL', HDL_analysis(int(test_info[1])), test_info[1])
    elif test_info[0].strip() == 'LDL':
        print(LDL_analysis(int(test_info[1])))
        save_result('LDL', LDL_analysis(int(test_info[1])), test_info[1])
    elif test_info[0].strip() == 'TOT':
        print(TOT_analysis(int(test_info[1])))
        save_result('TOT', TOT_analysis(int(test_info[1])), test_info[1])


def save_info():
    import json
    name = input('first name and last name:')
    age = input('age:')
    info_dict = {'full name': name, 'age': age}
    file = open('info.json', 'w')
    json.dump(info_dict, file)
    file.close()
    return info_dict


def save_result(x, y, z):
    import json
    r = y + ' (' + z.strip() + ')'
    file = open('info.json', 'w+') % 'r'
    result_dict = json.load(file)
    #file.close()
    result_dict[x] = r
    #file = open('info.json', 'w')
    json.dump(result_dict, file)
    file.close()
    return


def interface():
    while 1:
        print("Cholesterol Analysis")
        print("Options:")
        print("1 - Cholesterol Check")
        print("2 - Record Patient Info")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            cholesterol_analysis()
        elif choice == '2':
            a = save_info()
            print(a)


if __name__ == '__main__':
        interface()
