from sly import Lexer
class TaipanLexer(Lexer):
    tokens = {WRITE, VARIABLE, BOOLEAN, NAME, INTEGER, STRING, ASSIGN, PLUS, MINUS, TIMES, DIVIDE}
    ignore = ' \t'
    WRITE  = r'write'
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    VARIABLE = r'new'
    BOOLEAN = r'Yes|No'
    ASSIGN = r'='
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    INTEGER = r'\d+'
    STRING = r'\".*?\"'
    @_(r'//.*')
    def COMMENT(self, t):
        pass
    @_(r'\d+')
    def INTEGER(self, t):
        t.value = int(t.value)
        return t
    @_(r'Yes|No')
    def BOOLEAN(self, t):
        return t
    @_(r'[a-zA-Z_][a-zA-Z0-9_]*')
    def NAME(self, t):
        return t
    @_(r'\".*?\"')
    def STRING(self, t):
        t.value = t.value[1:-1]
        return t
