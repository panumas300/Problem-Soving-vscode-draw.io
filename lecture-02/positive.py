def main():
    again = 'y'
    while again.lower() == 'y' :

        pay = int(input('Enter your pay : '))
        bonus = 0

        if pay <= 1000 :
            bonus = 10
        elif pay <= 2000 :
            bonus = 50
        else:
            bonus = 100

        total = pay + bonus

        print('Pay : ',pay)
        print('Bonus : ',bonus)
        print('Total : ',total)
    
        again = input('Do you want to do this again (y/n) :  ')

main()