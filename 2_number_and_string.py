print(round(1.5))
print(round(2.5))
print(round(3.5))
print(round(4.5))


str1 = 'My text for autotest'
print(str1.startswith('My'), str1.endswith('test'), str1.startswith('dfva'))
# Результат True, True, False. startswith ищет вхождение в начале строки


num = 5
my_text = 'подстановка'
res1 = '''
Много текста для строки
И его перенесли на несколько.
Дата или какое-то число %d, а вот здесь текст %s
''' % (num, my_text)
print(res1)

res2 = f'''
Много текста для строки
И его перенесли на несколько.
Дата или какое-то число {num}, а вот здесь текст {my_text}
'''
print(res2)

res3 = '''
Много текста для строки
И его перенесли на несколько.
Дата или какое-то число {num34}, а вот здесь текст {my_text34}
'''.format(num34=num, my_text34=my_text)
print(res3)
