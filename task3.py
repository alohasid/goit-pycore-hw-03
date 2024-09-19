import re

PHONE_CODE_NUMBER_BY_DEFAULT = '+38' # Can be changed to any country code
PHONE_CODE_NUMBER_BY_DEFAULT_WITHOUT_PLUS = '38'

def normalize_phone(phone_number: str) -> str:
    cleaned_phone_number = re.sub(r'[^\d+]', '', phone_number)
    
    if cleaned_phone_number.startswith('+'):
        if cleaned_phone_number.startswith(PHONE_CODE_NUMBER_BY_DEFAULT):
            print('if 1')
            return cleaned_phone_number
        else:
            print('else 1')
            return PHONE_CODE_NUMBER_BY_DEFAULT + cleaned_phone_number[1:]
    elif cleaned_phone_number.startswith(PHONE_CODE_NUMBER_BY_DEFAULT_WITHOUT_PLUS):
        return PHONE_CODE_NUMBER_BY_DEFAULT + cleaned_phone_number[2:]
    else:
        print('else 2')
        return PHONE_CODE_NUMBER_BY_DEFAULT + cleaned_phone_number


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)



