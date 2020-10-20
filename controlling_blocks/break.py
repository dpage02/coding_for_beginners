# initialize i
for i in range(1,4):

    # add nested inner loop
    for j in range(1,4):
    
       # having a break statement at start of inner loop to break form that loop 
        if i ==2 and j==1:
            print('Breaks inner loop at i=2 j=1')
            break 

        # print message
        print('Running i=',i,'j=',j)
