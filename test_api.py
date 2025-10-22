from google import genai

client = genai.Client(api_key="AIzaSyCo9MP15NaOiCt3pzz6HviP_pQKf9VjeUc")

models = client.models.list()

for m in models:
    print(m.name)
