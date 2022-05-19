def arco(x, y):
    if x > 0 & x < 732 & y < 232:
        return "Es Gol"
    else:
        return "No Es Gol"
    if x < 732:
        return "Es Gol"
    else:
        return "No Es Gol"
    if y < 232:
        return "Es Gol"
    else:
        return "No Es Gol"
x = int(input("Valor de x: "))
y = int(input("Valor de y: "))
print (arco (x,y))
       
         

