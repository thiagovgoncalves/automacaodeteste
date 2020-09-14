from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options

import time

import unittest

chrome_options = Options()
chrome_options.add_argument("--start-maximized") # Iniciar com a janela maximizada

class SignUpTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\Webdrivers\chromedriver.exe', options=chrome_options)
        self.driver.get("https://cliente.americanas.com.br/simple-login/cadastro/pf?next=https%3A%2F%2Fwww.americanas.com.br%2F")

    def test_SignUp(self):
        driver = self.driver

        # Dados que serão inseridos nos campos
        emailteste1          = "teste@hotmail.com"
        emailteste2          = "teste92929292@hotmail.com" # Alterar a cada execução
        senhateste1          = "12"
        senhateste2          = "Teste13579"
        cpfteste1            = "99999999999"
        cpfteste2            = "64976119165" # Alterar a cada execução
        nometeste            = "Teste Dextra"
        datateste            = "06051994"
        telefoneteste        = "42999999999"

        # Definição dos campos
        campoEmailID         = "email-input"
        campoSenhaID         = "password-input"
        campoCPFID           = "cpf-input"
        campoNomeID          = "name-input"
        campoDataNascID      = "birthday-input"
        campoSexo            = "/html/body/div[1]/div/div[2]/form/div[6]/div[1]/label"
        campoTelefoneID      = "phone-input"
        signupButtonXpath    = "/html/body/div[1]/div/div[2]/form/button"

        # Mapeamento dos campos
        campoEmailElement    = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(campoEmailID))
        campoSenhaElement    = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(campoSenhaID))
        campoCPFElement      = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(campoCPFID))
        campoNomeElement     = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(campoNomeID))
        campoDataNascElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(campoDataNascID))
        campoSexoElement     = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(campoSexo))
        campoTelefoneElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(campoTelefoneID))
        signupButtonElement  = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(signupButtonXpath))

        # Funções para enviar os dados e os cliques
        campoEmailElement.send_keys(emailteste1)
        campoSenhaElement.send_keys(senhateste1)
        campoCPFElement.send_keys(cpfteste1)
        campoNomeElement.send_keys(nometeste)
        campoDataNascElement.send_keys(datateste)
        campoSexoElement.click()
        campoTelefoneElement.send_keys(telefoneteste)
        signupButtonElement.click()
        time.sleep(90) # tempo adicionado para resolver o captcha, diminuir/aumentar conforme necessidade

        # Validar a mensagem de e-mail cadastrado
        erro_email = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/div[1]/div").text
        for _ in erro_email:
            print("Erro: e-mail já cadastrado.")
            break

        # O campo e-mail é validado sozinho, sendo necessário limpá-lo
        # e inserir um e-mail válido para testar a validação da senha e do CPF
        campoEmailElement.clear() # Limpar o campo e-mail
        campoEmailElement.send_keys(emailteste2) # Enviar o e-mail correto
        signupButtonElement.click()
        time.sleep(90)  # tempo adicionado para resolver o captcha, diminuir/aumentar conforme necessidade

        # Validar senha fraca
        erro_senha = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/div[2]/div[2]").text
        for _ in erro_senha:
            print("Erro: senha muito fraca.")
            break

        # Validar CPF inválido
        erro_cpf = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/div[3]/div").text
        for _ in erro_cpf:
            print("Erro: CPF inválido.")
            break

        # Limpar os campos "Senha" e "CPF", inserir dados válidos e concluir o cadastro
        campoSenhaElement.clear()
        campoSenhaElement.send_keys(senhateste2)
        campoCPFElement.clear()
        campoCPFElement.send_keys(cpfteste2)
        signupButtonElement.click()
        time.sleep(90) # tempo adicionado para resolver o captcha, diminuir/aumentar conforme necessidade

        # Dados para inserir na busca
        pesquisateste = "moto g8 plus"

        # Definição dos campos da página após Login
        campoPesquisaID      = "h_search-input"
        buttonPesquisaID     = "h_search-btn"
        buttonProdutoXpath   = "/html/body/div[1]/div/div/div/div[3]/div/div[1]/div/div[2]/div[6]/div/div/div/div[1]/div[1]/div/div[2]/a/section/div[2]/div[1]/h2"
        buttonComprarXpath   = "/html/body/div[4]/div/div/div[2]/div/section/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/a/div/span"
        buttonContinuarXpath = "/html/body/div[4]/div/div/main/div[2]/div/div/div[2]/div/div[3]/div/div/div/button/div/span"
        buttonAdicionarXpath = "/html/body/div[4]/section/section/div[1]/div[1]/section/ul/li/div[1]/div[3]/div[1]/span[2]"

        # Mapear os campos para pesquisar o produto
        campoPesquisaElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(campoPesquisaID))
        buttonPesquisaElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(buttonPesquisaID))

        # Inserir os dados e clicar no botão de busca
        campoPesquisaElement.send_keys(pesquisateste)
        buttonPesquisaElement.click()
        time.sleep(5)  # tempo para carregar a página

        # Clicar no produto
        buttonProdutoElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(buttonProdutoXpath))
        buttonProdutoElement.click()
        time.sleep(5)  # tempo para carregar a página

        # Clicar em "Comprar"
        buttonComprarElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(buttonComprarXpath))
        buttonComprarElement.click()
        time.sleep(5)  # tempo para adicionar ao carrinho

        # Clicar em "Continuar" na tela de garantia estendida
        buttonContinuarElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(buttonContinuarXpath))
        buttonContinuarElement.click()
        time.sleep(5)  # tempo para ir à finalização de compra

        # Clicar no botão "+" para adicionar o segundo item à compra
        buttonAdicionarElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(buttonAdicionarXpath))
        buttonAdicionarElement.click()
        time.sleep(10)

        # Validar que o valor total é menor que R$ 5000,00
        # Não há um id para o valor, é uma string dentro de um span,
        # sendo necessário remover alguns caracteres e converter para float
        valortotal  = driver.find_element_by_xpath("/html/body/div[4]/section/section/div[1]/div[1]/section/ul/li/div[1]/div[5]/p").text
        totalcompra = float(valortotal.replace('.', '').replace("R$ ", '').replace(",00", ''))
        if totalcompra < 5000:
            print("O valor da compra é inferior a R$ 5000,00")

        # Validar que a compra pode ser parcelada em até 10x sem juros
        # Observação: como atualmente o número "padrão" de parcelas é 12x, foram feitas 2 validações
        parcelamento = driver.find_element_by_xpath("/html/body/div[4]/section/section/div[2]/div/div[1]/div").text
        parcelas     = int(parcelamento.replace("em até ", '').replace("x sem juros", '').replace('"', ''))
        if parcelas <= 10:
            print("A compra pode ser dividida em até 10x")
        elif parcelas > 10:
            print("A compra pode ser dividida em até", int(parcelas), "x")

        juros = (parcelamento.strip("em até 12 x"))
        if juros == "sem juros":
            print("sem juros")
        elif juros != "sem juros":
            print("com juros")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()