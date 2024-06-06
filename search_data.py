from return_data_file import data_file


def search_cust():
    data, nf = data_file()
    cust_1 = input("Введите искомое имя: ")
    cust_2 = input("Введите искомую фамилию: ")
    
    for i in range(len(data)):
        line = data[i].split(";")
        if line[1] == cust_1 and line[2] == cust_2:
            print(f"Имя: {line[1]}\nФамилия: {line[2]}\nДата рождения: {line[3]}\nГород: {line[4]}\nНомер телефона: {line[5]}")
        else:
            print("Абонент не найден")
         
    
    
  
    
     