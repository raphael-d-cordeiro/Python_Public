from eletronico import Eletronico
from log import LogMixing


class SmartPhone(Eletronico, LogMixing):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectar = False

    def inicia_conexao(self):
        if not self._ligado:
            _msg = f'{self._nome} ESTÁ DESLIGADO'
            print(_msg)
            self.log_error(_msg)
            return

        if self._conectar:
            _msg = f'{self._nome} SMARTPHONE JÁ CONECTADO!'
            print(_msg)
            self.log_error(_msg)
            return
        self._conectar = True
        _msg = f'{self._nome} Conexão realizada com sucesso!'
        print(_msg)
        self.log_alerta(_msg)

    def finaliza_conexao(self):
        if not self._conectar:
            _msg = f'{self._nome} SMARTPHONE JÁ DESCONECTADO'
            print(_msg)
            self.log_error(_msg)
            return
        self._conectar = False
        _msg = f'{self._nome} Desconexão realizada com sucesso!'
        print(_msg)
        self.log_alerta(_msg)
