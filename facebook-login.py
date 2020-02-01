import tadWeb

login = input("por favor informe seu email: ")
senha = input("informe sua senha: ")

browser=tadWeb.open_init("https://www.facebook.com/")
tadWeb.escrever(browser,"//*[@id='email']",login)
tadWeb.escrever(browser,"//*[@id='pass']",senha)
tadWeb.clicar(browser,"//*[@id='u_0_b']")