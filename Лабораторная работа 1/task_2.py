size_one_book = 4*25*50*100   #Объем одного учебника в байтах
size_floppy_bytes = 1.44*1024*1024   #Перевод 1.44Мб в байты
result = int(size_floppy_bytes/size_one_book)

print("Количество книг, помещающихся на дискету:", result)
