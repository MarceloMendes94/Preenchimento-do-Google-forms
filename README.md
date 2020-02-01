# Preenchimento-do-Google-forms
``` não dou suporte de instalação em MAC ou windows.```
1. pré-configuração
2. guia de uso
3. Sobre o selenium
4. exemplos de aplicações

## Pré-configuração
No seu browser google chrome clique em opções (três pontinhos)-> ajuda-> sobre o google chrome.

![imagem](img/sobre.png)

Feito o download descompacte e cole o arquivo chromedriver em:<br>
``` /usr/bin/```<br>
faça o dowload para versão do seu browser em:<br>
https://sites.google.com/a/chromium.org/chromedriver/downloads<br>
use o pip,gerenciador de pacotes do python para instaçar o a biblioteca selenium.<br>
```sudo pip3 install selenium``` 
## Guia
Por motivos de generalidade usamos xpath,uma forma de localizar mais genérica, alguns programadores ruins não colocam atributos ID e NAME em todos elementos.<br>

Antes de começar você deve importar a biblioteca e criar uma variável com um browser:<br>
``` 
import tadWeb
browser = tadWeb.open_init("https://www.google.com/")
``` 

Você vai abrir a página e abrir o modo desenvolvedor e selecionar o elemento de que você deseja usar.<br>
![sample](img/modo-desenvolverdor&#32;.png)
<br>
Feito isso clique com o botão direito sobre o código na parte de desenvolvedor, copy-> copy Xpath.<br>
```//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input```<br> 
troque as aspas duplas " por simples '

<br><br>
Caso seja um input de texto use a função:<br>
``` 
tadWeb.escrever(browser,"//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input","Nelson Mandela")
```
<br>

Caso seja um botão use a função:<br>
```
tadWeb.clicar(browser,"//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]")
```
<br>


## Exemplo

1. [login facebook](facebook-login.py)
2. [busca no Google por nelson mandela](busca-google.py)