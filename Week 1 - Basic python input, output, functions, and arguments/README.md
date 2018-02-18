# Some tips from what we covered
By the way, when you see `#`, this signifies a `comment`. A `comment` tells your computer "hey, I'm just a bunch of words. Don't treat me like code. The purpose is to put explanations and notes in code for people to read.

This won't throw an error when you run it:
```
# Output abc
print("abc")
```
This will, because the lack of `#` tells the computer everything is code. "Output abc" is not code:
```
Output abc
print("abc")
```

## Types
- `character` - A character. a, b, c, etc.
- `string` - A word, or a **string** of characters. Represented by "Something in double quotes" or 'single quotes'
- `integer` - Some number, 1, 2, 3, etc.
- `float` - Some decimal, 1.2, 2.4, etc.

There are more, but more on that later.

## Casting Types
- `chr()` - Casts to a `character`.
- `int()` - Casts to an `integer`.
  - `int("3")` changes the string "3" to the integer 3
- `str()` - Casts to a `string`.
  - `str(3)` changes the integer 3 to the string "3"
- `float()` - Casts to a `float`.
  - `float(3)` changes the integer 3 to the float 3.0

There are more, but more on that later.

## Printing things
- `print("abc")` - prints a string, ends with a newline by default
```
print("abc")
print("abc")
```
outputs
```
abc
abc
```
- `print("abc", end="")` - changes the end from a newline to whatever you specify
```
print("abc", end="")
print("abc", end="")
```
outputs
```
abcabc
```

- `print("abc", end="123")` - changes the end from a newline to whatever you specify
```
print("abc", end="123")
print("abc", end="123")
```
outputs
```
abc123abc123
```

## String operations
You can add strings...
```
print("abc"+"123")
```
outputs
```
abc123
```

You can also multiply strings...
```
print("abc"*3)
```
outputs
```
abcabcabc
```

## Variables
Think like math variables. It holds some value, and lets you do operations with it.

```
# x is the variable. You can mutate it like in math.
x = 10
x = x + 20
print x
```
outputs
```
30
```

## Functions
A block of code that does one specific task. It's defined with `def`, and ends with a colon. Indent after for the duration of the function. Call it with the function name, and ().

```
# Defining the function
def some_func():
  print("hi")

# Calling the function
some_func()
```
outputs
```
hi
```

## Arguments
These are values you pass into the function when you call it. They go in the function definition (the `def` line). G values in corresponding order in the parentheses when calling the function.

```
# Defining the function
def add_two_numbers(x, y):
  print(x+y)

# Calling the function
add_two_numbers(10,30)
```
outputs
```
40
```

## Input
Take a user input, you typically store it in a variable. `input()` stores your input as a *string*.
```
x = input("Give me a number: ")
print(x)
```
outputs
```
Give me a number:
```
You type 50:
```
Give me a number: 50
50
```

# Time for an assignment
Do this in the `Change Counter` directory
