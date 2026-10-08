# Model modifiers

This directory demonstrates modifying tests and results using model modifiers
and otherwise. We unfortunately did not have time to go through these examples
during the workshop, but hopefully the quick introduction here as well as the
examples themselves help understanding how and why to use model modifiers.

Modifiers work with the same data and result model objects as listeners using
the API version 3. Listeners always get access to both the data and the result
objects, but modifiers work either with data or with results. It is typically
easiest to go through these model structures by using
[visitors](https://robot-framework.readthedocs.io/en/stable/autodoc/robot.model.html#module-robot.model.visitor).

Modifiers, similarly as listeners, can get arguments so that they are embedded
to the modifier name or path like `RunEveryXth.py:2:1`. Automatic argument
conversion works based on the argument types the same way as with libraries.

For more details about model modifiers see the
[Robot Framework User Guide](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#programmatic-modification-of-test-data).
The model objects used by modifiers are documented
as part of the [Robot Framework API docs](http://robot-framework.readthedocs.org/)

## Data modifiers

[RunEveryXth.py](RunEveryXth.py) demonstrates modifying data after it has been parsed
but before it is executed. It can be enabled by using the `--prerunmodifier`
option:

    robot --prerunmodifier RunEveryXth.py tests.robot
    robot --prerunmodifier RunEveryXth.py:2:1 tests.robot

## Result modifiers

[FailSlow.py](FailSlow.py) shows how to inspect and modify results after execution.
It can be activated as part of execution or when using the Rebot tool by
using the `--prerebotmodifier` option:

    robot --prerebotmodifier FailSlow.py:0.05 tests.robot
    rebot --prerebotmodifier FailSlow.py:0.05 output.xml

It can also be executed as script after execution so that it modifies the output file:

    python FailSlow.py 0.05 output.xml
