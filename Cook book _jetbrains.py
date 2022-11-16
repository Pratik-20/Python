"""
Cook book

if statement

Any recipe starts with a list of ingredients. Below is an extract from a cookbook with the ingredients for some dishes.
Write a program that tells you what recipe you can make based on the ingredient you have.

The input format:

A name of some ingredient.

The output format:

A message that says "food time!" where "food" stands for the dish that contains this ingredient. For example, "pizza time!".
If the ingredient is featured in several recipes, write about all of them in the order they're featured in the cook book.

Sample Input 1:

basil
Sample Output 1:

pasta time!
Sample Input 2:

flour
Sample Output 2:

apple pie time!
chocolate cake time!

"""
# Program.....

pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

ingredient = input()
if ingredient in pasta:
    print("pasta time!")
if ingredient in apple_pie:
    print("apple pie time!")
if ingredient in ratatouille:
    print("ratatouille time!")
if ingredient in chocolate_cake:
    print("chocolate cake time!")
if ingredient in omelette:
    print("omelette time!")
