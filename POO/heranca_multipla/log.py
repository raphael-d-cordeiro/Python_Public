class LogMixing:

    @staticmethod
    def loger(msg):
        with open('logerror.log', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def log_alerta(self, msg):
        self.loger(f'ALERTA - {msg}')

    def log_error(self, msg):
        self.loger(f'ERROR - {msg}')
