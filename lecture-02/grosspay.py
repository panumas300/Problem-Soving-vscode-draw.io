hours = 0
pay_rate = 0
grosspay = 0


def read(grosspay):
    global hours
    global pay_rate
    hours = int(input('Enter your hours:'))
    pay_rate = int(input('Enter your hours:'))




def cal(pay_rate,hours):

    return hours * pay_rate 




def print_1(result):
    global hours
    global pay_rate

    print(cal(pay_rate,hours))

def main():
    do_you_want = 'y'
    while do_you_want.lower() == 'y':
        read()
        res = cal()
        print_1(res)
        do_you_want = input('Do you want to cal again :')

main()