import datetime
from ftplib import FTP

cme_url_dict = {
    'equity': 'ftp://ftp.cmegroup.com/pub/settle/stleqt',
    'currency': 'ftp://ftp.cmegroup.com/pub/settle/stlcur',
    'commodity': 'ftp://ftp.cmegroup.com/pub/settle/stlags',
    'interest_rate': 'ftp://ftp.cmegroup.com/pub/settle/stlint',
    'comex': 'ftp://ftp.cmegroup.com/settle/stlcomex',
    'nymex': 'ftp://ftp.cmegroup.com/pub/settle/stlnymex',
    'alternative': 'ftp://ftp.cmegroup.com/pub/settle/stlalt',
    'clearport': 'ftp://ftp.cmegroup.com/pub/settle/stlcpc',
}

cme_file_dict = {
    'equity': 'stleqt',
    'currency': 'stlcur',
    'commodity': 'stlags',
    'interest_rate': 'stlint',
    'comex': 'stlcomex',
    'nymex': 'stlnymex',
    'alternative': 'stlalt',
    'clearport': 'stlcpc',
}

today = datetime.datetime.now()
today_str = today.strftime('%Y%m%d')

# for k in cme_url_dict:
#     with open(k + '')

ftp = FTP('ftp.cmegroup.com')
ftp.login()
ftp.cwd('settle')

for k in cme_file_dict:
    with open(k + today_str, 'wb+') as f:
        ftp.retrbinary('RETR %s' % cme_file_dict[k], f.write)
