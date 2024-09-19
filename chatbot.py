import os
import google.generativeai as genai
import gradio as gr

# Retrieve Gemini API key from environment variable
API_KEY = "AIzaSyCrwpHbDi-msKra0YBHT4KNBsgS45ZwT9Q"
def query_gemini(prompt, history):
  try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(
        f"You are a medical assistant. Response as if you are a chatbot for doctors. Your name is MedicBot: {prompt}")

    # Check for valid response and access content
    if response and hasattr(response, 'candidates') and response.candidates:
      candidate = response.candidates[0]
      text = candidate.content.parts[0].text
      return text
    else:
      return "No valid response received."
  except Exception as e:
    print("Error occurred while checking Gemini:", e)
    return "An error occurred while processing your request."


# Create the Gradio interface
iface = gr.ChatInterface(
    fn=query_gemini,
    title="MedicBot Chatbot",
    description="Ask your medical queries",
    # Add other interface customization options as needed
)

# Launch the interface (adjust port as needed)
iface.launch(server_name="0.0.0.0", server_port=7861)
