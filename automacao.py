from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests

cotacoes_lista = ['euro', 'dolar']

element = webdriver.Edge(executable_path='msedgedriver.exe') 

element.get("https://www.google.com")
element.set_window_position(-10000,0)
element.find_element_by_id('L2AGLb').send_keys(Keys.ENTER)
element.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotacao euro real')
element.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
print(element.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value'))
element.quit()








