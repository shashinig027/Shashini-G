# LEETCODE PROBLEM #412: Fizz Buzz
# AUTHOR: [Your Name]
# 
# DESCRIPTION:
# Given an integer n, return a string array where numbers divisible by 3 are 
# replaced by "Fizz", numbers divisible by 5 are replaced by "Buzz", and numbers 
# divisible by both 3 and 5 are replaced by "FizzBuzz".
for i in range(1,16):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)