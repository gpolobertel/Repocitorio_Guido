import random as rd

def main():
    a=''
    pal='David'
    while a != 'exit':
        print(rd.choice(pal))
        a=input('oprima enter ')

if __name__=="__main__":
    main()