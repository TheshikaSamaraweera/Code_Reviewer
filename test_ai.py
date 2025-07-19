import google.generativeai as genai

genai.configure(api_key="AIzaSyDaW3FIrAlu3Kf_iLIDt8j5wlOw3lXTDiY")

model = genai.GenerativeModel("gemini-2.0-flash")

response = model.generate_content("What's the capital of France?")
print(response.text)
