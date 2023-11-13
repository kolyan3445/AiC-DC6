#Вариант 14. Конвейер сборки состоит из 10 технологических мест. На 4 из них требуется силовая подготовка (мужчины).
#Конвейер должен работать в 2 смены. Сформировать все возможные варианты рабочего расписания, если в цехе работает 20 рабочих: 12 женщин и 8 мужчин.

#Часть 1
shift = 'M' * 4 + 'W' * 6


def shift_o_matic(shift, shift_size_unused=None):
    # перестановки('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # перестановки(range(3)) --> 012 021 102 120 201 210
    pool = tuple(shift)
    shift_size_length = len(pool)
    shift_size = shift_size_length if shift_size_unused is None else shift_size_unused
    if shift_size > shift_size_length:
        return
    indices = list(range(shift_size_length))
    cycles_count = list(range(shift_size_length, shift_size_length - shift_size, -1))
    yield tuple(pool[x] for x in indices[:shift_size])
    while shift_size_length:
        for i in reversed(range(shift_size)):
            cycles_count[i] -= 1
            if cycles_count[i] == 0:
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                cycles_count[i] = shift_size_length - i
            else:
                j = cycles_count[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:shift_size])
                break
        else:
            return


shifts = list(set(shift_o_matic(shift)))

print("Часть 1\n Все возможные смены с четыремя мужчинами и оставшимися женщинами:")

for i in range(len(shifts)):
    print('Смена ' + str(i+1)+ ': ' + str(shifts[i]))

# Часть 2
# TODO: Места чередуются и мужчины не могут стоять рядом друг с другом

shift_separator = []
new_shifts = []

for i in range(len(shifts)):
    shift_separator.append(str(shifts[i]).replace('(', '').replace(')', '').replace("'", "").replace(',', '').replace(' ', ''))
for i in shift_separator:
    if not 'MM' in i:
        new_shifts.append(i)


print("Часть 2\n На заводе заметили, что разговоры между мужчинами занимают рабочее время,"
      " потому было решено ввести правило: мужчины на смене не могут стоять рядом на конвейере\n"
      " Все возможные смены с четыремя мужчинами и оставшимися женщинами между ними:")

for i in range(len(new_shifts)):
    print('Смена ' + str(i+1)+ ': ' + str(new_shifts[i]))
