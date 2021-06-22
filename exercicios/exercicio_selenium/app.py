from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class EdgeAuto:
    def __init__(self):
        self.driver_path = 'msedgedriver'
        self.options = webdriver.EdgeOptions()
        self.options.add_argument('user-data-dir=Perfil')
        self.options.add_argument("--remote-debugging-port=9222")

        self.edge = webdriver.Edge(
            self.driver_path,
            options=self.options
        )

    def clica_signin(self):
        try:
            btn_signin = self.edge.find_element(By.LINK_TEXT, 'Sign in')
            btn_signin.click()
        except Exception as e:
            print(e)

    def faz_login(self, username, password):
        try:
            input_login = self.edge.find_element(By.ID, 'login_field')
            input_password = self.edge.find_element(By.ID, 'password')
            input_login.send_keys(username)
            input_password.send_keys(password)
            btn_signin = self.edge.find_element(By.NAME, 'commit')
            btn_signin.click()

        except Exception as e:
            print('Erro ao fazer login:', e)

    def verifica_usuario(self, usuario_test):
        profile_link = self.edge.find_element(By.CLASS_NAME, 'user-profile-link')
        profile_html = profile_link.get_attribute('innerHTML')
        assert usuario_test in profile_html

    def clica_perfil(self):
        # css selector of perfil button
        s = 'body > div.position-relative.'
        s += 'js-header-wrapper > header > '
        s += 'div.Header-item.position-relative.mr-0.d-none.d-md-flex > details'

        try:
            perfil = self.edge.find_element(By.CSS_SELECTOR, s)
            perfil.click()
        except Exception as e:
            print('Erro ao clicar no perfil', e)

    def faz_logout(self):
        # css selector of sign out in perfil button
        signout_css = 'body > div.position-relative.js-header-wrapper > header > '
        signout_css += 'div.Header-item.position-relative.mr-0.d-none.d-md-flex > '
        signout_css += 'details > details-menu > form > button'
        try:
            btn_signout = self.edge.find_element(By.CSS_SELECTOR, signout_css)
            btn_signout.click()
        except Exception as e:
            print('Erro ao fazer logoff', e)

    def acessa_site(self, site):
        self.edge.get(site)

    def sair(self):
        self.edge.quit()


if __name__ == '__main__':
    edge = EdgeAuto()
    edge.acessa_site('https://github.com/')
    edge.clica_signin()
    edge.faz_login(username='', password='')
    sleep(3)
    edge.clica_perfil()
    # timing sleep for drop down menu be created
    sleep(3)
    edge.verifica_usuario(usuario_test='')
    sleep(3)
    edge.faz_logout()
    sleep(10)
    edge.sair()
