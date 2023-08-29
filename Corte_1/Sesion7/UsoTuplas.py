import Fcn_Tupla

def main():
    a=''
    pal=''
    while a != 'exit':
        pal += (f' {a}')
        a=input('Ingrese un dato: ')
        
    Fcn_Tupla.app(pal,i=1)
    

if __name__=="__main__":
    main()
else:
    Fcn_Tupla.app(3,4,56,67,78,a=1,i=2,k=4)
    