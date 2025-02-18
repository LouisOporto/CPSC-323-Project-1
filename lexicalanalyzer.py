
token_type = {
    'KEYWORD': 0,
    'SEPERATOR': 1,
    'IDENTIFIER': 2,
    'OPERATOR': 3,
    'INTEGER': 4,
    'UNKNOWN': 5,
}

def lexical_analysis(input: str):
    """ Given the file text as input read the text line by line and return the identified token types"""
    for i, char in enumerate(input, 1):
        print('char', str(i).rjust(3, ' '), ':', char)
    


if __name__ == "__main__":
    '''Run lexical program on user inputted file'''
    print("Runnin lexical analysis tool\n")

    full_text = ""
    # user_input = input("File Input: ")
    user_input = "source.txt"
    with open(user_input, "r") as file:
        full_text += file.read()
    
    print(full_text)

    print("Running lexical analyzer...\n")
    lexical_analysis(full_text)