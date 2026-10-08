# Library API

In this directory we have examples related to creating libraries.

## Basic features

[basics.py](basics.py) and [basics.robot](basics.robot) cover the basics of
the library API. That includes:

- Creating a library as a module with functions
- Using arguments
- Basics of argument conversion
- Logging
- Reporting status
- Returning values

These examples were created already before the workshop and participants were
expected to be familiar with the covered topics. The examples were gone through
together before continuing with more advanced topics, though.

## Advanced topics

[advanced.robot](advanced.robot) and [Advanced.py](Advanced.py) were created
during the workshop day. They contain examples related to the following topics:

- Creating library as a class with methods
- Library state and passing arguments to libraries
- Advanced argument conversion (restricting values with `Enum` and `Literal`,
  handling secrets, custom converters, ...)
- `@keyword` and `@library` decorators
- Embedded arguments
- Skipping tests, continuable failures and fatal errors.
- Documenting libraries and using the [Libdoc](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#library-documentation-tool-libdoc) tool

## Dynamic library API

[dynamic.robot](dynamic.robot) and [Dynamic.py](Dynamic.py) quickly introduce
the dynamic library API. This API is used, for example, by the
[Remote library API](https://github.com/robotframework/RemoteInterface) and
[PythonLibCore](https://github.com/robotframework/PythonLibCore) that in turn
is used by [SeleniumLibrary](https://github.com/robotframework/SeleniumLibrary)
and several other bigger libraries.

## More information

For more details about these features, and many more, see the
[Creating test libraries](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-test-libraries)
section in the *Robot Framework User Guide*.
