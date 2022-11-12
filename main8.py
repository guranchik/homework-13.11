def Change_number():
    q=0
    name=""
    num=""
    print("введите имя или номер")
    name = input()
    file = open("numberBook", "r")
    f = file.readlines()
    file.close()
    len1=len(f)
    for i in range(len1):
        line=f[i]
        l2=line.split("<razdel>")
        if name == l2[0] or name == l2[1]:
            what=input("что вы хотите изменить?(1-имя,2-номер)\n")
            while True:
                if what!="1" and what!="2":
                    what=input("что вы хотите изменить?(1-имя,2-номер)\n")
                else:
                    break
            if what=="1":
                print("введите новое имя")
                new=input()
                l2[0]=new
                newline=l2[0]+"<razdel>"+l2[1]+"<razdel>"
                f[i]=newline
                break

            if what=="2":
                print("введите новый номер")
                new=input()
                l2[1]=new
                newline=l2[0]+"<razdel>"+l2[1]+"<razdel>"
                f[i]=newline
                break

        

                
    f1=""
    for s in range(len(f)):
        f1=f1+f[s]+"\n"   
                 
    file = open("numberBook", "w")
    file.write(f1)
    file.close()
    




Change_number()


















#меню\ изменить номер