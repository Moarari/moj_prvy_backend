stu = [['Miso','5',1],['Filip','9',2],['kubo','7',3],['kristof','8',7],['marian','8',39],['fico','8',4]]


def abc():
    for i in range(len(stu)):
        for j in range(0, len(stu) - i - 1):
            if stu[j][0].lower() > stu[j + 1][0].lower():
                stu[j], stu[j + 1] = stu[j + 1], stu[j]
    print(stu)
def cba():
    for i in range(len(stu)):
        for j in range(0, len(stu) - i - 1):
            if stu[j][0].lower() < stu[j + 1][0].lower():
                stu[j], stu[j + 1] = stu[j + 1], stu[j]
    print(stu)
def a123():
    for i in range(len(stu)):
        for j in range(0, len(stu) - i - 1):
            if stu[j][1].lower() > stu[j + 1][1].lower():
                stu[j], stu[j + 1] = stu[j + 1], stu[j]
    print(stu)
def a321():
    for i in range(len(stu)):
        for j in range(0, len(stu) - i - 1):
            if stu[j][1].lower() < stu[j + 1][1].lower():
                stu[j], stu[j + 1] = stu[j + 1], stu[j]
    print(stu)
def chyba1():
    print('Zadaj 1 pre abcd, 2 pre dcba, 3 pre 123 vek, 4 pre 321 vek ')
    vstup=input()
    if vstup == 1:
        abc()
    elif vstup == 2:
        cba()
    elif vstup == 3:
        a123()
    elif vstup == 4:
        a321()
    else:
        chyba1()
def krok1():
    print('Vyber si podla coho chces svojuch studentov zoradit')
    print('Tvoji studenti:')
    for i in stu:
        print(i[0])
    print('')
    print('Zadaj 1 pre abcd, 2 pre dcba, 3 pre 123 vek, 4 pre 321 vek ')
    vstup=input()
    if vstup == '1':
        abc()
    elif vstup == '2':
        cba()
    elif vstup == '3':
        a123()
    elif vstup == '4':
        a321()
    else:
        chyba1()
krok1()