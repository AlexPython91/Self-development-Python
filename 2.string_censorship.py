# Создайте функцию, которая будет принимать строку и цензурировать 
# (закрывать звездочками) слова длиннее четырех букв.


str = 'Мы знаем кто мы есть но не знаем кем мы можем быть'
print(str)

def censor(str):
    for i in str.split():
        if len(i) > 4:
            str = str.replace(i, '*' * len(i))
    return str
print(censor(str))