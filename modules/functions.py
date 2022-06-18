import requests


def live(url):
    res = []
    # res = requests.get(url).text.split(';')[0]
    section = requests.get(url).text.split('@')
    dideban = section[2]
    info = section[3]
    mazinfo = info.split(';')
    sherkat = dideban.split(';')[0]
    main_id = sherkat.split(',')[0]
    res.append(sherkat.split(','))

    for maz in mazinfo:
        id = maz.split(',')[0]
        if (id == main_id):
            res.append(maz.split(','))

    return res