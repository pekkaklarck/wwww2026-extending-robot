class Dynamic:

    def get_keyword_names(self):
        return ["Dynamic keyword", "Dynamic with arguments"]

    def run_keyword(self, name, args, named):
        print(f"Running keyword '{name}' with {args} and {named}.")

    def get_keyword_arguments(self, name):
        if name == "Dynamic with arguments":
            return ["first", "second", "named"]
        return []
