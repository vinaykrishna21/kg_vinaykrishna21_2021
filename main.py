import sys




if __name__ == '__main__':
    x=sys.argv[1]
    y=sys.argv[2]
    if(len(x)!=len(y)):
        print("false")
        sys.exit()
    dict={}
    for i in range(len(x)):
        if x[i] in dict:
            if(dict[x[i]]==y[i]):
                continue
            print("false")
            sys.exit()
        else:
            dict[x[i]]=y[i]
    print("true")
