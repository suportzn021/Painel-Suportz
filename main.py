#!/usr/bin/env python

#script criada por py suportz
#para fins educacionais/estudos

#bibliotecas
import os
import time
import random
import string
from faker import Faker
from faker.providers import credit_card
import requests
#variaveis globais
fimPrograma = "\33[33mPrograma Finalizado!!\033[m"
#dicionarios de cores para utilizar nos menus e funções
cor = {
    "roxo":"\033[35m",
    "verde":"\033[32m",
    "fecha":"\033[m"
}

#funcao limpar terminal
def limpar(tempo):
    time.sleep(tempo)
    os.system("clear")
    
#Funcoes Redes for Nmap papai
def menu_nmap():
    os.system("clear")
    print("\033[1;31m#---Um script basico com funcoes do nmap---#\033[m")
    print(f"{cor['verde']}━━━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━━━{cor['fecha']}")
    print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}1{cor['fecha']}{cor['verde']}]{cor['fecha']}{cor['roxo']}--> {cor['fecha']}{cor['verde']}Scanear ips na sua rede{cor['fecha']}")
    print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}2{cor['fecha']}{cor['verde']}]{cor['fecha']}{cor['roxo']}--> {cor['fecha']}{cor['verde']}Portas abertas{cor['fecha']}")
    print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}3{cor['fecha']}{cor['verde']}]{cor['fecha']}{cor['roxo']}--> {cor['fecha']}{cor['verde']}Servicos rodando{cor['fecha']}")
    print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}99{cor['fecha']}{cor['verde']}]{cor['fecha']}{cor['roxo']}--> {cor['fecha']}{cor['verde']}Sair{cor['fecha']}")
    print(f"{cor['verde']}━━━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━━━{cor['fecha']}")
    return input(f"{cor['verde']}Digite um numero:{cor['fecha']} {cor['roxo']}")
   
def scaner_rede(ip):
    os.system("clear")
    os.system(f"nmap -sn {ip}")
    print(f"{cor['verde']}Finalizado!!!{cor['fecha']}")
    time.sleep(10)
    
def portas_abertas(ip):
    os.system("clear")
    os.system(f"nmap {ip}")
    time.sleep(10)
    print(f"{cor['verde']}Finalizado!!!{cor['fecha']}")
       
def servicos_on(ip):
    os.system("clear")
    os.system(f"nmap -sV {ip}")
    print(f"{cor['verde']}Finalizado!!!{cor['fecha']}")
    time.sleep(10)

def redes():
    while True:
        comando = menu_nmap()
        if comando != "99":
            if comando == "1":
                ip_endereco = input(f"{cor['verde']}Digite o endereco ip:{cor['fecha']} {cor['roxo']}")       
                scaner_rede(ip_endereco)
            elif comando == "2":
                ip_endereco = input(f"{cor['verde']}Digite o endereco ip:{cor['fecha']} {cor['roxo']}")
                portas_abertas(ip_endereco)
            elif comando == "3":
                ip_endereco = input(f"{cor['verde']}Digite o endereco ip:{cor['fecha']} {cor['roxo']}")
                servicos_on(ip_endereco)
            else:
                print("\033[33mErro! comando invalido\033[m")
                time.sleep(1)
                os.system("clear")
                continue                       
        else:
            break
    
