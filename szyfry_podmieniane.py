from typing import Dict, Union

gadery_map = {
    'G': 'A',
    'D': 'E',
    'R': 'Y',
    'P': 'O',
    'L': 'U',
    'K': 'I',
    'A': 'G',
    'E': 'D',
    'Y': 'R',
    'O': 'P',
    'U': 'L',
    'I': 'K'
}

polityka_map = {
    'P': 'O',
    'L': 'I',
    'T': 'Y',
    'K': 'A',
    'R': 'E',
    'N': 'U',
    'O': 'P',
    'I': 'L',
    'Y': 'T',
    'A': 'K',
    'E': 'R',
    'U': 'N',
}


def encode(string: str, cipher: Dict) -> str:
    return ''.join(list(map(lambda x: cipher.get(x.upper(), x.upper()), string)))


def create_cipher_map(string: str) -> Union[Dict, None]:
    cipher = dict(
        list(zip(string[::2], string[1::2])) + list(zip(string[1::2], string[::2]))
    )
    if sorted(list(set(cipher.values()))) != sorted(list(cipher.values())):
        print('Your cipher is not unambiguous')
    elif not cipher.values():
        print('Your cipher has to have at least 2 characters')
    else:
        return cipher


if __name__ == '__main__':
    cipher = False
    while not cipher:
        cipher_choice = input('Choose what cipher to use: (G)ADERY POLUKI, (P)OLITYKA RENU or (C)ustom: ')

        if cipher_choice == 'G':
            cipher = gadery_map
        elif cipher_choice == 'P':
            cipher = polityka_map
        elif cipher_choice == 'C':
            custom_cipher_input = input('Write your custom cipher: ')
            cipher = create_cipher_map(custom_cipher_input)
        else:
            print('Wrong input, try choosing again.')

    string = input('Write what you want to encode: ')
    string_encoded = szyfruj(string, cipher)
    print(string_encoded)
