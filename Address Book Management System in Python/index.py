#if else statement
gender=input ('enter your gender :')
name=input('entr your name :')
age=int(input('enter your age :'))
if age>=18:
    if gender=='m':
        print('hello mr.',name,'your wellcome')
    elif gender=='f':
        print('hello ms.',name,'your wellcome')
else:
    print('your age is not sufficient ..! sorry')

