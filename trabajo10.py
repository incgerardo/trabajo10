import pdb
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

password=input("Ingresa el password: ")
desc_pedido=input("Carga el contenido del sim: ")

driver = webdriver.Chrome()

url="http://manten.grupogamma.com/sim2/login.php"

driver.get(url)

title = driver.title

print(title)
#html_content = driver.page_source

#with open("salida.html", "w", encoding="utf-8") as file:
#    file.write(html_content)



cuadro_usuario=driver.find_element(By.ID,"idoperador")
cuadro_usuario.send_keys("gincide")

cuadro_password=driver.find_element(By.ID,"clave")
cuadro_password.send_keys(password)


boton_enviar=driver.find_element(By.CLASS_NAME,"boton_enviar")
print(boton_enviar.text)
boton_enviar.click()

time.sleep(3)
url_actual=driver.current_url
driver.implicitly_wait(5)  # Esperar hasta 5 segundos por cualquier elemento
driver.get(url_actual)

#print(url_actual)

accion1 = driver.find_element(By.XPATH,"//div[text()='PEDIDOS']")
accion1.click()

accion2 = driver.find_element(By.XPATH,"//div[text()='MANTENIMIENTO']")
accion2.click()

time.sleep(3)

iframe = driver.find_element(By.ID, "content")
driver.switch_to.frame(iframe)

selector_up = Select(driver.find_element(By.ID, "idsector"))
selector_up.select_by_value("91")

# Guardar el manejador (handle) de la ventana principal
ventana_principal = driver.current_window_handle

selector_equipo = driver.find_element(By.ID, "seleq")
selector_equipo.click()

time.sleep(2)

# Obtener todos los manejadores de ventana
handles_ventanas = driver.window_handles

# Cambiar al manejador de la nueva ventana
for ventana in handles_ventanas:
    if ventana != ventana_principal:
        driver.switch_to.window(ventana)
        break

radio_equipo = driver.find_element(By.XPATH,"//input[@type='radio' and @value='1659']")
radio_equipo.click()

driver.switch_to.window(ventana_principal)
driver.switch_to.frame(iframe)

descripcion = driver.find_element(By.ID,"descripcion")
descripcion.send_keys(desc_pedido)

boton_enviar2 = driver.find_element(By.CLASS_NAME,"boton_enviar")
boton_enviar2.click()

pedido_sim = driver.find_element(By.CLASS_NAME,"estado_ok")
print(pedido_sim.text)

pdb.set_trace()

time.sleep(3)

driver.quit()







