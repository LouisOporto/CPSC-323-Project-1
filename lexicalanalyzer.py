import re

# Define token patterns
TOKEN_PATTERNS = [
    (r'\bif\b|\belse\b|\bfor\b|\bwhile\b|\breturn\b|\bdef\b|\bclass\b', 'keyword'),
    (r'#[^\n]*', 'comment'),
    (r'\d+', 'integer'),
    (r'\b[a-zA-Z_]\w*\b', 'identifier'),
    (r'\+|\-|\*|\/|\=|\==|\!=|\>|\<|\>=|\<=', 'operator'),
    (r'[\(\)\{\}\[\],\.:]', 'separator'), # Same as delimiters
    (r'".*?"|\'.*?\'', 'string')
]

# Combine patterns into a single regex
TOKEN_REGEX = '|'.join(f'(?P<{token_name}>{pattern})' for pattern, token_name in TOKEN_PATTERNS)

# Function to remove comments and whitespace
def remove_comments_and_whitespace(text: str):
    text = re.sub(r'#[^\n]*', '', text) # Remove comments
    return text

def lexical_analysis(input: str):
    print("<lexeme>: <token>")

    # Remove comments and whitespace from input
    input_string = remove_comments_and_whitespace(input)

    # Tokenize the input string
    for match in re.finditer(TOKEN_REGEX, input_string):
        for token_name in match.groupdict():
            lexme = match.group(token_name)
            if lexme:
                print('{0:10} = {1}'.format(lexme, token_name))

if __name__ == "__main__":
    '''Run lexical program on user inputted file'''
    full_text = ""
    # user_input = input("File Input: ")
    user_input = "source.txt"
    with open(user_input, "r") as file:
        full_text = file.read()

    # print(full_text) # Print the full text of the file

    print("Running lexical analyzer...")
    lexical_analysis(full_text)
    print("Lexical analysis complete!")