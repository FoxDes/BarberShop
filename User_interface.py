


def get_info ():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_number = ''
    valid =False
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    info.append(phone_number)
    description = input('Стрижка: голова, борода или комплекс? : ')
    info.append(description)
    file = 'Usrebook.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[0]}\nИмя: {info[1]}\nНомер телефона: {info[2]}\nСтрижка: {info[3]}\n==============================\n')
    file = 'Usrebook.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'\n{info[0]}; {info[1]}; {info[2]}; {info[3]}')
    return info

def get_rec ():
    info_rec = []
    last_name = input('Введите фамилию: ')
    info_rec.append(last_name)
    first_name = input('Введите имя: ')
    info_rec.append(first_name)
    phone_number = ''
    valid =False
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    info_rec.append(phone_number)
    description = input('На какое время Вас записать? : ')
    info_rec.append(description)
    work = input('Вид работ: ')
    info_rec.append(work)
    file_rec = 'Recbook.txt'
    with open (file_rec, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info_rec[0]}\nИмя: {info_rec[1]}\nНомер телефона: {info_rec[2]}\nЗапись на: {info_rec[3]}\nВид работ: {info_rec[4]}\n==============================\n')
    file_rec = 'Recbook.csv'
    with open (file_rec, 'a', encoding = 'utf-8') as data:
        data.write(f'\n{info_rec[0]}; {info_rec[1]}; {info_rec[2]}; {info_rec[3]}; {info_rec[4]}')
    return info_rec


def king_menu():
    answer = int(input("1 - Добавить клиента в журнал контактов\n2 - Записать на прием\n"))
    match answer:
        case 1:
            get_info()
        case 2:
            get_rec()