import requests


def enter(login, password):
    session = requests.Session()
    response = session.post(
        'https://avn.kstu.kg/lms/Index.aspx',
        data={
            'ctl00$LoginControl1$LoginTextbox': login,
            'ctl00$LoginControl1$PasswordTextbox': password,
            'ctl00$LoginControl1$ConnectButton': 'Войти'
        }
    )
    return response
