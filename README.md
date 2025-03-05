# PROJECT REQUIREMENTS #

- Identify the lexemes and token relationships given an input file (txt consisting of source code and commnets)

Ex. Tokens:
- keyword
- separator
- identifier
- integer
- float
- operator
- punctuator
- unknown

Should ignore whitespaces and comments

# Input is language of choice #

### Example Input ###

```python
a = 10 
b = 5

if a > b:
    print("a is greater than b")
else:
    print("b is greater than or equal to a")


for i in range(5):
    print("iteration", i)
```