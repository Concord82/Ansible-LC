#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path as Path
import argparse


parser = argparse.ArgumentParser()
# парсинг входных параметров скрипта
parser.add_argument('-f', '--file', required=True,
                    help='file name crt and key without extension')
parser.add_argument('-i', '--host', required=True,
                    help='host name for save var file')
args = parser.parse_args()

# если заданный key файл существует. Читаем его, иначе выход
if Path.isfile(args.file + '.key'):
    with open(args.file + '.key') as key_src:
        key_file = key_src.readlines()
else:
    print('File ' + args.file + '.key not found')
    sys.exit(1)

# если заданный crt файл существует. Читаем его, иначе выход
if Path.isfile(args.file + '.crt'):
    with open(args.file + '.crt') as crt_src:
        crt_file = crt_src.readlines()
else:
    print('File ' + args.file + '.crt not found')
    sys.exit(1)


# Формируем файл переменных для ansible содержащий SSL ключ и сертификат
with open(args.host + '.yml', 'w') as out_file:
    out_file.write('---\n')

    out_file.write('content_ssl_key: |\n')
    for content_line in key_file:
        out_file.write('  ' + content_line)
    out_file.write('\n\n')

    out_file.write('content_ssl_crt: |\n')
    for content_line in crt_file:
        out_file.write('  ' + content_line)
    out_file.write('\n')

print('Ansible var file ' + args.host + '.yml created ')
print('                !!! ATENTION !!!')
print(' Don`t move this file and don`t use git commit command before ')
print('       use ansible-vault command for encript this file. \n')
print('Exаmple:')
print('--------')
print('ansible-vault encrypt ansible_var.yml - and enter password\n')
print('ansible-vault encrypt ansible_var.yml --vault-password-file ../password_file.txt - for use password file')
