# name = input("What is your name?")
# print("Hello, {}".format(name))
# num_times=int(input("How mant times do you want to repeat your name?"))
# for i in range(num_times):
#     print(name)

# Example of print()
# print("Hello, world!")

# # Example of input()
# name = input("What is your name? ")
# print(f"Hello, {name}!")

# # Example of string replication
# my_string = "Hello"
# print(my_string * 3)  # Output: HelloHelloHello


#testing 1
# print("Hello, World!")
# name=input("What is your name? ")
# my_string="Hello"
# print(my_string * 3)



# def Fibonacci(n):
#     if n<= 0:
#         print("Incorrect input")
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)
# print(Fibonacci(10))



# #elif is used when there are many conditions
# age = 19

# if age<=18:
#     print("Chotu")
# elif age<=60:
#     print("Sigma")
    
# # for is used to iterate sequence of items

# fruits = ["apple", "orange"]
# for fruit in fruits:
#     print(fruit.upper())
    
# # while is used to repeat a block of code
# count = 0 
# while count < 5:
#     print(count)
#     count += 1
    
# # break is used to end the loop
# numbers = [1,2,3,4,5]
# for num in numbers:
#     if num == 3:
#         break
#     print(num)
    
# #continue is used to skip a part of loop
# numbers = [1,2,3,4,5]

# for num in numbers:
#     if num % 2 == 0:
#         continue
#     print(num)


# List is an ordered collection of items of difeerent data types

# #append     used to add an item to at the end of list
# numbers = [1,2,3,4]
# numbers.append(5)
# print(numbers)

# #insert     used to add an item at a particular place it shift everything to right.
# numbers = [1,2,3,4,5]
# numbers.insert(1,1.5)
# print(numbers)

# #remove     used to remove an item from the list
# numbers = [1,2,6,3,4,5]
# numbers.remove(6)
# print(numbers)


# person = {"name": "alice", "age": "30", "city":"new york"}
# keys_list=list(person.keys())
# print(keys_list)
# if "name" in person.keys():
#     print("Name exists in the dictionary")



text = "Hello"
uppercase_text=text.upper()
print(text)
print(uppercase_text)