####################################################
# -*- coding:utf-8 -*-
#Created by Rodrigo Cordeiro
#
####################################################
#
from utils.password import Password
from utils.validators import Validacoes

import sys
argumentos = sys.argv


def password():
    passwd = Password()
    passwd.generate()
    # print(passwd.password)
    validate = Validacoes(passwd.password).validate()
    if validate != False:
        if "-v" in argumentos:
            print("Generating Password")
            print('='*10+'\n'+passwd.password)
            print(validate[1])
            print("\nPontuação: {}".format(validate[0]))
        else:
            print(passwd.password)
        return passwd.password
    else:
        password()

password()

        
