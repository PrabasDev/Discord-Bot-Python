import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)




model = genai.GenerativeModel("gemini-1.5-pro-latest")
prompt = 'me retorne o nome completo,a idade, o sexo, a altura, o peso, as afiliações, um resumo breve de sua história e uma imagem do personagem Zoro e ignore qualquer outro parametro que não seja os passados, retorne em json com as respectivas propriedades, propriedade nome o nome do personagem, propriedade sexo com sexo, propriedade idade, propriedade altura, propriedade peso, propriedade historia com o resumo da historia, propriedade imagem e não retorne nenhuma observação alem das passadas no prompt, retorne em json e não utilize acento em qualquer palavra.'

result = model.generate_content(prompt, generation_config=genai.GenerationConfig(
        response_mime_type="application/json"
    ),)
print(result.text)
