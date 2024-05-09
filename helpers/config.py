import configparser


def GetParam(name: str):
    config = configparser.ConfigParser()
    config.read('settings.ini')
    return config.get('Settings', name)
