size_symbol = 4
symbol_of_lines = 25
lines_in_pages = 50
pages_in_book = 100
size_floppy_mb = 1.44

size_one_book = size_symbol*symbol_of_lines*lines_in_pages*pages_in_book
size_floppy_bytes = size_floppy_mb*1024*1024
result = int(size_floppy_bytes/size_one_book)

print("Количество книг, помещающихся на дискету:", result)
