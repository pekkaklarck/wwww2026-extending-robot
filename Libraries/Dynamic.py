class Dynamic:

    def get_keyword_names(self):
        """Return names of the keywords that the library contains.

        This is a mandatory method in the dynamic library API.
        """
        return ["Dynamic keyword", "Dynamic with arguments"]

    def run_keyword(self, name, args, named):
        """Execute a keyword with the given arguments.

        This is a mandatory method in the dynamic library API.
        """
        print(f"Running keyword '{name}' with {args} and {named}.")

    def get_keyword_arguments(self, name):
        """Return argument specification to the specified keyword.

        This information is used for argument validation and shown in Libdoc
        documentation.

        This is one of the optional methods in the dynamic library API.
        """
        if name == "Dynamic with arguments":
            return ["first", "second", "named"]
        return []
