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
` 
int main() {
    float x = 3.14; float y = 3.15;
    float z = x + y;
    bool boolean = true
    if (boolean) {
        std::cout << "Value Z:" << z << std::endl;
    }
    return 0;
}
`