#PROJECT

weight = int(input("Enter your weight: "))
unit = input("Is it Kgs or lbs: ")

if unit == 'kgs':
    print(weight * 2.2,'lbs')
else:
    print(weight / 2.2,'kgs')
