s = "У лукоморья 123 дуб зеленый 456"
if s.find('я') != -1:
    print('Такая буква есть находится на месте',s.find('я'))
else:
    print('такой буквы нет')
print('Буква у вошла в строку',s.count('у'),'раз')
if s.isalpha():
    print('Только из букв')
else:print ('Строка ток в вернем регистер:',s.upper())
print('Длина строки:',len(s))
if len(s) > 4:
    print(s.lower())
print(s[0] + 'О' + s[2:])
