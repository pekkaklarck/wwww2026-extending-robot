# Listener interface

This directory demonstrates Robot Frameworks listener interface:

- [stop_on_failure.py](stop_on_failure.py) is a simple listener that can be used
  from the command line to stop execution if a test fails:

      robot --listener stop_on_failure.py tests.robot

- [Modifier.py](Modifier.py) demonstrates different ways how to modify and inspect
  data and results during execution. It can be used the same way as the listener
  above. It uses the optional `robot.api.interfaces.ListenerV3` base class and
  utilizes type hints.

- [LibraryWithListener.py](LibraryWithListener.py) shows how a library can register
  a listener. The library is used by [tests.robot](tests.robot) and does not need
  to be taken into use from the command line separately.

For more information see the
[Listener interface](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#listener-interface)
section in the *Robot Framework User Guide*.
