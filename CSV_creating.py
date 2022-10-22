
def creating ():
    file = 'Usrebook.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'Фамилия; Имя; Номер телефона; Стрижка\n')

def rec_creating ():
    file_rec = 'Recbook.csv'
    with open (file_rec, 'w', encoding = 'utf-8') as data:
        data.write(f'Фамилия; Имя; Номер телефона; Время записи; Вид работ\n')