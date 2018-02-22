def latin(num):
        ar = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        latin = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        i = 0
        result = ""
        while num > 0:
            for j in range(num//ar[i]):
                result += latin[i]
                num -= ar[i]
            i += 1
        print (result)
n=raw_input('input the number')
if  n>=0:
 try:
  latin(int(n))
 except ValueError :
    print('the number is invalid')