#gerador de pessoas,idada e CPF...
def gerador():    
    limpar(0.500)
    # Configura o Faker para português do Brasil
    fake = Faker('pt_BR')

    # Gera dados aleatórios brasileiros
    nome_completo = fake.name()
    sexo = fake.random_element(elements=('Masculino', 'Feminino'))
    idade = fake.random_int(min=18, max=90)
    cpf = fake.cpf()
    cep = fake.postcode()
    continente = 'América do Sul/Brasil'  # Fixado como América do Sul, já que estamos gerando dados brasileiros
    estado = fake.state()
    cidade = fake.city()
    bairro = fake.bairro()
    email = fake.email()
    senha = fake.password()
    
    # Exibe os dados gerados
    print(f"{cor['verde']}━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━{cor['fecha']}")
    print(f'{cor["roxo"]}Nome Completo: {cor["fecha"]}{cor["verde"]}{nome_completo}{cor["fecha"]}')
    print(f'{cor["roxo"]}Sexo: {cor["fecha"]}{cor["verde"]}{sexo}{cor["fecha"]}')
    print(f'{cor["roxo"]}Idade: {cor["fecha"]}{cor["verde"]}{idade}{cor["fecha"]}')
    print(f'{cor["roxo"]}CPF: {cor["fecha"]}{cor["verde"]}{cpf}{cor["fecha"]}')
    print(f'{cor["roxo"]}CEP: {cor["fecha"]}{cor["verde"]}{cep}{cor["fecha"]}')
    print(f'{cor["roxo"]}Continente: {cor["fecha"]}{cor["verde"]}{continente}{cor["fecha"]}')
    print(f'{cor["roxo"]}Estado: {cor["fecha"]}{cor["verde"]}{estado}{cor["fecha"]}')
    print(f'{cor["roxo"]}Cidade: {cor["fecha"]}{cor["verde"]}{cidade}{cor["fecha"]}')
    print(f'{cor["roxo"]}Bairro: {cor["fecha"]}{cor["verde"]}{bairro}{cor["fecha"]}')
    print(f'{cor["roxo"]}Email: {cor["fecha"]}{cor["verde"]}{email}{cor["fecha"]}')
    print(f'{cor["roxo"]}Senha: {cor["fecha"]}{cor["verde"]}{senha}{cor["fecha"]}')
    
def gerar_pessoa():
    os.system("clear")
    while True:
        print(f"{cor['verde']}━━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}1{cor['fecha']}{cor['verde']}]--> {cor['roxo']}Gerar Pessoa{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}99{cor['fecha']}{cor['verde']}]--> {cor['roxo']}Sair{cor['fecha']}")
        print(f"{cor['verde']}━━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━{cor['fecha']}")
        comando = input(f"{cor['verde']}Digite a opção:{cor['fecha']} {cor['roxo']}")
        if comando == "99":
            break
        elif comando == "1":
            gerador()
        else:
            print("\033[33mComando inválido.\033[m")
            limpar(1)   
#fazer consulta de um ip
def puxar_ip(endereco_ip):
        limpar(0.50)
        resposta = requests.get(f'https://ipinfo.io/{endereco_ip}/json')
        data = resposta.json()
        
        #lista das informações do ip
        print(f"{cor['verde']}━━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━{cor['fecha']}")
        print(f"{cor['roxo']}Endereco ip:{cor['fecha']} {cor['verde']}{data.get('ip')}{cor['fecha']}")
        print(f"{cor['roxo']}Cidade: {cor['fecha']}{cor['verde']}{data.get('city')}{cor['fecha']}")
        print(f"{cor['roxo']}Regiao:{cor['fecha']}{cor['verde']} {data.get('region')}{cor['fecha']}")
        print(f"{cor['roxo']}Continente:{cor['fecha']}{cor['verde']} {data.get('country')}{cor['fecha']}")
        print(f"{cor['roxo']}Localizacao:{cor['fecha']}{cor['verde']} {data.get('loc')}{cor['fecha']}")
        print(f"{cor['roxo']}Status:{cor['fecha']} {cor['verde']}online{cor['fecha']}")
######fazer uma consulta de um ip
def consultar_ip():
    os.system("clear")
    while True:
        print(f"{cor['verde']}━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}1{cor['fecha']}{cor['verde']}]--> {cor['roxo']}Puxar Ip{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}99{cor['fecha']}{cor['verde']}]--> {cor['roxo']}Sair{cor['fecha']}")
        print(f"{cor['verde']}━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━{cor['fecha']}")
        comando = input(f"{cor['verde']}Digite a opção:{cor['fecha']} {cor['roxo']}")
        if comando == "99":
            break
        elif comando == "1":
            ip = input(f"{cor['verde']}Insira o ip:{cor['fecha']} {cor['roxo']}")
            puxar_ip(ip)
        else:
            print("\033[33mComando inválido.\033[m")
            limpar(1)
            
#Função para gerar uma senha aleatória
def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

# Função para gerar um e-mail aleatório
def gerar_email():
    nomes = ["Tareds",'aries','user','usuario', 'admin', 'ano_ni', 'demo', 'exem','maniRob','kingxv',"supraO#","daniR_","Games"]
    dominios = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'hots.com','loves.com',"jumpis.com","Gpeude.gd"]
    nome = random.choice(nomes) + str(random.randint(1000, 9999))
    dominio = random.choice(dominios)
    email = f"{nome}@{dominio}"
    return email

