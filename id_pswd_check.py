def main():
    input_id = input("id : ")
    id1 = 'dltkdgns00'
    id2 = 'LeeKing'
    if input_id == id1:
        pswd_check(1)
    elif input_id == id2:
        pswd_check(2)
    else:
        print("wrong id")

main()

def pswd_check(id):
    input_pswd = input("password (six numbers): ")
    pswd1 = '111111'
    pswd2 = '222222'
    if id == 1:
        pswd = pswd1
    elif id == 2:
        pswd = pswd2
    else:
        print("ERROR")

    if input_pswd == pswd:
       print("Welcome")
    else:
        print("wrong password")

