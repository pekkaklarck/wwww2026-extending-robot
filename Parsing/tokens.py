import sys

from robot.api.parsing import get_tokens


path = sys.argv[1]
for token in get_tokens(path):
    print(repr(token))
