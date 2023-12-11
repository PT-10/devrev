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
        gr.Textbox(label = f"Argument Name"),
        gr.Textbox(label = f"Argument Description"),
        gr.Textbox(label = f"Argument Type"),
        gr.Textbox(label = f"Argument Example")]

        output_component = gr.Textbox()

        gr.Interface(fn=add_tool, inputs=input_components, outputs=output_component)
    
demo.queue().launch(debug=True)