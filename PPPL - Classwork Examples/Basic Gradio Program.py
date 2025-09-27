import gradio as gr

def fx(name):
    print(name)


demo = gr.Interface(fn=fx, inputs = 'text', outputs = 'text')

demo.launch()