# Função para exibir o menu
def menu_senhasEemail():
    os.system("clear")
    while True:
        print(f"""{cor["verde"]}
 _____                 _ _                            | ____|_ __ ___   __ _(_) |
|  _| | '_ ` _ \ / _` | | |                           | |___| | | | | | (_| | | |
|_____|_| |_| |_|\__,_|_|_|
{cor["fecha"]}""")    
        print(f"{cor['verde']}━━━━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━━━{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}1{cor['fecha']}{cor['verde']}]--> {cor['roxo']}Gerar Email e senha{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}99{cor['fecha']}{cor['verde']}]--> {cor['roxo']}Sair{cor['fecha']}")
        print(f"{cor['verde']}━━━━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━━━{cor['fecha']}")
        escolha = input(f"{cor['verde']}Digite um numero:{cor['fecha']} {cor['roxo']}")
        
        if escolha == '1':
            email = gerar_email()
            senha = gerar_senha()
            limpar(0.200)
            print(f"{cor['verde']}━━━━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━━━{cor['fecha']}")
            print(f"{cor['roxo']}E-mail gerado:{cor['fecha']} {cor['verde']}{email}{cor['fecha']}")
            print(f"{cor['roxo']}Senha gerada:{cor['fecha']} {cor['verde']}{senha}{cor['fecha']}")
            print(f"{cor['verde']}━━━━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━━━{cor['fecha']}")
        elif escolha == '99':
            break
        else:
            print("\033[33mOpção inválida, tente novamente.\033[m")
            limpar(1)

def consultar_num(ddd,numero):
    url = f"https://brasilapi.com.br/api/ddd/v1/{ddd}"
    response = requests.get(url)
    ##############################
    API_KEY = '0yodSwrgWuXP7zFprcaKe2pAhgO8h14b'
    url_validar = f"https://api.apilayer.com/number_verification/validate?number={numero}"
    headers = {'apikey': API_KEY}
    response_validar = requests.get(url_validar, headers=headers)

    
    if response.status_code == 200:
        data_ddd = response.json()
        data = response_validar.json()
        if data['valid']:
            print(f"{cor['verde']}#####━━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━#####{cor['fecha']}")
            print(f"{cor['roxo']}Valido:{cor['fecha']} {cor['verde']}{data['valid']}{cor['fecha']}")
            print(f"{cor['roxo']}Numero válido:{cor['fecha']} {cor['verde']}{numero}{cor['fecha']}")
            print(f"{cor['roxo']}Local formatado:{cor['fecha']} {cor['verde']}{data['local_format']}{cor['fecha']}")
            print(f"{cor['roxo']}Pais:{cor['fecha']} {cor['verde']}{data['country_name']}{cor['fecha']}")
            print(f"{cor['roxo']}Cod País:{cor['fecha']} {cor['verde']}{data['country_code']}{cor['fecha']}")
            print(f"{cor['roxo']}Prefixo:{cor['fecha']} {cor['verde']}{data['country_prefix']}{cor['fecha']}")
            print(f"{cor['roxo']}Operadora:{cor['fecha']} {cor['verde']}{data['carrier']}{cor['fecha']}")
            print(f"{cor['roxo']}Tipo de numero:{cor['fecha']} {cor['verde']}{data['line_type']}{cor['fecha']}")
            print(f"{cor['roxo']}Localizacao:{cor['fecha']} {cor['verde']}{data['location']}{cor['fecha']}")
            estado = data_ddd['state']
            cidade = data_ddd['cities']
            print(f"{cor['roxo']}DDD {ddd} corresponde ao estado:{cor['fecha']} {cor['verde']}{estado}{cor['fecha']}")
            print(f"{cor['roxo']}Cidades:{cor['fecha']} {cor['verde']}{cidade}{cor['fecha']}")
        else:
            print(f"\033[33mErro Numero n encontrado!\033[m")
    else:
        print(f"\033[33mErro no servico!\033[m")
        
def puxar_tel():
    while True:
        ddd = input(f"{cor['roxo']}Informe o DDD:{cor['fecha']} {cor['verde']}")
        numero = input(f"{cor['roxo']}Informe o Telefone:{cor['fecha']} {cor['verde']} ")
        consultar_num(ddd,numero)
        print(f"{cor['verde']}━━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}1{cor['verde']}]--> {cor['roxo']}Repetir{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}99{cor['verde']}]--> {cor['roxo']}Sair{cor['fecha']}")
        print(f"{cor['verde']}━━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━{cor['fecha']}")           
        res = input("Escolha uma opcao: ")
        if res == "1":
            os.system("clear")
            continue
        else:
            print(fimPrograma)
            break
            
