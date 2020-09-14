# automacaodeteste
Automação de teste de cadastro utilizando Python e Selenium.

Para executar o teste:

1. Instalar o Python (https://www.python.org/downloads/)
2. Instalar o Selenium (https://selenium-python.readthedocs.io/installation.html)
3. Baixar o ChromeDriver (https://sites.google.com/a/chromium.org/chromedriver/downloads)
4. Criar uma pasta na raiz do disco C: chamada "Webdrivers" e extrair o arquivo ChromeDriver.exe nesta pasta
5. Executar o arquivo TesteDextra.py

Observações: 

A cada execução será necessário alterar o "emailteste2" e o "cpfteste2", pois gera um cadastro e esses dados são únicos.

Ao testar o e-mail inválido será necessário validar um captcha.

Ao testar a senha fraca e o CPF inválido será necessário validar outro captcha

Ao testar o cadastro com os dados corretos será necessário validar um último captcha.

Foram adicionados time.sleep(90) ao final de cada execução que dispara um captcha, para que haja tempo de finalizar.

Testes anteriores feitos com time.sleep(60) mostraram não ser tempo suficiente para alguns captchas.

Caso o captcha seja resolvido em menos de 90 segundos, a página permanece estática até que os 90 segundos terminem e o próximo comando seja executado.
