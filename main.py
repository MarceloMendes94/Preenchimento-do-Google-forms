from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
 
# Wait for 5 seconds
#time.sleep(5)
'''
alunos =["MATHEUS CAILLAUX BACELAR ANDRADE","JOSE RODOLFO DE SOUZA FILHO","GABRIEL MONTEIRO FLEGLER","GABRIEL DOS SANTOS CURTO","HARRISON FELIPE SANCHES MACHADO","LETICIA TEIXEIRA DO NASCIMENTO","GUILHERME AMORIM PEREIRA","SIDNEY FARIA LOSS","PATRICK SENNA ROSA","LEANDRO CRUZ DE ANDRADE","LEONARDO CHRYSTIAN RIBEIRO SILVA","LUIZA SONEGHETI COLI","MATHEUS COMERIO REZENDE","LEONARDO LAIA ARPINI","LUCAS SILVA FERREIRA ","DANIEL TAVARES DE BARCELLOS", "RICARDO XAVIER CAMPOS", "GABRIELA PIFFER MARINATO", "EMANUEL MEDEIROS CLAUDINO", "ANA CAROLINA ICHIMURA", "DANIEL HENRIQUE COMERIO","LHORAN GOMES CLAUDIANO","ANDREAS JOSE ALVES HERMES", "NICOLAS PEREIRA SAMPAIO ","CELSO JOSE CALDEIRA JUNIOR","HUDSON NEVES JUNIOR","JULIA MIRANDA ROSSA CAMPOS","RODRIGO RAIDER DE OLIVEIRA","CLARA MAESTRI BRANCO","THIAGO SILVA OLIVEIRA","YURI FERNANDES GONCALVES","MATHEUS DOS SANTOS VASCONCELOS","RENATO PERES DE SOUZA ","DANIEL DA SILVA LIPPAUS", "BERNARDO GOMES DOELINGER", "LORENZO LORENZONI ","RAPHAEL BITTENCOURT DE SOUZA ","THAIS DE SOUZA ","MATHEUS SOARES ","JOSE RICARDO RAMOS", "RAMON MENDES RODRIGUES", "PEDRO HENRIQUE CASSIANO DE ASSIS ","KALLEB RODRIGUES NEVES","TIAGO FELIPE VIVALDI BRAGA ","DANIEL LYRIO CARVALHO ","EMANUEL NORJOSA LUZ ","MATHEUS HENRIQUE GONCALVES COSTA","REBECA ISIDA HIROSSE ","RICARDO ROCHA RIBEIRO","THIAGO CORREA DOS SANTOS" "BRUNO RAFT OLIVEIRA NUNES","NICOLE JOAQUIM LOPES ","CARLOS ALFREDO RAMOS DE CASTRO","VITOR SIQUEIRA DA SILVA","DIEGO DE FREITAS FERNANDES","ADMILSON OLIVEIRA","LUAN LEITE CALDEIRA","FILIPE DOS ANJOS SOUSA" ,"GABRIEL VICTOR FERREIRA DE ARAUJO","CRISTHIAN FONTANA MATTIUZZI","GUSTAVO GOMES DIAS","WILLIAN JAMES SANTOS DE SOUSA","GUILHERME REIS CAPELI VAZ","MICHEL BOLDRIN","VINICIUS ALVES SAIBEL TIM","WILDEMBERG DE JESUS OLIVEIRA","VINICIUS LUCAS DOS REIS","ERIC AUGUSTIN","LUIZ BORGES DE MENDONCA NETO","MATHEUS PENIDO LOUREIRO","CAIO LOPES DE OLIVEIRA"]
cont=50
while(cont>0):
    mat  = str(random.randint(2016, 2019))+"BSI"+str(random.randint(1000, 9999)) 
    tel  = str(random.randint(98800, 99999))+"-"+str(random.randint(1000, 9999)) 
    nome = random.choice(alunos)
    cpf  = str(random.randint(100,999))+str(random.randint(100,999))+str(random.randint(100,999))+str(random.randint(10,99))
    print(cpf +"   "+ nome+"  "+tel+"    "+mat)
    email="zxcxz@gmail.com"
    driver = webdriver.Chrome()
    driver.get("https://forms.gle/YCbgsERFa2gp9wz67")
    elem = driver.find_element_by_name("emailAddress")
    elem.send_keys(email)
    elem = driver.find_element_by_name("entry.1242724763")
    elem.send_keys(nome)
    elem = driver.find_element_by_name("entry.1742243098")
    elem.send_keys(mat)
    elem = driver.find_element_by_name("entry.1884481573")
    elem.send_keys(cpf)
    elem = driver.find_element_by_name("entry.976849792")
    elem.send_keys(tel)
    elem = driver.find_element_by_xpath("//*[@id='mG61Hd']/div/div/div[2]/div[6]/div/div[2]/div/span/div/div[5]/label/div/div[1]/div/div[3]/div").click()
    elem = driver.find_element_by_xpath("//*[@id='mG61Hd']/div/div/div[2]/div[7]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div").click()
    elem = driver.find_element_by_xpath("//*[@id='mG61Hd']/div/div/div[3]/div[1]/div/div/span").click()
    time.sleep(5)
    driver.close()
    
    cont=cont-1


'''

