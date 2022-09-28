#Q1 loops

list = [12, 75, 150, 180, 145, 525, 50]
for number in list:
    if number > 500:
        break
    elif number > 150:
        continue
    elif number % 5 == 0:
        print(number)



