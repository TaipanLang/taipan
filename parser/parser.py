from lexer import TaipanLexer
from sly import Parser
class TaipanParser(Parser):
    def __init__(self):
        self.variable = {}
    tokens = TaipanLexer.tokens
    @_('expr PLUS term')
    def expr(self, p):
        return p.expr + p.term

    @_('expr MINUS term')
    def expr(self, p):
        return p.expr - p.term

    @_('term')
    def expr(self, p):
        return p.term

    @_('term TIMES factor')
    def term(self, p):
        return p.term * p.factor

    @_('term DIVIDE factor')
    def term(self, p):
        return p.term / p.factor

    @_('factor')
    def term(self, p):
        return p.factor

    @_('INTEGER')
    def factor(self, p):
        return p.INTEGER
    @_('write_str')
    def expr(self, p):
        return print(p.write_str)
    @_('write_int')
    def expr(self, p):
        return print(p.write_int)
    @_('write_bool')
    def expr(self, p):
        return print(p.write_bool)
    @_('WRITE STRING')
    def write_str(self, p):
        return p.STRING
    @_('WRITE INTEGER')
    def write_int(self, p):
        return p.INTEGER
    @_('WRITE BOOLEAN')
    def write_bool(self, p):
        return p.BOOLEAN

