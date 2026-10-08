# Parsing API

This directory quickly introduces Robot Framework's parsing API.
For more details see the [parsing API documentation](
https://robot-framework.readthedocs.io/en/stable/autodoc/robot.api.html#module-robot.api.parsing).

## Tokens

[tokens.py](tokens.py) shows how to parse a suite file into tokens. This
is a pretty low level API that can be used, for example, by syntax highlighters.
Token values could also be written back to the disk and modified on the fly.

Run the script like `python tokens.py tests.robot` to get tokens in
[tests.robot](tests.robot) printed to the console.

## Model

[model.py](model.py) demonstrates using a higher level parsing API that returns
a model that is easier to inspect and modify than raw tokens. The model is
implemented on top of Python's [ast](https://docs.python.org/3/library/ast.html)
module and internally contains the lower level tokens. This API is used
by editors like [RobotCode](https://robotcode.io/) as well as by code formatters
and linters such as [Robocop](https://robocop.dev/).

Run `python model.py tests.robot` to get the model from [tests.robot](tests.robot)
shown on the console. The script also modifies the model, writes modified data
back to the disk, and creates an executable suite based on the model and runs it.
