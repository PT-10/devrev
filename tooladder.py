class Argument:
    def __init__(self, name):
        self.arg_name = name
        self.arg_desc = None
        self.arg_type = None
        self.arg_example = None

    def add_description(self, desc):
        self.arg_desc = desc

    def set_type(self, type):
        self.arg_type = type

    def set_example(self, example):
        self.arg_example = example

class Tool:
    def __init__(self, name):
        self.tool_name = name
        self.desc = None
        self.arg_list = []

    def add_description(self, desc):
        self.desc = desc


