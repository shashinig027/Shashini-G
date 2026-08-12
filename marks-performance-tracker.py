while True:
    a=input('enter name of the student')
    b=int(input('enter Physics mark'))
    c=int(input('enter Chemistry mark'))
    d=int(input('enter Maths mark'))
    if b>100 or c>100 or d>100 or b<0 or c<0 or d<0:
        print('invalid marks, please enter marks between 0 and 100')
        continue
    e=(b+c+d)/3
    print('average marks of',a,'is',e)
    if e>=75:
        print('PASSED WIH DISTINCTION')
    elif e>=40 and e<75:
        print('PASSED')
    else:
        print('failed')    
    f=input('do you want to enter marks for another student? (yes/no)')
    if f.lower()!='yes':
        break
