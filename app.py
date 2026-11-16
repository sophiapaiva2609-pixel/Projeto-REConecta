import unicodedata
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

UNIDADES = [
    {
        "nome": "UPA do Ibura",
        "horario": "24 horas (todos os dias)",
        "insumos": ["soro antiescorpionico", "soro antiofidico"],
        "especialidades": ["clinica medica", "pediatria"],
    },
    {
        "nome": "Policlínica e Maternidade Professor Barros Lima",
        "horario": "Segunda a sexta, das 07h às 19h",
        "insumos": [],
        "especialidades": ["clinica medica", "pediatria", "ginecologia"],
    },
    {
        "nome": "UPA dos Torrões",
        "horario": "24 horas (todos os dias)",
        "insumos": ["soro antiescorpionico"],
        "especialidades": ["ortopedia", "clinica medica"],
    },
]

AVISO = (
    "📞 Em caso de sintomas graves, ligue para o SAMU (192). "
    "Confirme por telefone a disponibilidade antes de ir. "
    "Este assistente não substitui atendimento médico."
)


class MensagemUsuario(BaseModel):
    mensagem: str


def normalizar(texto: str) -> str:
    texto = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def listar_unidades(insumo: str, nome_soro: str) -> str:
    aptas = [u for u in UNIDADES if insumo in u["insumos"]]
    if not aptas:
        return f"Não encontrei unidade cadastrada com {nome_soro}. Ligue para o SAMU (192)."
    texto = f"Unidades cadastradas com **{nome_soro}**:\n\n"
    for u in aptas:
        texto += f"🏥 **{u['nome']}**\n• Horário: {u['horario']}\n\n"
    return texto


@app.post("/chat")
def responder_chat(dados: MensagemUsuario):
    texto = normalizar(dados.mensagem)

    if "escorpiao" in texto:
        resposta = "⚠️ " + AVISO + "\n\n" + listar_unidades(
            "soro antiescorpionico", "soro antiescorpiônico"
        )
    elif any(p in texto for p in ["cobra", "serpente", "jararaca", "surucucu"]):
        resposta = "⚠️ " + AVISO + "\n\n" + listar_unidades(
            "soro antiofidico", "soro antiofídico"
        )
    elif "picada" in texto or "mordida" in texto:
        resposta = (
            "Qual animal causou a picada ou mordida? (escorpião, cobra, outro)\n\n"
            "Se não souber, vá imediatamente a uma UPA e ligue para o SAMU (192)."
        )
    else:
        resposta = (
            "Olá! Sou o assistente do **REConecta**. No momento, consigo ajudar com "
            "picadas de **escorpião** e de **cobra**. Me conte o que aconteceu "
            "(ex: *fui picado por escorpião*)."
        )
    return {"resposta": resposta}