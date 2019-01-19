# These solutions are not meant to serve as a python
# script.  They are simply solution methods to the 
# associated problem found at https://codingbat.com/python/Warmup-1

#1
def sleep_in(weekday, vacation):
    return not weekday or vacation


#2
def monkey_trouble(a_smile, b_smile):
    return a_smile and b_smile or not a_smile and not b_smile


#3
def sum_double(a, b):
    if a == b:
        return 2*(a+b)
    
    else:
        return a+b


#4
def diff21(n):
    if n < 22:
        return 21 - n
    
    else:
        return (n-21)*2


#5
def parrot_trouble(talking, hour):
    return (talking and (hour < 7 or hour > 20))


#6
def makes10(a, b):
    return (a + b == 10) or a == 10 or b == 10


#7
def near_hundred(n):
    return n < 111 and n > 89 or n < 211 and n > 189


#8
def pos_neg(a, b, negative):
    return a < 0 and b > 0 and not negative or a < 0 and b < 0 and negative or a > 0 and b < 0 and not negative


#9
def not_string(str):
    if len(str) >= 3 and str[:3] == "not":
        return str
    return "not " + str


#10
def missing_char(str, n):
    return str[:n] + str[n+1:]


#11
def front_back(str):
    if len(str) < 2:
        return str
  
    return str[len(str)-1] + str[1:len(str)-1] + str[0]


#12
def front3(str):
    if len(str) < 3:
        return str + str + str
    return str[0:3] + str[0:3] + str[0:3]

