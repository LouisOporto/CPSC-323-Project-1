import re

# Define token patterns to represent each token type
TOKEN_PATTERNS = [
    (r'\bif\b|\belse\b|\bfor\b|\bwhile\b|\breturn\b|\bdef\b|\bclass\b', 'keyword'),
    (r'#[^\n]*', 'comment'),
    (r'\d+', 'integer'),
    (r'\b[a-zA-Z_]\w*\b', 'identifier'),
    (r'\+|\-|\*|\/|\=|\==|\!=|\>|\<|\>=|\<=', 'operator'),
    (r'[\(\)\{\}\[\],\.:]', 'separator'),
    (r'".*?"|\'.*?\'', 'string')
]
# Combine token patterns into a single regular expression
TOKEN_REGEX = '|'.join(f'(?P<{token_name}>{pattern})' for pattern, token_name in TOKEN_PATTERNS)
# print(TOKEN_REGEX)

def remove_comments_and_whitespace(text: str):
    ''' Function to remove coments and whitespace'''
    text = re.sub(r'#[^\n]*', '', text) # Remove comments
    return text


def lexical_analysis(input: str):
    ''' Function to perform lexical analysis '''
    print("<lexeme>: <token>") # Print format

    # Remove comments and whitespace from input
    input_string = remove_comments_and_whitespace(input)

    # Tokenize the input string
    for match in re.finditer(TOKEN_REGEX, input_string):
        for token_name in match.groupdict():
            lexeme = match.group(token_name)
            if lexeme:
                print('{0:10} = {1}'.format(lexeme, token_name)) # Result of each identified lexeme


if __name__ == "__main__":
    '''Run lexical program on user inputted file'''
    full_text = ""
    user_input = input("File Input: ")
    with open(user_input, "r") as file:
        full_text = file.read()

    # print(full_text) # Print the full text of the file

    print("Running lexical analyzer...")
    lexical_analysis(full_text)
    print("Lexical analysis complete!")