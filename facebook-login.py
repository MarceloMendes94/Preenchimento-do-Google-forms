import tadWeb

login = input("por favor informe seu email: ")
senha = input("informe sua senha: ")

browser=tadWeb.open_init("https://www.facebook.com/")
tadWeb.escrever(browser,"//*[@id='email']",login)
tadWeb.escrever(browser,"//*[@id='pass']",senha)
tadWeb.clicar(browser,"/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input")
#usar sempre full path
