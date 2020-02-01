from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#abre um página
def open_init(site):
    browser = webdriver.Chrome()
    browser.get(site)
    return browser
    
# escreve em um input da tela
def escrever(browser,xpath,value):
    browser.find_element_by_xpath(xpath).send_keys(value)
    
# clicar em um elemento da tela
def clicar(browser,xpath):
    browser.find_element_by_xpath(xpath).click()    
    
# clicar em um elemento da tela
def close_page(browser):
    browser.close()     
    