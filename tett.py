with open('task5.txt', 'r', encoding='utf-8') as src, open('task7.txt', 'w', encoding='utf-8') as dest:
    dest.write(src.read())
