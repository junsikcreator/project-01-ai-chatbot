import gradio as gr
from chatbot import chat_with_ai

def respond(message: str, history: list):
    if not message.strip():
        return history, ""
    
    reply = chat_with_ai(message, history)
    history.append((message, reply))
    return history, ""

# Custom CSS for better look
custom_css = """
.chatbot {height: 70vh}
"""

with gr.Blocks(css=custom_css, title="My First AI Chatbot") as demo:
    gr.Markdown("# 🤖 Build Your First AI Chatbot\n**Project 1 — 30 AI Projects in 30 Days**")
    
    chatbot = gr.Chatbot(
        label="Chat History",
        height=600,
        show_copy_button=True,
        avatar_images=["👤", "🤖"]
    )
    
    with gr.Row():
        msg = gr.Textbox(
            placeholder="Type your message here...",
            scale=8,
            container=False
        )
        submit = gr.Button("Send", variant="primary", scale=1)
    
    with gr.Row():
        clear = gr.Button("Clear Chat")
        gr.Markdown("**Tip**: Press Enter to send")

    # Interactions
    msg.submit(respond, [msg, chatbot], [chatbot, msg])
    submit.click(respond, [msg, chatbot], [chatbot, msg])
    clear.click(lambda: [], None, chatbot)

    # Examples
    gr.Examples(
        examples=["What are the best productivity tips?", "Tell me a joke", "Explain quantum computing simply"],
        inputs=msg
    )

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False  # Set to True for public link
    )
