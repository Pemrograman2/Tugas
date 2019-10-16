# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:46:37 2019

@author: Dyning Aida Batrishya
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
opsi = Options()
opsi = webdriver.firefox.options.Options()
opsi.headless = False
binary = webdriver.firefox.firefox_binary.FirefoxBinary("C:\Program Files(x86)\Mozilla Firefox\firefox.exe")
cap = webdriver.common.desired_capabilities.DesiredCapabilities().FIREFOX
cap['marionette'] = True
driver = webdriver.Firefox()
driver.get("https://siap.poltekpos.ac.id")
driver.find_element_by_name('user_name').send_keys("1184030")
driver.find_element_by_name('user_pass').send_keys("sariasih54")
driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[2]/table[2]/tbody/tr[1]/td[2]/div/form/input[4]').click()