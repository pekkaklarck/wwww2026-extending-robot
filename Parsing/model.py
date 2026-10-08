import ast
import sys
try:
    import astpretty    # Third-party module to provide better debugging.
except ImportError:
    astpretty = None

from robot.api import TestSuite
from robot.api.parsing import get_model, ModelVisitor, Tags, Token, KeywordCall


try:
    path = sys.argv[1]
except IndexError:
    sys.exit("Usage: python model.py path")
model = get_model(path)


print(f"1. Model created from file '{path}':\n")
if astpretty:
    astpretty.pprint(model)
else:
    print(ast.dump(model, include_attributes=True))
print()


class Fixer(ModelVisitor):

    def visit_Tags(self, node: Tags):
        for token in node.get_tokens(Token.ARGUMENT):
            if token.value == "bad":
                token.value = "good"

    def visit_KeywordCall(self, node: KeywordCall):
        kw = node.get_token(Token.KEYWORD)
        if kw.value == "Log to konsole":
            kw.value = "Log to console"


print("2. Modify model and save data back to disk.\n")
Fixer().visit(model)
model.save()


print('3. Execute the modified model:\n')
suite = TestSuite.from_model(model)
suite.run()
