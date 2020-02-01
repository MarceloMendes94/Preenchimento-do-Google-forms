import tadWeb
browser = tadWeb.open_init("https://www.google.com/")
tadWeb.escrever(browser,"//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input","Nelson Mandela")
tadWeb.clicar(browser,"//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]")