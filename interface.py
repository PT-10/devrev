import json
import gradio as gr
from tooladder import Tool, Argument
from main import predict
from schema import tool_info


def add_tool(toolName, desc):
    if toolName in tool_info:
        return "Tool with the same name already exists. Choose a different name."
    if toolName == "":
        return "Tool name cannot be empty."
    if desc == "":
        return "Tool description cannot be empty."
    new_tool = Tool(toolName)
    new_tool.add_description(desc)
    tool_info[toolName] = {
        "description": new_tool.desc,
        "arguments": []
    }
    update_json()
    return json.dumps(tool_info, indent=4)

def add_argument(toolName, argName, argDesc, argType, argExample):
    if toolName not in tool_info:
        return "Tool with the given name does not exist. Choose a different name."

    if argName == "":
        return "Argument name cannot be empty"
    if argName in tool_info[toolName]["arguments"]:
        return "Argument with the same name already exists. Choose a different name."

    new_arg = Argument(argName)

    if argDesc == "":
        return "Argument description cannot be empty."
    new_arg.add_description(argDesc)
    new_arg.set_type(argType)
    new_arg.set_example(argExample)
    tool_info[toolName]["arguments"].append({
        "argument_name": new_arg.arg_name,
        "argument_description": new_arg.arg_desc,
        "argument_type": new_arg.arg_type,
        "argument_example": new_arg.arg_example
    })
    update_json()
    return json.dumps(tool_info, indent=4)

def delete_tool(toolName):
    if toolName not in tool_info:
        return "Tool with the given name does not exist. Choose a different name."

    tool_info.pop(toolName)
    update_json()
    return json.dumps(tool_info, indent=4)

def update_json():
    with open("tools.json", "w") as jsonFile:
        json.dump(tool_info, jsonFile)
    return True
  

with gr.Blocks() as demo:
    with gr.Tab("Chat"):
        gr.ChatInterface(predict)

    with gr.Tab("Tools"):
        input_components = [
        gr.Textbox(label = "Tool Name"),
        gr.Textbox(label = "Tool Description")]
        output_component = gr.Textbox()
        gr.Interface(fn=add_tool, inputs=input_components, outputs=output_component)

        delete_component = gr.Textbox(label = "Tool Name for deletion")
        del_output = gr.Textbox(value="", label="Output")
        del_btn = gr.Button(value="Delete Tool")
        del_btn.click(delete_tool, inputs=[delete_component], outputs=[del_output])

        arg_components = [gr.Textbox(label = "Tool Name"),
                          gr.Textbox(label = "Argument Name"),
                          gr.Textbox(label = "Argument Description"),
                          gr.Textbox(label = "Argument Type"),
                          gr.Textbox(label = "Argument Example")]
        txt_3 = gr.Textbox(value="", label="Output")
        add_argument_btn = gr.Button(value="Add Argument")
        add_argument_btn.click(add_argument, inputs=arg_components, outputs=[txt_3])
    
demo.queue().launch(debug=True)
