from robot import running, result
from robot.api.interfaces import ListenerV3


class Modifier(ListenerV3):

    def start_test(self, data: running.TestCase, result: result.TestCase):
        data.body.create_keyword("Log", ["New keyword!"])

    def end_keyword(self, data: running.Keyword, result: result.Keyword):
        if result.status == "FAIL":
            result.status = "PASS"
            index = data.parent.body.index(data)
            retry = data.copy(name="Log")
            data.parent.body.insert(index + 1, retry)

    def start_library_keyword(
        self,
        data: running.Keyword,
        implementation: running.LibraryKeyword,
        result: result.Keyword,
    ):
        print(
            f"Starting library keyword '{implementation.name}' from "
            f"'{implementation.owner.name}' on line {implementation.lineno}."
        )

    def start_user_keyword(
        self,
        data: running.Keyword,
        implementation: running.UserKeyword,
        result: result.Keyword,
    ):
        print(
            f"Starting user keyword '{implementation.name}' in "
            f"'{implementation.owner.source}' on line {implementation.lineno}."
        )
        implementation.body.create_keyword("Log", ["Another new keyword!"])
