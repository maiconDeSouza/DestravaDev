Claro! Aqui está um modelo de README em português para o seu projeto:

---

# Coletor de Dados Climáticos e Notificador por E-mail

## Descrição

Este projeto foi desenvolvido para coletar dados meteorológicos de um site, processar as informações e enviá-las por e-mail. Os dados meteorológicos incluem a temperatura atual, as condições climáticas e as previsões para os próximos três dias.

## Funcionalidades

- **Coleta de Dados**: Coleta dados meteorológicos de um site especificado usando o Selenium.
- **Processamento de Dados**: Formata os dados coletados em uma mensagem de texto legível.
- **Notificação por E-mail**: Envia os dados meteorológicos processados por e-mail usando SMTP.

## Pré-requisitos

- Python 3.x
- Biblioteca `selenium`
- Biblioteca `webdriver-manager`
- Biblioteca `python-dotenv`
- Acesso a um servidor SMTP para envio de e-mails

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/yourusername/weather-data-emailer.git
   cd weather-data-emailer
   ```

2. **Instale as bibliotecas Python necessárias:**

   ```bash
   pip install selenium webdriver-manager python-dotenv
   ```

3. **Configure as variáveis de ambiente:**

   Crie um arquivo `.env` no diretório raiz do projeto com o seguinte conteúdo:

   ```env
   USER_NAME_EMAIL=seu-email@example.com
   PASSWORD_EMAIL=sua-senha-do-email
   TO_EMAIL=email-do-destinatario@example.com
   ```

## Uso

1. **Atualize os XPaths:**

   Edite o arquivo `app.py` para garantir que os XPaths correspondam aos elementos do site de previsão do tempo que você está raspando.

2. **Execute o script:**

   Execute o script usando:

   ```bash
   python app.py
   ```

   O script coletará os dados meteorológicos, processará as informações e enviará um e-mail com a previsão.

## Explicação do Código

- **`app.py`**: 
  - Gerencia o fluxo principal do aplicativo.
  - Coleta dados meteorológicos usando funções do `functions_for_data_extraction.py`.
  - Formata os dados e os envia por e-mail usando o `send_email.py`.

- **`functions_for_data_extraction.py`**: 
  - Contém funções para navegar no site e extrair dados meteorológicos usando o Selenium.

- **`send_email.py`**: 
  - Gerencia o processo de envio de e-mails usando o protocolo SMTP.
  - Carrega variáveis de ambiente e lida com a autenticação de e-mail.

## Contribuindo

Sinta-se à vontade para fazer um fork do repositório e enviar pull requests. Contribuições e sugestões são bem-vindas.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

---

Substitua os placeholders (`yourusername`, `seu-email@example.com`, `sua-senha-do-email`, `email-do-destinatario@example.com`) com as informações apropriadas. Este README fornece uma visão geral do projeto, instruções de instalação e uso, e informações sobre a estrutura do código.