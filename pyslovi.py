#!/usr/bin/python3
import argparse

map = {
        'А' : 'a',
        'Б' : 'b',
        'В' : 'v',
        'Г' : 'g',
        'Д' : 'd',
        'Ђ' : 'đ',
        'Е' : 'e',
        'Ж' : 'ž',
        'З' : 'z',
        'И' : 'i',
        'Ј' : 'j',
        'К' : 'k',
        'Л' : 'l',
        'Љ' : 'lj',
        'М' : 'm',
        'Н' : 'n',
        'Њ' : 'nj',
        'О' : 'o',
        'П' : 'p',
        'Р' : 'r',
        'С' : 's',
        'Т' : 't',
        'Ћ' : 'ć',
        'У' : 'u',
        'Ф' : 'f',
        'Х' : 'h',
        'Ц' : 'c',
        'Ч' : 'č',
        'Џ' : 'dž',
        'Ш' : 'š',
        'а' : 'a',
        'б' : 'b',
        'в' : 'v',
        'г' : 'g',
        'д' : 'd',
        'ђ' : 'đ',
        'е' : 'e',
        'ж' : 'ž',
        'з' : 'z',
        'и' : 'i',
        'ј' : 'j',
        'к' : 'k',
        'л' : 'l',
        'љ' : 'lj',
        'м' : 'm',
        'н' : 'n',
        'њ' : 'nj',
        'о' : 'o',
        'п' : 'p',
        'р' : 'r',
        'с' : 's',
        'т' : 't',
        'ћ' : 'ć',
        'у' : 'u',
        'ф' : 'f',
        'х' : 'h',
        'ц' : 'c',
        'ч' : 'č',
        'џ' : 'dž',
        'ш' : 'š'
}

def main():
    parser = argparse.ArgumentParser(description='Prebacuje ćirilicu u latinicu.')
    parser.add_argument('-i', dest='input', help='ulazni fajl')
    parser.add_argument('-o', dest='output', help='izlazni fajl')    
    args = parser.parse_args()

    with open(args.output, 'w') as output:
        with open(args.input) as f:
            for line in f:  
                for ch in line: 
                    output.write(convert_char(ch))

def convert_char(c):
    if c in map:
        return map[c]
    else:
        return c

if __name__ == "__main__":
    main()
