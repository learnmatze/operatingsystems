import re

# Phase 1: Lexikalische Analyse
def lexer(expression):
    tokens = re.findall(r'\d+|\+|\*|\/|\-|\(', expression)
    return tokens

# Phase 2: Syntaxanalyse (Parsing)
def parser(tokens):
    stack = []
    operators = {'+', '-', '*', '/'}
    output = []

    for token in tokens:
        if token.isnumeric():
            output.append(token)
        elif token in operators:
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()

    while stack:
        output.append(stack.pop())

    return output

# Phase 3: Semantische Analyse (Auswertung des Ausdrucks)
def evaluate_postfix(expression):
    stack = []
    for token in expression:
        if token.isnumeric():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
    return stack[0]

# Phase 4: Bytecode-Erzeugung
def generate_bytecode(expression):
    bytecode = []
    for token in expression:
        if token.isnumeric():
            bytecode.append(('PUSH', int(token)))
        elif token in ('+', '-', '*', '/'):
            bytecode.append(('BINARY_OP', token))
    return bytecode

math_expression = "3 + 5 * 2"
print(math_expression)

# Lexikalische Analyse
tokens = lexer(math_expression)
print("Tokens:", tokens)

# Syntaxanalyse
postfix_expression = parser(tokens)
print("Postfix Expression:", postfix_expression)

# Semantische Analyse (Auswertung)
result = evaluate_postfix(postfix_expression)
print("Ergebnis:", result)

# Bytecode-Erzeugung
bytecode = generate_bytecode(postfix_expression)
print("Bytecode:", bytecode)