def calculadora():
    num1 = float(input(f"{cor['roxo']}Primeiro Numero:{cor['fecha']} {cor['verde']}"))
    soma = input(f"{cor['roxo']}Operador +,-,÷,×:{cor['fecha']} {cor['verde']}")
    num2 = float(input(f"{cor['roxo']}Segundo Numero:{cor['fecha']} {cor['verde']}"))
    if soma == "+":
        print(f'{cor["roxo"]}o resultado é = {cor["fecha"]}{cor["verde"]}{num1+num2}{cor["fecha"]}')
    elif soma == "-":
         print(f'{cor["roxo"]}o resultado é = {cor["fecha"]}{cor["verde"]}{num1-num2}{cor["fecha"]}')
    elif soma == "×":
         print(f'{cor["roxo"]}o resultado é = {cor["fecha"]}{cor["verde"]}{num1*num2}{cor["fecha"]}')
    elif soma == "÷":
        if num1 > 0 and num2 > 0:            
            print(f'{cor["roxo"]}o resultado é = {cor["fecha"]}{cor["verde"]}{num1/num2}{cor["fecha"]}')
        else:
            print(f"\033[33mErro!! numeros n podem ser dividido por zero!!\033[m")
    else:
        print(f"\033[1;31mOperador Inválido!!!\033[m")
    time.sleep(3)
    

#funcao para baixar arquivo e adicionar no arquivo  Download  
def baixar():
    print(f"\033[33mFuncao baixar arquivos\033[m")
    URL = input(f"{cor['roxo']}Coloque a URL -->{cor['fecha']} {cor['verde']}")
    dir = "/sdcard/Download/"
    os.system(f"wget {URL} -P {dir}")#baixo e informa o diretório 
    print(f"{cor['verde']}Finalizado!! Arquivo esta em {dir}{cor['fecha']}")
    limpar(3)

def raiz():
    num = int(input(f"{cor['roxo']}digite um numero:{cor['fecha']} {cor['verde']}"))
    print(num*num)
    time.sleep(3)
    
def raio_circulo():
    pi = 3.14
    raio = float(input(f"{cor['roxo']}numero do raio:{cor['fecha']} {cor['verde']} "))
    print("Area = ",pi*raio**2)
    time.sleep(3)
 
def imc():
    peso = float(input(f"{cor['roxo']}qual seu peso?{cor['fecha']} {cor['verde']}"))
    altura = float(input(f"{cor['roxo']}qual sua altura?{cor['fecha']} {cor['verde']}"))
    calculo = peso / (altura**2)
    if calculo < 18.5:
        print(f"{cor['verde']}Vc esta abaixo do peso{cor['fecha']}")
    elif calculo > 18.5 and calculo < 24.9:
        print(f"{cor['verde']}Peso saudavel{cor['verde']}")
    elif calculo > 25.0 and calculo < 30.0:
        print(f"\033[33mSobrepeso\033[m")
    else:
        print(f"\033[33mObeso nivel hard\033[m")
    time.sleep(3)
    
def outros():
    while True:
        os.system("clear")
        print(f"{cor['verde']}━━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}1{cor['fecha']}{cor['verde']}]{cor['roxo']}-->{cor['fecha']} {cor['verde']}Baixar arquivo{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}2{cor['fecha']}{cor['verde']}]{cor['roxo']}-->{cor['fecha']} {cor['verde']}Raiz quadrada{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}3{cor['fecha']}{cor['verde']}]{cor['roxo']}-->{cor['fecha']} {cor['verde']}Raio circulo{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}4{cor['fecha']}{cor['verde']}]{cor['roxo']}-->{cor['fecha']} {cor['verde']}Mat basica{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}5{cor['fecha']}{cor['verde']}]{cor['roxo']}-->{cor['fecha']} {cor['verde']}IMC{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}99{cor['fecha']}{cor['verde']}]{cor['roxo']}-->{cor['fecha']} {cor['verde']}sair{cor['fecha']}")
        print(f"{cor['verde']}━━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━{cor['fecha']}")
        cmd = input(f"{cor['roxo']}Digite:{cor['fecha']} {cor['verde']}")
        if cmd == "99":
            print(f"{cor['verde']}programa finalizado!!!{cor['fecha']}")
            break
        elif cmd == "1":
            baixar()
        elif cmd == "2":
            raiz()
        elif cmd == "3":
            raio_circulo()
        elif cmd == "4":
            calculadora()
        elif cmd == "5":
            imc()
        else:
            print(f"\033[33mComando não reconhecido, tente novamente.\033[m")
            time.sleep(1)
