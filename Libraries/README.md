# Library API

In this directory we have examples related to creating libraries.

[basics.py](basics.py) and [basics.robot](basics.robot) cover the basics of
the library API. That includes creating a library as a module, creating keyword
as a function, logging, basics of argument conversion and reporting status.
Participants should be familiar with these topics beforehand, but we go through
them quickly before continuing with more advanced topics.

Further examples related to following topics will be created during the training:

- Library state and passing arguments to libraries
- Advanced argument conversion (restricting values with `Enum` and `Literal`,
  using `Secret`, custom converters, ...)
- `@keyword` and `@library` decorators
- Embedded arguments
- Skipping tests
- Continuable and fatal failures
- Documenting libraries and Libdoc
- Dynamic library API
