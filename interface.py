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
    for args in tool_info[toolName]["arguments"]:
        if argName==args["name"]:
            return "Argument with the same name already exists. Choose a different name."

    new_arg = Argument(argName)

    if argDesc == "":
        return "Argument description cannot be empty."
    new_arg.add_description(argDesc)
    new_arg.set_type(argType)
    new_arg.set_example(argExample)
    tool_info[toolName]["arguments"].append({
        "name": new_arg.arg_name,
        "description": new_arg.arg_desc,
        "type": new_arg.arg_type,
        "example": new_arg.arg_example
    })
    update_json()
    return json.dumps(tool_info[toolName], indent=4)

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

def delete_argument(toolName, argName):
    if toolName not in tool_info:
        return "Tool with the given name does not exist. Choose a different name."

    arguments = tool_info[toolName]["arguments"]
    for i, arg in enumerate(arguments):
        if arg["name"] == argName:
            del arguments[i]
            update_json()
            return json.dumps(tool_info[toolName], indent=4)
    
    return f"Argument '{argName}' not found in tool '{toolName}'."

def modify_tool(toolName, newToolName):
    if toolName not in tool_info:
        return "Tool with the given name does not exist. Choose a different name."
    
    if newToolName not in tool_info:
        return "Tool with the given name does not exist. Choose a different name."

    if newToolName == "":
        return "New tool name cannot be empty."

    # Create a copy of the existing tool
    existing_tool = tool_info[toolName].copy()

    # Remove the existing tool
    tool_info.pop(toolName)

    # Add the modified tool with the new name
    tool_info[newToolName] = existing_tool
    update_json()
    return json.dumps(tool_info[newToolName], indent=4)


def modify_argument(toolName, argName, newArgName, argDesc, argType, argExample):
    if toolName not in tool_info:
        return "Tool with the given name does not exist. Choose a different name."

    arguments = tool_info[toolName]["arguments"]
    for i, arg in enumerate(arguments):
        if arg["name"] == argName:
            # Update the argument with the new values
            arg["name"] = newArgName if newArgName else argName
            arg["description"] = argDesc if argDesc else arg["description"]
            arg["type"] = argType if argType else arg["type"]
            arg["example"] = argExample if argExample else arg["example"]

            update_json()
            return json.dumps(tool_info[toolName], indent=4)

    return f"Argument '{argName}' not found in tool '{toolName}'."
  
def view_tools():
    return json.dumps(tool_info, indent=4)

with gr.Blocks() as demo:
    with gr.Tab("Chat"):
        gr.ChatInterface(predict)

    with gr.Tab("View Tools"):
        with gr.Tab("View Tools"):
            gr.Markdown(
                """
                View all tools
                """)
            gr.Interface(view_tools, inputs=[], outputs=gr.Textbox(label="Tool Set", lines=25))


    with gr.Tab("Add Tools"):
        gr.Markdown(
        """
        Add a tool
        """)
        input_components = [
        gr.Textbox(label = "Tool Name"),
        gr.Textbox(label = "Tool Description")]
        output_component = gr.Textbox()
        gr.Interface(fn=add_tool, inputs=input_components, outputs=output_component)

        gr.Markdown(
        """
        Add arguments to any existing tool
        """)
        arg_components = [gr.Textbox(label = "Tool Name"),
                          gr.Textbox(label = "Argument Name"),
                          gr.Textbox(label = "Argument Description"),
                          gr.Textbox(label = "Argument Type"),
                          gr.Textbox(label = "Argument Example")]
        txt_3 = gr.Textbox(value="", label="Output", interactive=True)
        gr.Interface(add_argument, inputs=arg_components, outputs=[txt_3])

    with gr.Tab("Modify Tools"):
        gr.Markdown(
            """
            Modify a tool or argument
            """)
        modify_tool_components = [gr.Textbox(label="Tool Name to be Modified"),
                                  gr.Textbox(label="New Tool Name")]
        modify_tool_output = gr.Textbox(value="", label="Output")
        gr.Interface(modify_tool, inputs=modify_tool_components, outputs=[modify_tool_output])

        modify_arg_components = [gr.Textbox(label="Tool Name"),
                                 gr.Textbox(label="Argument Name to be Modified"),
                                 gr.Textbox(label="New Argument Name (leave empty to keep the same)"),
                                 gr.Textbox(label="Argument Description (leave empty to keep the same)"),
                                 gr.Textbox(label="Argument Type (leave empty to keep the same)"),
                                 gr.Textbox(label="Argument Example (leave empty to keep the same)")]
        modify_arg_output = gr.Textbox(value="", label="Output")
        gr.Interface(modify_argument, inputs=modify_arg_components, outputs=[modify_arg_output])


    with gr.Tab("Delete Tools"):
        gr.Markdown(
        """
        Delete a tool
        """)
        delete_component = gr.Textbox(label = "Tool Name for deletion")
        del_output = gr.Textbox(value="", label="Output")
        gr.Interface(delete_tool, inputs=[delete_component], outputs=[del_output])

        gr.Markdown(
        """
        Delete argument of an existing tool
        """)
        arg_del_components = [gr.Textbox(label = "Tool Name"),
                          gr.Textbox(label = "Argument Name")]
        txt_4 = gr.Textbox(value="", label="Output", interactive=True)
        gr.Interface(delete_argument, inputs=arg_del_components, outputs=[txt_4])


    
demo.queue().launch(debug=True)