def convert_to_roman(num):
    numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    symbols = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','DM','M']
    i = len(numbers) - 1
     
    while num:
        div = num // numbers[i]
        num %= numbers[i]
 
        while div:
            print(symbols[i], end ='')
            div -= 1
        i -= 1

convert_to_roman(1522)