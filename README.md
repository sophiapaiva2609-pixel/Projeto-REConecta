REConecta

Reconectando caminhos para a saúde

Assistente que ajuda a pessoa a encontrar a unidade de saúde certa, sem peregrinação.

🌱 Origem do projeto

O REConecta nasceu como o projeto de Kickoff do Porto Digital, ao ingressar no programa Embarque Digital. A base conceitual foi um desafio de inovação aberta, inspirado no BOS de Recife, com um propósito central: combater a peregrinação do cidadão em busca de atendimento à saúde pública.

📌 O problema

Em uma emergência, como uma picada de escorpião ou de cobra, nem toda unidade de saúde tem o soro necessário. Quem vai ao posto errado perde um tempo que pode ser decisivo.

💡 A solução

O REConecta é um chatbot que recebe a descrição do problema em linguagem natural e indica as unidades cadastradas que possuem o insumo adequado, com horário de funcionamento e orientações de segurança, como ligar para o SAMU (192).

✨ Funcionalidades
Reconhece picada de escorpião e de cobra e indica a unidade com o soro correto
Funciona com ou sem acentos (escorpião ou escorpiao)
Pergunta qual foi o animal quando a mensagem é vaga (ex.: "fui picado")
Mostra o aviso do SAMU (192) em toda resposta de emergência
Avisa quando nenhuma unidade cadastrada tem o soro
🛠️ Tecnologias
Python 
FastAPI
Pydantic
Uvicorn

🚀 Como rodar
Clone o repositório:
bash
git clone https://github.com/sophiapaiva2609-pixel/Projeto-REConecta.git
cd Projeto-REConecta
Instale as dependências:
bash
pip install fastapi uvicorn
Inicie o servidor:
bash
uvicorn app:app --reload
Abra no navegador a documentação interativa, onde dá para testar o chat:
http://127.0.0.1:8000/docs
🔌 Exemplo de uso

Requisição (POST /chat):

json
{
  "mensagem": "fui picado por escorpião"
}

Resposta:

json
{
  "resposta": "⚠️ ... Unidades cadastradas com soro antiescorpiônico: UPA do Ibura, UPA dos Torrões ..."
}

Exemplo com curl:

bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"mensagem": "fui picado por escorpiao"}'
  
📂 Estrutura do projeto
Projeto-REConecta/
├── app.py                              # API e lógica do chatbot
├── Slide REConecta. Squad 33 (1).pdf   # Apresentação do projeto
└── README.md                           # Documentação
⚠️ Avisos importantes
Os dados das unidades (horários e insumos) estão cadastrados manualmente no código e precisam ser confirmados com a Secretaria de Saúde antes de qualquer uso real.
O REConecta não mostra estoque em tempo real e não substitui atendimento médico.
Em caso de emergência, ligue para o SAMU: 192.
🗺️ Próximos passos
[ ] Integrar dados oficiais de unidades e estoque
[ ] Usar a localização para indicar a unidade mais próxima
[ ] Reconhecer mais sintomas (febre alta, fraturas, etc.)
