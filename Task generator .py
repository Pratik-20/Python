"""
Project: Arithmetic Exam Application

Work on project. Stage 2/4: Task generator

Task generator

Description
Any test includes at least one task. This task can vary in difficulty and required timeframes. There can be more than one task; they can demand different forms of answers. One thing remains — if there's a task, there's a solution. And we need to assess it.

Math tasks can vary in difficulty. 1 * 3 is easy. 75 * 34 is a bit more difficult. For the next stages, think about levels of difficulty that you can add!

For now, let's use random numbers from 2 to 9 and integer operations: +, - and *.

Objectives
Generate a math task that looks like a math operation. Use the requirements above. Print it.
Read the answer from a user.
Check whether the answer is correct. Print Right! or Wrong!
Examples

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

5 * 7
> 35
Right!
Example 2:

5 * 7
> 5
Wrong!
"""
import random
dict = ["+","*","-"]
a = random.randint(2,9)
b = random.randint(2,9)
c = random.choice(dict)
math = str(a) + c + str(b)
#print(eval(math))
print(math)
answer = int(input())
if answer == eval(math):
    print("Right!")
else:
    print("Wrong!")