def mostra_cc():
    os.system("clear")
    fake = Faker()
    fake.add_provider(credit_card)

    # Gerar um número de cartão de crédito falso
    numero_cartao = fake.credit_card_number()
    # Gerar uma data de validade falsa
    data_validade = fake.credit_card_expire()
    # Gerar um código de segurança falso (CVV)
    cvv = fake.credit_card_security_code()
    print(f"{cor['verde']}━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━{cor['fecha']}")
    print(f"{cor['roxo']}Numero do Cartão:{cor['verde']} {numero_cartao}{cor['fecha']}")
    print(f"{cor['roxo']}Data de Validade:{cor['fecha']} {cor['verde']}{data_validade}{cor['fecha']}")
    print(f"{cor['roxo']}CVV:{cor['fecha']} {cor['verde']}{cvv}{cor['fecha']}")
    
def gerar_cc():
    os.system("clear")
    while True:
        print(f"""{cor["verde"]}
  ____ ____
 / ___/ ___|
| |  | |
| |__| |___
 \____\____|
{cor["fecha"]}""") 
        print(f"{cor['verde']}━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}1{cor['fecha']}{cor['verde']}]--> {cor['roxo']}Gerar CC{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}99{cor['fecha']}{cor['verde']}]--> {cor['roxo']}Sair{cor['fecha']}")
        print(f"{cor['verde']}━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━{cor['fecha']}")
        comando = input(f"{cor['verde']}Digite a opção:{cor['fecha']} {cor['roxo']}")
        if comando == "99":
            break
        elif comando == "1":
            mostra_cc()
        else:
            print("\033[33mComando inválido.\033[m")
            time.sleep(1)
            os.system("clear")

#Funcao consultar/puxar cep
def puxar_cep(cep):
    try:
        os.system("clear")
        url_cep = requests.get(f"https://cep.awesomeapi.com.br/{cep}")
        url_cep.raise_for_status()
        data_cep = url_cep.json()
        print(f"{cor['verde']}━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━{cor['fecha']}")
        print(f"{cor['roxo']}Status:{cor['fecha']} {cor['verde']}Online{cor['fecha']}")
        print(f"{cor['roxo']}Cep:{cor['fecha']} {cor['verde']}{data_cep['cep']}{cor['fecha']}")
        print(f"{cor['roxo']}DDD:{cor['fecha']} {cor['verde']}{data_cep['ddd']}{cor['fecha']}")
        print(f"{cor['roxo']}Enderoco tipo:{cor['fecha']} {cor['verde']}{data_cep['address_type']}{cor['fecha']}")
        print(f"{cor['roxo']}Endereco:{cor['fecha']} {cor['verde']}{data_cep['address']}{cor['fecha']}")
        print(f"{cor['roxo']}Estado:{cor['fecha']} {cor['verde']}{data_cep['state']}{cor['fecha']}")
        print(f"{cor['roxo']}Cidade:{cor['fecha']} {cor['verde']}{data_cep['city']}{cor['fecha']}")
        print(f"{cor['roxo']}Distrito:{cor['fecha']} {cor['verde']}{data_cep['district']}{cor['fecha']}")
    except requests.exceptions.RequestException as e:
        print(f"\033[33mErro ao buscar o CEP: {cep}\033[m")
    except KeyError:
        print("\033[33mCEP não encontrado ou resposta inválida.\033[m")

def consultar_cep():
    os.system("clear")
    while True:    
        print(f"{cor['verde']}━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}1{cor['fecha']}{cor['verde']}]--> {cor['roxo']}Puxar cep{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}99{cor['fecha']}{cor['verde']}]--> {cor['roxo']}Sair{cor['fecha']}")
        print(f"{cor['verde']}━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━{cor['fecha']}")
        comando = input(f"{cor['verde']}Digite a opção:{cor['fecha']} {cor['roxo']}")
        if comando == "99":
            break
        elif comando == "1":
            cep = input(f"{cor['verde']}Insira o CEP:{cor['fecha']} {cor['roxo']}")
            puxar_cep(cep)
        else:
            print("\033[33mComando inválido.\033[m")
            limpar(1)
