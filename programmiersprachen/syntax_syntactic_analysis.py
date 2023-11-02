# Lexikalische Analyse (Tokenisierung)
import re
import sys
# Lexeme definieren
TOKENS = [
    (r'[ \n\t]+', None),  # Whitespace
    (r'\d+', 'NUMBER'),  # Ganze Zahlen
    (r'\+', 'PLUS'),     # Addition
    (r'-', 'MINUS'),     # Subtraktion
    (r'\*', 'MULTIPLY'), # Multiplikation
    (r'/', 'DIVIDE'),    # Division
]

def lex(input_string):
    tokens = []
    position = 0

    while position < len(input_string):
        match = None
        for token_expr in TOKENS:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(input_string, position)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character: %s\n' % input_string[position])
            sys.exit(1)
        else:
            position = match.end(0)
    return tokens

# Beispiel: Lexikalische Analyse
input_string = "3 + 5 * 2"
tokens = lex(input_string)
print(tokens)

# Syntaxanalyse (Parsing)

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None

    def parse(self):
        self.advance()
        result = self.expr()
        if self.current_token is not None:
            sys.stderr.write('Unexpected token: %s\n' % self.current_token[0])
            sys.exit(1)

        return result

    def advance(self):
        if self.tokens:
            self.current_token = self.tokens.pop(0)
        else:
            self.current_token = None

    def factor(self):
        token = self.current_token
        if token[1] == 'NUMBER':
            self.advance()
            return int(token[0])
        elif token[0] == '(':
            self.advance()
            result = self.expr()
            if self.current_token[0] != ')':
                sys.stderr.write('Expected closing parenthesis\n')
                sys.exit(1)
            self.advance()
            return result

    def term(self):
        result = self.factor()
        while self.current_token and self.current_token[1] in ('MULTIPLY', 'DIVIDE'):
            if self.current_token[1] == 'MULTIPLY':
                self.advance()
                result *= self.factor()
            else:
                self.advance()
                result /= self.factor()
        return result

    def expr(self):
        result = self.term()
        while self.current_token and self.current_token[1] in ('PLUS', 'MINUS'):
            if self.current_token[1] == 'PLUS':
                self.advance()
                result += self.term()
            else:
                self.advance()
                result -= self.term()
        return result

# Beispiel: Syntaxanalyse
tokens = lex("3 + 5 * 2")
parser = Parser(tokens)
result = parser.parse()
print(result)