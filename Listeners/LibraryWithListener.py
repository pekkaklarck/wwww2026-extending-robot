from robot.api.deco import keyword, library


# This library registers itself as a library. It could also register another object.
@library(scope="GLOBAL", listener="SELF")
class LibraryWithListener:

    def __init__(self):
        self.status = "initialized"

    def end_test(self, data, result):
        """Listener method resetting state automatically when a test ends."""
        self.status = "reset"

    @keyword
    def set_status(self, status):
        """Keyword for setting the `status`."""
        print(f"Previous status: {self.status}")
        self.status = status
        print(f"New status: {self.status}")
