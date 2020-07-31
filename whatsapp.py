'''
You need to install selenium by using command 'pip install selenium'
'''
from selenium import webdriver
from time import sleep
'''
download driver and place driver.exe in same folder where this .py is present
'''
driver = webdriver.Chrome('python learning\chromedriver.exe')
driver.get('https://web.whatsapp.com/')
'''
Enter your Full contact name as writen make sure it is same 
'''
name=['name1','name2','etc']
#Wait until whatsapp web screen appear and your whatsapp show then press any key
input('Press Any key if you have scan your Whatsapp Br code')
for item in name:
    #Change Class name value if giving error and select according to your system
    msg = item
    search_box = driver.find_element_by_class_name('_3FRCZ')
    search_box.send_keys(item)
    sleep(2)
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(item))
    user.click()
    msg_box = driver.find_element_by_class_name('_3uMse')
    sleep(2) 
    msg_box.send_keys(msg)
    sleep(3)
    button = driver.find_element_by_class_name('_1U1xa')
    button.click()
    
print("Sending Succeefully")
