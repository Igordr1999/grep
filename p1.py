import requests


def get_register(firma_name):
    data = {
        'suchTyp': 'n',
        'registerArt': '',
        'registerNummer': '',
        'registergericht': '',
        'schlagwortOptionen': '2',
        'ergebnisseProSeite': '10',
        'btnSuche': 'Suchen',
        'schlagwoerter': firma_name
    }

    url = 'https://www.handelsregister.de/rp_web/search.do'
    r = requests.post(url, data)

    if r.text.find("Ihre Suche hat 0 Treffer ergeben.") == -1:
        return 0
    else:
        return 1


def get_icann(firma_name):
    url = "http://api.whois.vu"
    data = {
        'q': '{}.com'.format(firma_name)
    }
    r = requests.get(url, data)
    if r.json()['available'] == 'yes':
        return 1
    else:
        return 0


def main():
    f = open('names.txt')
    names = f.readlines()
    names = [line.rstrip() for line in names]

    for firma_name in names:
        register = get_register(firma_name)
        if register is 0:
            continue
        icann = get_icann(firma_name)
        if register and icann:
            print("OK {}".format(firma_name))


if __name__ == '__main__':
    main()