#puxa cnpjtinha
def puxar_cnpj(cnpj):
    os.system("clear")
    try:
        url_cnpj = requests.get(f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}")
        url_cnpj.raise_for_status()
        data_cnpj = url_cnpj.json()     
        print(f"{cor['verde']}━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━{cor['fecha']}")
        print(f"{cor['roxo']}Status:{cor['fecha']} {cor['verde']}online{cor['fecha']}")
        print(f"{cor['roxo']}UF:{cor['fecha']} {cor['verde']}{data_cnpj['uf']}{cor['fecha']}")
        print(f"{cor['roxo']}CEP:{cor['fecha']} {cor['verde']}{data_cnpj['cep']}{cor['fecha']}")
        print(f"{cor['roxo']}CNPJ:{cor['fecha']} {cor['verde']}{data_cnpj['cnpj']}{cor['fecha']}")
        print(f"{cor['roxo']}País:{cor['fecha']} {cor['verde']}{data_cnpj['pais']}{cor['fecha']}")
        print(f"{cor['roxo']}Email:{cor['fecha']} {cor['verde']}{data_cnpj['email']}{cor['fecha']}")
        print(f"{cor['roxo']}Porte:{cor['fecha']} {cor['verde']}{data_cnpj['porte']}{cor['fecha']}")
        print(f"{cor['roxo']}Bairro:{cor['fecha']} {cor['verde']}{data_cnpj['bairro']}{cor['fecha']}")
        print(f"{cor['roxo']}Número:{cor['fecha']} {cor['verde']}{data_cnpj['numero']}{cor['fecha']}")
        print(f"{cor['roxo']}DDD Fax:{cor['fecha']} {cor['verde']}{data_cnpj['ddd_fax']}{cor['fecha']}")
        print(f"{cor['roxo']}Município:{cor['fecha']} {cor['verde']}{data_cnpj['municipio']}{cor['fecha']}")
        print(f"{cor['roxo']}Logradouro:{cor['fecha']} {cor['verde']}{data_cnpj['logradouro']}{cor['fecha']}")
        print(f"{cor['roxo']}CNAE Fiscal:{cor['fecha']} {cor['verde']}{data_cnpj['cnae_fiscal']}{cor['fecha']}")
        print(f"{cor['roxo']}Complemento:{cor['fecha']} {cor['verde']}{data_cnpj['complemento']}{cor['fecha']}")
        print(f"{cor['roxo']}Razão Social:{cor['fecha']} {cor['verde']}{data_cnpj['razao_social']}{cor['fecha']}")
        print(f"{cor['roxo']}Nome Fantasia:{cor['fecha']} {cor['verde']}{data_cnpj['nome_fantasia']}{cor['fecha']}")
        print(f"{cor['roxo']}Capital Social:{cor['fecha']} {cor['verde']}{data_cnpj['capital_social']}{cor['fecha']}")
        print(f"{cor['roxo']}DDD Telefone 1:{cor['fecha']} {cor['verde']}{data_cnpj['ddd_telefone_1']}{cor['fecha']}")
        print(f"{cor['roxo']}DDD Telefone 2:{cor['fecha']} {cor['verde']}{data_cnpj['ddd_telefone_2']}{cor['fecha']}")
        print(f"{cor['roxo']}Natureza Jurídica:{cor['fecha']} {cor['verde']}{data_cnpj['natureza_juridica']}{cor['fecha']}")
        print(f"{cor['roxo']}Situação Especial:{cor['fecha']} {cor['verde']}{data_cnpj['situacao_especial']}{cor['fecha']}")
        print(f"{cor['roxo']}Situação Cadastral:{cor['fecha']} {cor['verde']}{data_cnpj['situacao_cadastral']}{cor['fecha']}")
        print(f"{cor['roxo']}Data Situação Cadastral:{cor['fecha']} {cor['verde']}{data_cnpj['data_situacao_cadastral']}{cor['fecha']}")
        print(f"{cor['roxo']}CNAE Fiscal Descrição:{cor['fecha']} {cor['verde']}{data_cnpj['cnae_fiscal_descricao']}{cor['fecha']}")
        print(f"{cor['roxo']}Data Início Atividade:{cor['fecha']} {cor['verde']}{data_cnpj['data_inicio_atividade']}{cor['fecha']}")
        print(f"{cor['roxo']}Motivo Situação Cadastral:{cor['fecha']} {cor['verde']}{data_cnpj['motivo_situacao_cadastral']}{cor['fecha']}")
        print(f"{cor['roxo']}Descrição Situação Cadastral:{cor['fecha']} {cor['verde']}{data_cnpj['descricao_situacao_cadastral']}{cor['fecha']}")
        print(f"{cor['roxo']}Tipo de Logradouro:{cor['fecha']} {cor['verde']}{data_cnpj['descricao_tipo_de_logradouro']}{cor['fecha']}")
        print(f"{cor['roxo']}Descrição Motivo Situação Cadastral:{cor['fecha']} {cor['verde']}{data_cnpj['descricao_motivo_situacao_cadastral']}{cor['fecha']}")
        print(f"{cor['roxo']}Identificador Matriz/Filial:{cor['fecha']} {cor['verde']}{data_cnpj['descricao_identificador_matriz_filial']}{cor['fecha']}")
    except requests.exceptions.RequestException as e:
        print(f"\033[33mErro ao buscar o CNPJ: {cnpj}\033[m")
    except KeyError:
        print(f"\033[33mCNPJ não encontrado ou resposta inválida.\033[m")
            
