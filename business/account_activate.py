import requests
import os
import csv
from data.objects import Product
from data.objects import Student

account_url = "http://qa.englishtown.com/services/oboe2/salesforce/test/CreateMemberForE14HZ?v=2"
activate_url = "http://qa.englishtown.com/services/oboe2/salesforce/test/ActivateV2"


def get_default_activation_data():
    return {'startLevel': '0A',
            'levelQty': 16,
            'mainRedemptionQty': 3,
            'freeRedemptionQty': 3,
            'securityverified': 'on',
            'includesenroll': 'on'
            }


def _merge_activation_dict_data(source_dict={}, *kwargs):
    for data in kwargs:
        source_dict.update(data)

    return source_dict


def activate_account():
    r = requests.get(account_url)
    if r.status_code == 200:
        info = r.content.split(',')
        member_id = info[1].split(':')[1].strip()
        data = get_default_activation_data()
        data['memberId'] = member_id
        data['mainRedemptionCode'] = 'S15SCHOOLMAIN'
        data['freeRedemptionCode'] = 'S15SCHOOLF1D'
        data['divisionCode'] = 'SSCNTE2'
        data['productId'] = 63
        result = requests.post(activate_url, data)
        if result.status_code == 200:
            print result.content


def get_file_path(filename):
    filename = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\data\\source\\" + filename

    return filename


def open_csv_file(filename):
    csvfile = open(get_file_path(filename), 'rb')
    reader = csv.reader(csvfile)
    return reader


def get_all_product_info_by_partner(partner='Cool'):
    reader = open_csv_file('ProductList.csv')
    found = []
    for partner_code, productId, productType, mainRedCode, freeRedCode in reader:
        prod = Product()
        prod.detail['productId'] = productId
        prod.detail['mainRedemptionCode'] = mainRedCode
        prod.detail['freeRedemptionCode'] = freeRedCode
        prod.detail['partner'] = partner_code.lower()

        found.append(prod.detail)

    return found


get_all_product_info_by_partner()
