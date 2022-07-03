def main():
    for_basic()
    for_multi_dimensional()
    for_dictionary()

def for_basic():
    names = ['dlghdwn', 'dlawjdgml', 'dltkdgns', 'dlwjdgns']
    for name in names:
        print("Hello, "+name+". Bye, "+name+".")

def for_multi_dimensional():
    persons = [
        ['dlghdwn', '1970', 'Boeun'],
        ['dlawjdgml', '1974', 'Seoul'],
        ['dltkdgns', '2000', 'Siheung'],
        ['dlwjdgns', '2002', 'Siheung']
    ]
    
    for person in persons:
        print('name: '+person[0]+', birthyear: '+person[1]+', birthplace: '+person[2])

    print("--------------------------------------------------")
    
    for name, birthyear, birthplace in persons:
        print('name: '+name+', birthyear: '+birthyear+', birthplace: '+birthplace)

def for_dictionary():
    persons = [
        {'name':'dlghdwn', 'birthyear':'1970', 'birthplace':'Boeun'},
        {'name':'dlawjdgml', 'birthyear':'1974', 'birthplace':'Seoul'},
        {'name':'dltkdgns', 'birthyear':'2000', 'birthplace':'Siheung'},
        {'name':'dlwjdgns', 'birthyear':'2002', 'birthplace':'Siheung'}
    ]

    for person in persons:
        for key in person:
            print(key,':',person[key])
        print('------------------------------------------------')

main()