#consultar cnpj aianananna
def consultar_cnpj():
    os.system("clear")
    while True:        
        print(f"{cor['verde']}━━━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━━━{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}1{cor['fecha']}{cor['verde']}]--> {cor['roxo']}Puxar CNPJ{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}99{cor['fecha']}{cor['verde']}]--> {cor['roxo']}Sair{cor['fecha']}")
        print(f"{cor['verde']}━━━━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━━━{cor['fecha']}")
        comando = input(f"{cor['verde']}Digite a opção:{cor['fecha']} {cor['roxo']}")
        if comando == "99":
            break
        elif comando == "1":
            cnpj = input(f"{cor['verde']}Insira o CNPJ:{cor['fecha']} {cor['roxo']}")
            puxar_cnpj(cnpj)
        else:
            print("\033[33mComando invalido.\033[m")
            limar(1)
#menu do criado
def sobre_painel():
    os.system("clear")
    print(f"{cor['verde']}━━━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━━━{cor['fecha']}")
    print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}+{cor['fecha']}{cor['verde']}]-{cor['roxo']}Criador:{cor['fecha']} {cor['verde']}Suportz")
    print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}+{cor['fecha']}{cor['verde']}]-{cor['roxo']}Versao:{cor['fecha']} {cor['verde']}1.0.0")
    print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}+{cor['fecha']}{cor['verde']}]-{cor['roxo']}Data:{cor['fecha']} {cor['verde']}2/06/2024")
    print(f"{cor['verde']}━━━━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━━━{cor['fecha']}")
    
def menu_info():
    os.system("clear")
    while True:        
        print(f"{cor['verde']}━━━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━━━{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}1{cor['fecha']}{cor['verde']}]--> {cor['roxo']}Contato{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}2{cor['fecha']}{cor['verde']}]--> {cor['roxo']}Sobre{cor['fecha']}")
        print(f"{cor['verde']}[{cor['fecha']}{cor['roxo']}99{cor['fecha']}{cor['verde']}]--> {cor['roxo']}Sair{cor['fecha']}")
        print(f"{cor['verde']}━━━━━━━━━━━━━━❮{cor['fecha']}{cor['roxo']}◆{cor['fecha']}{cor['verde']}❯━━━━━━━━━━━━━{cor['fecha']}")
        comando = input(f"{cor['verde']}Digite a opção:{cor['fecha']} {cor['roxo']}")
        if comando == "99":
            break
        elif comando == "1":
            os.system("termux-open https://t.me/Suportzn021")
            os.system("clear")
        elif comando == "2":
            sobre_painel()
        else:
            print("\033[33mComando invalido.\033[m")
            time.sleep(1)
            os.system("clear")
           
