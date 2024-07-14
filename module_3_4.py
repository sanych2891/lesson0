# Самостоятельная работа по уроку "Произвольное число параметров".
# Задача "Однокоренные":
# Напишите функцию single_root_words, которая принимает одно обязательное слово в
# параметр root_word, а далее неограниченную последовательность в параметр *other_words.
# Функция должна составить новый список same_words только из тех слов списка other_words,
# которые содержат root_word или наоборот root_word содержит одно из этих слов.
# После вернуть список same_words в качестве результата своей работы.

# Объявим функцию single_root_words и напишем в ней параметры root_word и *other_words.


def single_root_words(root_word, *other_words):
    # Создадим внутри функции пустой список same_words, который пополнится нужными словами.
    same_words = []
    # При помощи цикла for переберем предполагаемо подходящие слова.
    for word in other_words:
        word = word.lower()
        root_word = root_word.lower()
        # условие, при котором добавляются слова в результирующий список same_words
        if word.lower() in root_word.lower() or root_word.lower() in word.lower():
            same_words.append(word)
    # вернем образованный функцией список same_words
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words("меч", "отмеченный", "примечание", "Мечтатель", "закат", "ЗаМечательныЙ") # свой вариант
print(result1)
print(result2)
print(result3) # свой вариант