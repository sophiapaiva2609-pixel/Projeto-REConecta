from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

BASE_DADOS_UNIDADES = [
    {
        "nome": "UPA do Ibura",
        "horario": "24 horas (Todos os dias)",
        "atende_urgencia": True,
        "insumos": ["soro antiescorpiônico", "soro antiofídico", "clinica medica", "pediatria"],
        "status": "Aberta"
    },
    {
        "nome": "Policlínica e Maternidade Professor Barros Lima",
        "horario": "Segunda a Sexta, das 07h às 19h",
        "atende_urgencia": False,
        "insumos": ["clinica medica", "pediatria", "ginecologia"],
        "status": "Fechada (Abre amanhã às 07h)"
    },
    {
        "nome": "UPA dos Torrões",
        "horario": "24 horas (Todos os dias)",
        "atende_urgencia": True,
        "insumos": ["soro antiescorpiônico", "ortopedia", "clinica medica"],
        "status": "Aberta"
    }
]

class MensagemUsuario(BaseModel):
    mensagem: str

@app.post("/chat")
def responder_chat(dados: MensagemUsuario):
    texto = dados.mensagem.lower()
    
    # 2. Lógica para detectar caso de escorpião / animais peçonhentos
    if "escorpião" in texto or "picada" in texto or "mordida" in texto:
        unidades_aptas = [u for u in BASE_DADOS_UNIDADES if "soro antiescorpiônico" in u["insumos"]]
        
        resposta = (
            "⚠️ **Atenção: Picada de animal peçonhento exige atendimento rápido!**\n\n"
            "Não vá para qualquer posto. Encontrei as unidades mais próximas que **possuem o soro antiescorpiônico** disponível agora:\n\n"
        )
        
        for u in unidades_aptas:
            resposta += f"🏥 **{u['nome']}**\n"
            resposta += f"   • Status: {u['status']} ({u['horario']})\n"
            resposta += f"   • O que tem: Soro antiescorpiônico disponível\n\n"
            
        resposta += "Recomendamos ligar para o SAMU (192) caso haja sintomas graves de envenenamento."
        return {"resposta": resposta}
    
   
    else:
        return {
            "resposta": (
                "Olá! Sou o assistente do **REConecta**. "
                "Para que eu possa te indicar a unidade correta sem risco de peregrinação, "
                "me diga qual é o sintoma ou o problema médico (ex: *fui picado por escorpião*, *estou com febre alta*)."
            )
        }
