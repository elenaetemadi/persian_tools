from persian_tools.bank import card_number


def card_info(card):
    if card_number.validate(card):
        return (card_number.bank_data(card))
    else:
        print('INVALID...')


print(card_info('6037701689095443'))
print(card_info('6219861034529007'))
print(card_info('6219861034529008'))

print('.' * 50)

from persian_tools import phone_number


def phone_info(phone):
    if phone_number.validate(phone):
        return (phone_number.operator_data(phone))
    else:
        print('INVALID...')


print(phone_info('09107242144'))
print(phone_info('09303456789'))
print(phone_info('98912345678'))

print('.' * 50)

from persian_tools import national_id


def national_info(id):
    if national_id.validate(id):
        return (national_id.find_place(id))
    else:
        print('INVALID...')


print(national_info('0643005846'))
print(national_info('4215678900'))

print('.' * 50)

from persian_tools import plate


def plate_info(pelak):
    if plate.is_valid(pelak):
        return (plate.get_info(pelak))
    else:
        print('INVALID...')


print(plate_info('12D45147'))
print(plate_info('1204567'))

print('.' * 50)

