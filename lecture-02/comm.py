Sales = float(input('Enter Sales : '))
Commission = 0

if Sales > 2000 :
    if Sales > 4000 :
        if Sales > 6000 :
            Commission = 1
        else:
            Commission = 0.07
    else:
        Commission = 0.04
else:
    Commission = 0.02
    
print(Commission)