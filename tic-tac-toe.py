import copy
##############################################################################
def apply_decision(turn,num)
    #change table with x and o
    #turn= x or o
    
    global table
    
    if num==1
        table[0][0]=turn 
    elif num==2
        table[0][1]=turn
    elif num==3
        table[0][2]=turn
    elif num==4
        table[1][0]=turn    
    elif num==5
        table[1][1]=turn
    elif num==6
        table[1][2]=turn
    elif num==7
        table[2][0]=turn
    elif num==8
        table[2][1]=turn
    elif num==9
        table[2][2]=turn
    else
        print(none)


##############################################################################
def terminate(state)
    #we have 8 possible rule to check 
    
    if (state[0][0]==state[0][1]==state[0][2])
        if state[0][0]=='x'
            return 1
        else
            return -1

    elif (state[1][0]==state[1][1]==state[1][2])
        if state[1][0]=='x'
            return 1
        else
            return -1

    elif (state[2][0]==state[2][1]==state[2][2])
        if state[2][0]=='x'
            return 1
        else
            return -1
        
    elif (state[0][0]==state[1][0]==state[2][0])
        if state[0][0]=='x'
            return 1
        else
            return -1
        
    elif (state[0][1]==state[1][1]==state[2][1])
        if state[0][1]=='x'
            return 1
        else
            return -1
        
    elif (state[0][2]==state[1][2]==state[2][2])
        if state[0][2]=='x'
            return 1
        else
            return -1

    elif (state[0][0]==state[1][1]==state[2][2])
        if state[0][0]=='x'
            return 1
        else
            return -1
        
    elif (state[0][2]==state[1][1]==state[2][0])
        if state[0][2]=='x'
            return 1
        else
            return -1
    else
        return 0
##############################################################################
#alphamax's best option on the path to root
#betamin's best option on the path to root        
def max_value(state,level,alpha,beta)
    
    if(terminate(state)!=0)
        return {Uterminate(state)(10-level),move0}
    
    maximum={U-200,move0}
    
    for i in range(3)
        for j in range(3)
            
            if state[i][j]!='x' and state[i][j]!='o'
                
                new_state=copy.deepcopy(state)
                new_state[i][j]='x'
                temp=min_value(new_state,level+1,alpha,beta)
                
      
                if temp[U]maximum[U]
                    maximum={Utemp[U],move(i3)+(j+1)}   
                
                if maximum[U]=beta
                    return maximum
                
                if alpha=maximum[U]
                    alpha=maximum[U]
    
    return maximum

##############################################################################
#alphamax's best option on the path to root
#betamin's best option on the path to root
def min_value(state,level,alpha,beta)
    
    if(terminate(state)!=0)
        return {Uterminate(state)(11-level),move0}
    
    minimum={U200,move0}
    
    for i in range(3)
        for j in range(3)
            
            if state[i][j]!='x' and state[i][j]!='o'
                
                
                new_state=copy.deepcopy(state)
                new_state[i][j]='o'
                temp=max_value(new_state,level+1,alpha,beta)
 
                if temp[U]minimum[U]
                    minimum={Utemp[U],move(i3)+(j+1)}    
    
                if minimum[U]=alpha
                    return minimum
                
                if beta=minimum[U]
                    beta=minimum[U]
                    
    return minimum
    
    
##############################################################################
    
table=[[1,2,3],
       [4,5,6],
       [7,8,9]]


for i in range(5)
    
    for k in table
        print(k)    
        
    val = input(Enter your number ) 
    
    apply_decision(o,int(val))
    
    if terminate(table)!=0
        for k in table
            print(k)
        print(terminate(table))
        break
    
    AI=max_value(copy.deepcopy(table),0,-200,200)
    apply_decision(x,AI[move])
    
    if terminate(table)!=0
        for k in table
            print(k)
        print(terminate(table))
        break
    

