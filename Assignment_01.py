# Comprehensive list:
#1.Write a list comprehension to generate squares of numbers from 1 to 10.
squares = [x**2 for x in range(1, 11)]
print(squares)
# 2. Create a list of even numbers between 1 and 50 using list 
# comprehension.
evens = [x for x in range(1, 51) if x % 2 == 0]
print(evens)
# 3. Convert all strings in a list to uppercase using list comprehension.
strings = input(str("Enter a string :"))
upper_list = [s.upper() for s in strings]
print(upper_list)
# 4. Given a list of integers, create a new list that contains only the positive 
# numbers.
nums = [1,-2,3,4,-5,6]
positives = [x for x in nums if x > 0]
print(positives)
# 5. Create a list of tuples (num, num^2) for numbers 1 to 5.
tuples = [(x, x**2) for x in range(1, 6)]
print(tuples)
# 6. Extract all vowels from a given string using list comprehension.
text = str(input("Enter a string: "))
vowels = [ch for ch in text if ch.lower() in "aeiou"]
print(vowels)
# 7. Flatten a 2D list using list comprehension.
matrix = [[1,2,3],[4,5,6]]
flat = [item for sublist in matrix for item in sublist]
print(flat)
# 8.Replace all negative numbers in a list with 0 using list comprehension.
nums = [1,-2,3,4,-5]
replaced = [x if x >= 0 else 0 for x in nums]
print(replaced)
# 9. Given a list of words, create a list of lengths of each word.
words = ["hrishikesh","Mrudula","Deshpande","Paranjape"]
lengths = [len(word) for word in words]
print(lengths)
# 10. Filter out words that start with the letter 'A' or 'a'.
word = ["Hrishikesh","Mrduula","Akansha","Akashya","ammco","apple"]
filter_word = [w for w in word if not w.lower().startswith('a') and not w.startswith("A")]
print(filter_word)
# 11. From a list of numbers, generate a list of “even” or “odd” strings using 
# list comprehension.
list_num = [1,2,3,4,5,6,7,8,9,10]
Even_num = ["even" if l % 2 == 0 else "odd" for l in list_num]
print(Even_num)
# (Like → [“even”, “odd”, “odd”, “even”…])
# 12. Create a list of numbers divisible by both 3 and 5 in range 1–100.
divisible = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print(divisible)
# 13. Write a nested list comprehension to generate a multiplication table 
# for 1–5.
tabel = [[i*j for j in range(1,6)] for i in range(1,6)]
print(tabel)
# 14.Convert a dictionary’s keys into a list using list comprehension.
my_dict = {"name":'Hrishikesh',"email":"hrishikeshdeshpande12@gmail.com","age":22}
key_list = [k for k in my_dict]
print(key_list)
# 15.Extract numeric digits from a string using list comprehension.
text = input("Enter a alphanumeric text: ")
Ex_num = [ch for ch in text if ch.isdigit()]
print(Ex_num)

# 16. Use list comprehension to remove all spaces from a string.
text_str = input("Enter a string: ")
no_spaces = [ch for ch in text_str if ch != " "]
print(no_spaces)
# 17. Create a list of characters that appear more than once in a string.
String_text = input("Enter a string: ")
Charecter = [ch for ch in set(String_text) if String_text.count(ch) > 1]
print(Charecter)
# 18. From a list of sentences, generate a list of all words (split using list 
#  comprehension).
sentences = ["Hi I am Hrishikesh","I am 22 years old","I am a Associate Software Engineer at Bizmetric"]
all_words = [word for sentence in sentences for word in sentence.split()]
print(all_words)
# 19. Create a list of unique elements from a list using list comprehension + 
# condition.
lst = ["Hrishikesh",1,"Deshpande"]
unique = [x for i,x in enumerate(lst) if x not in lst[:i]]
print(unique)
# 20. Generate all pairs (x, y) where x is from list A and y is from list B 
#  (cartesian product).
A = [1,2,3,4]
B = [5,6,7,8]
pairs = [(x,y) for x in A for y in B]
print(pairs)
# Lambda functions
# 1. Write a lambda to add two numbers.
add = lambda a,b: a+b 
print(add(1,2))
# 2.Create a lambda to check if a number is even.
is_even = lambda x:x % 2 == 0
print(is_even(4))
# 3. Write a lambda to get the last character of a string.
last_char = lambda s:s[-1]
print(last_char("Hrishikesh"))
# 4.Use lambda with map() to square every number in a list.
nums = [1,2,3,4,5]
squares = list(map(lambda x:x**2 ,nums))
print(squares)
# 5.Use lambda with filter() to get only odd numbers from a list.
nums = [1,3,4,5,6]
odds = list(filter(lambda x:x%2 != 0,nums))
print(odds)
# 6. Use sorted() + lambda to sort a list of tuples by second value.
tuples = [(1,2),(3,4),(5,6)]
sorted_list = sorted(tuples,key = lambda x:x[1])
print(sorted_list)
# 7. Create a lambda to check if a string is a palindrome
is_pallindrome = lambda s:s == s[::-1]
print(is_pallindrome("SiS"))

