#Import any necessary libraries



# Define the token types
# KEYWORD, SEPERATOR, IDENTIFIER, OPERATOR, INTEGER, UNKNOWN, END
token_type = {
    'KEYWORD': 0,
    'SEPERATOR': 1,
    'IDENTIFIER': 2,
    'OPERATOR': 3,
    'INTEGER': 4,
    'UNKNOWN': 5,
    'END': 6
}

# Define the keywords in Python
keywords = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue',
    'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
    'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
    'return', 'try', 'while', 'with', 'yield'
] # 32 keywords

# Define token structure
class Token:
    def __init__(self, token_type, lexeme):
        self.token_type = token_type
        self.lexeme = lexeme

    def __str__(self):
        return f"Token Type: {self.token_type}, Lexeme: {self.lexeme}"
    

# Define the lexical analysis function
def lexical_analysis(input: str):
    """ Given the file text as input read the text line by line and return the identified token types"""
    white_space = ' '
    lexme = ''
    
    print("Set of lexemes and tokens (<lexemes> = <tokens>)")
    print("\"")
    # Need to resovlve the issue with last lexme in a line to be properly printed
    for i, char in enumerate(input):
        if char != white_space:
            lexme += char
            if (i + 1 < len(input)): 
                if input[i + 1] == white_space:
                    if lexme in keywords:
                        print(f"\"{lexme}\" = keyword")
                    elif lexme == '=' or lexme == '+' or lexme == '-' or lexme == '*' or lexme == '/' or lexme == '%' or lexme == '**' or lexme == '//' or lexme == '==' or lexme == '!=' or lexme == '>' or lexme == '<' or lexme == '>=' or lexme == '<=' or lexme == 'and' or lexme == 'or' or lexme == 'not':
                        print(f"\"{lexme}\" = operator")
                    elif lexme.isdigit():
                        print(f"\"{lexme}\" = integer")
                    elif lexme.isidentifier():
                        print(f"\"{lexme}\" = identifier")
                    elif lexme == '(' or lexme == ')' or lexme == '{' or lexme == '}' or lexme == '[' or lexme == ']' or lexme == ',' or lexme == ':' or lexme == '.' or lexme == ';' or lexme == '@':
                        print(f"\"{lexme}\" = seperator")
                    else:
                        print(f"\"{lexme}\" = unknown")
                    lexme = ''
                
    print (f"\"{lexme}\" = <seperator>") # Final lexme before end of file
    print("\"")

if __name__ == "__main__":
    '''Run lexical program on user inputted file'''
    full_text = ""
    # user_input = input("File Input: ")
    user_input = "source.txt"
    with open(user_input, "r") as file:
        full_text += file.read()
    # print(full_text) # Print the full text of the file

    print("Running lexical analyzer...")
    lexical_analysis(full_text)
    print("Lexical analysis complete!")