#funcao menu principal
def menu():
    limpar(0.100)
    print(f"""{cor["verde"]}
 ____                         _
/ ___| _   _ _ __   ___  _ __| |_ ____
\___ \| | | | '_ \ / _ \| '__| __|_  /
 ___) | |_| | |_) | (_) | |  | |_ / /
|____/ \__,_| .__/ \___/|_|   \__/___|
            |_|
{cor["fecha"]}""")
    print(f'{cor["roxo"]}DO CODIGO PARA O MUNDO{cor["fecha"]}')
    print(f'{cor["verde"]}┏━┅┅┄┄⟞⟦{cor["fecha"]}{cor["roxo"]}Suportz{cor["fecha"]}{cor["verde"]}⟧⟝┄┄┉┉━┓ {cor["fecha"]}')
    print(f'{cor["verde"]}|⟦{cor["fecha"]}{cor["roxo"]}1{cor["fecha"]}{cor["verde"]}⟧{cor["fecha"]}{cor["roxo"]}-> {cor["fecha"]}{cor["verde"]}Basico{cor["fecha"]}')
    print(f'{cor["verde"]}|⟦{cor["fecha"]}{cor["roxo"]}2{cor["fecha"]}{cor["verde"]}⟧{cor["fecha"]}{cor["roxo"]}-> {cor["fecha"]}{cor["verde"]}Redes{cor["fecha"]}')
    print(f'{cor["verde"]}|⟦{cor["fecha"]}{cor["roxo"]}3{cor["fecha"]}{cor["verde"]}⟧{cor["fecha"]}{cor["roxo"]}-> {cor["fecha"]}{cor["verde"]}Gerador CC{cor["fecha"]}')
    print(f'{cor["verde"]}|⟦{cor["fecha"]}{cor["roxo"]}4{cor["fecha"]}{cor["verde"]}⟧{cor["fecha"]}{cor["roxo"]}-> {cor["fecha"]}{cor["verde"]}Gerador de Pessoas{cor["fecha"]}')
    print(f'{cor["verde"]}|⟦{cor["fecha"]}{cor["roxo"]}5{cor["fecha"]}{cor["verde"]}⟧{cor["fecha"]}{cor["roxo"]}-> {cor["fecha"]}{cor["verde"]}Gerador de Contas{cor["fecha"]}')
    print(f'{cor["verde"]}|⟦{cor["fecha"]}{cor["roxo"]}6{cor["fecha"]}{cor["verde"]}⟧{cor["fecha"]}{cor["roxo"]}-> {cor["fecha"]}{cor["verde"]}Consultar Ip{cor["fecha"]}')
    print(f'{cor["verde"]}|⟦{cor["fecha"]}{cor["roxo"]}7{cor["fecha"]}{cor["verde"]}⟧{cor["fecha"]}{cor["roxo"]}-> {cor["fecha"]}{cor["verde"]}Consultar Tel{cor["fecha"]}')
    print(f'{cor["verde"]}|⟦{cor["fecha"]}{cor["roxo"]}8{cor["fecha"]}{cor["verde"]}⟧{cor["fecha"]}{cor["roxo"]}-> {cor["fecha"]}{cor["verde"]}Consultar Cep{cor["fecha"]}')
    print(f'{cor["verde"]}|⟦{cor["fecha"]}{cor["roxo"]}9{cor["fecha"]}{cor["verde"]}⟧{cor["fecha"]}{cor["roxo"]}-> {cor["fecha"]}{cor["verde"]}Consultar CNPJ{cor["fecha"]}')
    print(f'{cor["verde"]}|⟦{cor["fecha"]}{cor["roxo"]}10{cor["fecha"]}{cor["verde"]}⟧{cor["fecha"]}{cor["roxo"]}-> {cor["fecha"]}{cor["verde"]}Info{cor["fecha"]}')
    print(f'{cor["verde"]}|⟦{cor["fecha"]}{cor["roxo"]}99{cor["fecha"]}{cor["verde"]}⟧{cor["fecha"]}{cor["roxo"]}-> {cor["fecha"]}{cor["verde"]}Exit{cor["fecha"]}')
    print(f'{cor["verde"]}┗━┅┅┄┄⟞⟦{cor["fecha"]}{cor["roxo"]}Suportz{cor["fecha"]}{cor["verde"]}⟧⟝┄┄┉┉━┛ {cor["fecha"]}')
    return input(f'{cor["verde"]}--> {cor["fecha"]}{cor["roxo"]}')
                
#loop dos menus e funções
while True:
    cmd = menu()
    if cmd == "1":
        outros()
    elif cmd == "2":
        redes()
    elif cmd == "3":
        gerar_cc()
    elif cmd == "4":
        gerar_pessoa()
    elif cmd == "5":
        menu_senhasEemail()
    elif cmd == "6":
        consultar_ip()
    elif cmd == "7":
        puxar_tel()
    elif cmd == "8":
        consultar_cep()
    elif cmd == "9":
        consultar_cnpj()
    elif cmd == "10":
        menu_info()
    elif cmd == "99":
        exit()
    else:
        print("\033[1;31mNúmero não existente!!!\033[m")
        time.sleep(0.800)
        continue
   
