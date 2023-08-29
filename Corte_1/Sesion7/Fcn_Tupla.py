def app(*args,**kwargs):
    print(args)
    print(kwargs)

if __name__=='__main__':
    app(3,4,56,67,78,a=1,i=2,k=4)