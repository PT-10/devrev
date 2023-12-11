import json
import gradio as gr
from schema import tools
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

    def add_argument(self, name, desc, type, example):
        arg = Argument(name)
        arg.add_description(desc)
        arg.set_type(type)
        arg.set_example(example)
        self.arg_list.append(arg)

def add_tool(toolName, desc, num_args, *args):
    if toolName in tools:
        return "Tool with the same name already exists. Choose a different name."

    new_tool = Tool(toolName)
    new_tool.add_description(desc)

    for i in range(0, num_args * 4, 4):
        argName, argDesc, argType, argExample = args[i], args[i + 1], args[i + 2], args[i + 3]
        new_tool.add_argument(argName, argDesc, argType, argExample)

    tools[toolName] = {
        "description": new_tool.desc,
        "arguments": [
            {
                "arg_name": arg.arg_name,
                "arg_desc": arg.arg_desc,
                "arg_type": arg.arg_type,
                "arg_example": arg.arg_example
            } for arg in new_tool.arg_list
        ]
    }

    return json.dumps(tools, indent=4)

# Create Gradio interface
