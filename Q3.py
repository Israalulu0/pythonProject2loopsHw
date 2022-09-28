#Q3
number = 76542
reverse=0

while number >0:
#isolate the last digit from number by %10
     lastdigit=number%10

#append the last digit to reverse, we first multiply the reverse by 10 so the ones column becomes the tens

     reverse=reverse*10+lastdigit

#remove the last digit from the original number and take the nearest smallest integer
     import math
     number=math.floor(number/10)

print(reverse)



