# Изменить значение в кортеже

poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
print(poet_data)

corrected_poet_data = list(poet_data)  # Преобразуем кортеж в список
corrected_poet_data[2] = 'Москва'  # Исправляем город
poet_data = tuple(corrected_poet_data)  # Преобразуем обратно в кортеж

print(poet_data)

