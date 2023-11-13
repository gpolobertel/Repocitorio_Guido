festivo={'Enero':['1 - año nuevo','reyes magos'],
        'Febrero':['No tiene festivos'],
        'Marzo':['20 - Dia de san jose']}
def main():
    mes=input('ingrese un mes: ')
    print(festivo[mes])


if __name__=='__main__':
    main()