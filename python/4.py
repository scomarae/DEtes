# 4) Даны два слова. Написать функцию anagram для определения, являются ли эти слова анаграммами.
# Примечание: Анаграммами называются слова, которые состоят из одного и того же набора букв (и имеют одинаковую длину).

def anagram(word_1, word_2):
    if sorted(word_1) == sorted(word_2):  # простой метод: сортируем две строки и проверяем их
        return True
    else:
        return False


print(anagram('silent', 'listen'))
print(anagram('mama', 'mam'))
print(anagram('mama', 'papa'))
