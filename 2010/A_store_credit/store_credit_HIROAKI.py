num_cases = int( input() )

mycredit = []
num_prod = []
item_prices = []

for i in range( num_cases ):
    a = int( input() )
    b = int( input() )
    c = input()
    d = c.split()
    e = []
    for j in range( len( d ) ):
        e.append(int( d[ j ] ) )

    mycredit.append( a ) 
    num_prod.append( b )
    
    item_prices.append( e )


for i in range( num_cases ):
    Flag = False
    for j in range( num_prod[i] - 1 ):
        for x in range( j+1, num_prod[i], 1 ):
            if mycredit[i] == item_prices[ i ][ j ] + item_prices[i][x]:
                Flag = True
                print( "Case #" + str(i + 1) + ":  " + str(j+1) + " " + str(x+1) )
                break
        if Flag:
            break






            A

