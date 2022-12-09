print("input should be in the form \n utkarsh gaur,khushi singh,sonu kumar")
a=input("data: ").split(",")
c=" "
for i in a:
    b=i.split(" ")
    for m in b:
        c+=m[0]
        c+=" "
    print("the acronym of",i,"is",c.upper())
    c=" "
