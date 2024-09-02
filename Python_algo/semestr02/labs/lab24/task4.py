# Программа получает на вход число участников олимпиады N.
# Далее идет N строк, в каждой строке записана фамилия участника,
# затем, через пробел, набранное им количество баллов.
# # Выведите список участников (только фамилии) в порядке убывания набранных баллов.


def sort_by_score(members):
    members.sort(key=lambda x: x[1], reverse=True)


def print_names(lst):
    for el in lst:
        print(el[0])


if __name__ == '__main__':
    members = []
    while True:
        m = input()
        if not m:
            break
        name, score = m.split()
        members.append((name, int(score)))

    sort_by_score(members)
    print_names(members)

