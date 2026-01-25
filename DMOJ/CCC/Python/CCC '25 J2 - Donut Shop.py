D = int(input()) 
E = int(input()) 

for i in range(E):
    symbol = str(input()).strip() 
    Q = int(input()) 

    if symbol == "-":
        D -= Q
    
    if symbol == "+":
        D += Q
        
print(D)