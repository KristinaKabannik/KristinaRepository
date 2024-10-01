adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

new_text1 = adwentures_of_tom_sawer.replace("\n", " ")
print("Виправлений текст (1):", new_text1)


# task 02 ==
""" Замініть .... на пробіл
"""
new_text2 = new_text1.replace("....", " ")
print("Виправлений текст (2):", new_text2)


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
#new_text3 = " ".join(new_text2.split())
new_text3 = " ".join(new_text2.split()).rstrip()
print("Виправлений текст (3):", new_text3)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
find_h = adwentures_of_tom_sawer.find("h")
print(f"Літера h зустрічається: {find_h} разів")


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

text = adwentures_of_tom_sawer.split()
title_words_number = sum(1 for text in text if text[0].istitle())
print(f"Кількість слів, що починаються з великої літери: {title_words_number}")



# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

first_tom = adwentures_of_tom_sawer.find("Tom")
second_tom = adwentures_of_tom_sawer.find("Tom", first_tom + 1)
print("Позиція, на якій слово Tom зустрічається вдруге:", second_tom)


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

adwentures_of_tom_sawer_sentences = None
dots_replacing = adwentures_of_tom_sawer.replace("....", " ")
adwentures_of_tom_sawer_sentences = dots_replacing.split('.')
print(adwentures_of_tom_sawer_sentences)


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

print(f'Четверте речення: {adwentures_of_tom_sawer_sentences[3].replace("\n", " ")}.')
print(f'Четверте речення у нижньому регістрі: {adwentures_of_tom_sawer_sentences[3].replace("\n", " ").lower()}.')


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

for sentence in adwentures_of_tom_sawer.replace("\n", " ").split(". "):
    print(f'Чи речення починається з By the time: {sentence}: {sentence.startswith("By the time")}')


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

last_sentence = adwentures_of_tom_sawer_sentences[-2].replace("....", " ")
words_in_last_sentence = last_sentence.split()
print(f"Кількість слів останнього речення: {len(words_in_last_sentence)}")