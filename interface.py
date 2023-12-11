import gradio as gr
from main import predict
from tooladder import add_tool

with gr.Blocks() as demo:
    with gr.Tab("Chat"):
        gr.ChatInterface(predict)
    with gr.Tab("Tools"):
        input_components = [
    gr.Textbox(label = "Tool Name"),
    gr.Textbox(label = "Tool Description"),
    gr.Dropdown([1, 2, 3, 4, 5], label = "Number of Arguments"),
    *[gr.Textbox(label = f"Argument {i + 1} Name") for i in range(5)],
    *[gr.Textbox(label = f"Argument {i + 1} Description") for i in range(5)],
    *[gr.Textbox(label = f"Argument {i + 1} Type") for i in range(5)],
    *[gr.Textbox(label = f"Argument {i + 1} Example") for i in range(5)],
    ]

    output_component = gr.Textbox()

    gr.Interface(fn=add_tool, inputs=input_components, outputs=output_component).launch(debug=True)

demo.queue().launch()