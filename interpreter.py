from lexer import TaipanLexer
from parser import TaipanParser
class TaipanInterpreter:
    def __init__(self, code):
        self.code = code
        self.variables = {}
        self.output = self.execute()
    def execute(self):
        lexer = TaipanLexer()
        parser = TaipanParser()
        tokens  = lexer.tokenize(self.code)
        result = parser.parse(tokens)
        return result
print("Taipan 0.0.1")
print("Type 'exit' to exit")
code = ""
while code != "exit":
    code = input("Taipan >> ")
    interpreter = TaipanInterpreter(code)
    interpreter.output