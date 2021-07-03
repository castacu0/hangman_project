"""Complete the square_sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9

numbers = [1,2,2]
def square_sum(numbers):
    return sum(x**2 for x in numbers)
square_sum(numbers)

WE MUST USE "RETURN" IN HERE

"""
numbers = [0, 3, 4, 5] #50

#1 ---- WORKS
def square_sum(numbers):
    return sum(w**2 for w in numbers)
caller = square_sum(numbers)
print(caller)


#2 ---- WORKS (missin' return)
# def square_sum(numbers):
#     return (sum(x**2 for x in numbers))
# caller = square_sum(numbers)
# print(caller)

#3
# def square_sum(*numbers):
#     suma = []
#     for i in numbers:
#         suma.append(i**2)
#     print(sum(suma))
# square_sum(1,2,9) #86


#4
# def square_sum(a,b,c):
#     r = a*a, b*b, c*c
#     sumaX = (sum(r))
#     print(sumaX)
# square_sum(1,2,2) #9

def square_sum(numbers):
    return sum(map(lambda x: x**2,numbers))

print("Using lambda:")
print(square_sum(numbers))