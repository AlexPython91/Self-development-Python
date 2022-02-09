# Ваша задача — воспроизвести функционал метода title(), 
# создав функцию emphasise(). Метод title() делает заглавной первую букву каждого слова.

str = 'мы знаем кто мы есть но не знаем кем мы можем быть'
print(str)

def make_it_uppercase(str):
    return str.title()
print(make_it_uppercase(str))