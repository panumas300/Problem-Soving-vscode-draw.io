Principal = float(input('Principal : '))
Interest = float(input('Interest : '))
Years = int(input('years : '))
Time = int(input('Time : '))

Amount = Principal * (1 + Interest/Time) ** (Years * Time)

print('Total Amount : ',Amount)
print('Begining Principal : ',Principal)
print('Interest Rate : ',Interest)
print('Number of Years : ',Years)
print('Number of Time Interest is Compounded Yearly : ',Time)