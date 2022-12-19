import datetime as dt

class SystemInfo:
    def __init__(self):
        pass
    
    @staticmethod
    def getTime():
        now = dt.datetime.now()
        answer = f'Agora são {now.hour} horas e {now.minute} minutos.'
        return answer