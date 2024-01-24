"""
 JOIN bandi umumiy atributlar asosida ikkita jadvaldagi yozuvlarni birlashtiradi. Har xil turdagi ulanishlar quyidagilar:

INNER JOIN (OR JOIN) - ikkala jadvalda umumiy atributlarga ega bo'lgan yozuvlarni beradi.
LEFT JOIN - chap jadvaldagi barcha yozuvlarni va faqat o'ng jadvaldagi umumiy yozuvlarni beradi.
RIGHT JOIN - o'ng jadvaldagi barcha yozuvlarni va faqat chap jadvaldagi umumiy yozuvlarni beradi.
FULL OUTER JOIN - chap yoki o'ng jadvalda umumiy atribut mavjud bo'lganda barcha yozuvlarni beradi.
CROSS JOIN - bir jadvalning yozuvlarini boshqa jadvalning barcha boshqa yozuvlari bilan birga beradi.

"""  # noqa

import sqlite3

connection = sqlite3.connect('data.db')




connection.commit()
connection.close()

