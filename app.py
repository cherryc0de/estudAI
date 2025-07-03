from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=groq_api_key)

app = Flask(__name__)

def gerar_resposta(pergunta, estilo, idioma):
    prompt = f"""
Você é uma tutora {estilo}, como uma kouhai fofa e dedicada de anime escolar.
Responda com carinho e entusiasmo, mas com conteúdo claro e educativo.
Idioma: {idioma}

Pergunta: {pergunta}
"""
    resposta = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="llama3-8b-8192"  # modelo novo, ativo e fofinho!
    )
    return resposta.choices[0].message.content

@app.route("/", methods=["GET", "POST"])
def index():
    resposta = ""
    if request.method == "POST":
        pergunta = request.form["pergunta"]
        estilo = request.form["estilo"]
        idioma = request.form["idioma"]
        resposta = gerar_resposta(pergunta, estilo, idioma)
    return render_template("index.html", resposta=resposta)

if __name__ == "__main__":
    app.run(debug=True)
