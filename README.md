# Assistente de Voz em Python

Este é um projeto de assistente de voz desenvolvido em Python, utilizando as bibliotecas `SpeechRecognition` para reconhecimento de voz e `Pyttsx3` para síntese de fala. O assistente é capaz de reconhecer comandos de voz e responder verbalmente.

## Estrutura do Projeto

voice_assistant/
├── controller/
│ ├── init.py
│ └── voice_controller.py
├── service/
│ ├── init.py
│ └── voice_service.py
├── repository/
│ ├── init.py
│ └── voice_repository.py
├── main.py
└── requirements.txt


### Descrição das Pastas

- **controller/**: Contém o controlador que coordena a interação entre as camadas de serviço e repositório.
- **service/**: Contém os serviços que processam os comandos e geram respostas.
- **repository/**: Contém o repositório que lida com a interação com o microfone e reconhecimento de voz.
- **main.py**: Ponto de entrada do aplicativo.
- **requirements.txt**: Arquivo de dependências do projeto.

## Pré-requisitos

- Python 3.x
- Pip (gerenciador de pacotes do Python)

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu_usuario/voice_assistant.git
cd voice_assistant
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Uso

Para iniciar o assistente de voz, execute o comando abaixo:

```bash
python main.py
```
## Comandos Disponíveis

- **"horas":** O assistente dirá a hora atual.
- **"nome":** O assistente dirá o seu nome.
- **"sair":** Encerra o assistente de voz.

## Adicionando Novos Comandos

Para adicionar novos comandos, siga os passos abaixo:

1. Adicione uma nova função no serviço (voice_service.py):

```python
def dizer_data(self):
    hoje = datetime.now().strftime("%d/%m/%Y")
    self.falar(f"Hoje é {hoje}")
```

2. Atualize a função executar_comando para incluir o novo comando:

```python
def executar_comando(self, comando):
    if "horas" in comando:
        self.dizer_horas()
    elif "nome" in comando:
        self.dizer_nome()
    elif "data" in comando:
        self.dizer_data()
    else:
        print("Comando não reconhecido.")
```

## Licença

Este projeto está licenciado sob a **MIT License**.

```perl
Adicione este conteúdo ao seu arquivo `README.md` no repositório do projeto. Isso ajudará outros desenvolvedores a entenderem o propósito do projeto, como instalá-lo e usá-lo, além de incentivar contribuições.
```