# 8. Use lambda to find maximum of three numbers.
max_three = lambda a,b,c : max(a,b,c)
print(max_three(23,22,21))
# 9. Write a lambda to reverse a string.
reverse = lambda s:s[::-1]
print(reverse)
# 10. Use lambda with map() to convert a list of strings to integers.
strings = ["1","25","300"]
ints = list(map(lambda x: int(x),strings))
print(ints)
# 11. Use lambda with filter() to remove empty strings from a list.
strings = ["hrihsi"," ","snoei","nsof"]
non_empty = list(filter(lambda s:s != " ",strings))
print(non_empty)
# 12. Use lambda to compute factorial using reduce() (yeah, that one-liner 
# madness).
from functools import reduce
factorial = lambda n: reduce(lambda a,b:a*b,range(1,n+1),1)
print(factorial(5))
# 13. Write a lambda that returns the larger of two numbers.
larger = lambda a,b:a if a > b else b  
print(larger(12,13))
# 14. Use lambda to check if number is divisible by 5.
num = int(input('Enter a number: '))
div = lambda x:x % 5 == 0
if div(num):
    print("Number is divisibel by 5:",num)
else:
    print("Number is not divisible by 5")


# 15. Use lambda + map() to add 10 to each element of a list.
nums = [1,2,3,4,5,6]
plus_ten = list(map(lambda x:x + 10,nums))
print(plus_ten)
# 16. Use lambda to sort a list of dictionaries by a key (like "age").
people = [{"name":"Hrishikesh","age":21},{"name":"Mrudula","age":22},{"name":"Akansha","age":19}]
sorted_dicts = sorted(people,key = lambda x:x["age"])
print(sorted_dicts)
# 17. Write a lambda that returns True if a character is a vowel.
str = input("Enter a string: ")
is_vowel = lambda ch:ch.lower() in "aieou"
if is_vowel(str):
    print("The Entered character has a vowel in it")
else:
    print("The Entered character has no vowel in it")
# 18. Use lambda + filter to extract words of length > 5 from a list.
words = ["hrishikesh","Mrudula","Des","para"]
long_words = list(filter(lambda w: len(w) > 5,words))
print(long_words)
# 19. Use lambda to calculate the area of a circle (πr²).
radius = int(input("Enter the radius of circle: "))
area_circle = lambda r: 3.14159* r**2
print(area_circle(radius))
# 20. Write a lambda to remove duplicates from a list using filter + set.
lst = ["Hello","Hello","Number"]
remove_dupes = list(filter(lambda x: True,set(lst)))
print(remove_dupes)
# 21. Use lambda with reduce() to find the product 
# of all numbers in a list.
from functools import reduce
nums = [1,2,3,4,5]
product = reduce(lambda a,b:a*b,nums)
print(product)
# 22. Write a lambda that returns absolute value of a number.
absolute = lambda x:x if x> 0 else -x
print(absolute(4))
# 23. Use lambda to sort a list of strings by their length.
sorted_strings = sorted(strings, key=lambda s: len(s))

# 24. Use lambda to get only uppercase characters from a string.
upper_chars = list(filter(lambda ch: ch.isupper(), text))

# 25. Write a lambda that returns the square if number is even, cube if odd.
even_square_odd_cube = lambda x: x**2 if x % 2 == 0 else x**3
# 26. Use lambda with map to convert Celsius to Fahrenheit.
celsius = [24]
fahrenheit = list(map(lambda c: (c * 9/5) + 32,celsius))
print(fahrenheit)
# 27. Write a lambda to check if two strings are anagrams.
is_anagram = lambda a, b: sorted(a) == sorted(b)
# 28. Use lambda to extract only numeric values from a mixed list.
mixed = [12,"nfsk","sjnf",1323]
numeric_vals = list(filter(lambda x: isinstance(x, (int, float)), mixed))
# 29. Use lambda inside any() to check if any list element is negative.
any_negative = any(map(lambda x: x < 0, nums))
# 30. Use lambda to generate a function that multiplies any number by n
multiplier = lambda n: (lambda x: x * n)
