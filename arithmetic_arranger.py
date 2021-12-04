def arithmetic_arranger(problems,condition=False):
 
 if len(problems) > 5:
      return('Error: Too many problems.')

 _split=[]
#split each arithemetic sum

 for problem in problems:
  _split.append(problem.split(" "))

#separate op1, op2 and sign
 op1,sign,op2=[],[],[]
  
 for i in range(3):
    for j in range(len(_split)):
        
        if i==0:
          op1.append(_split[j][i])
        elif i==1:
          sign.append(_split[j][i])
        else:
          op2.append(_split[j][i])
 
 #Opertor check
 for _sign in sign:
    if _sign!="+" and _sign!="-":
      return "Error: Operator must be '+' or '-'."  
    else : continue
        
 #Digit check       
 if not all(map(lambda x: x.isdigit(), op1)):
        return "Error: Numbers must only contain digits."
        
 if not all(map(lambda x: x.isdigit(), op2)):
        return "Error: Numbers must only contain digits."    
 
 #Width check        
 for  _op1 in op1:
    if len(_op1)<5:
      continue
    else : 
      return "Error: Numbers cannot be more than four digits."

 for  _op2 in op2:
    if len(_op2)<5:
      continue
    else : 
      return "Error: Numbers cannot be more than four digits."   
 
 #Four line output

 topline, midline, dashes, bottomline = [],[],[],[]
 
 for i in range(4):
    for j in range(len(_split)):
      
        if i==0:
            topline.append(op1[j].rjust(max( len(op1[j]) , len(op2[j]) ) + 2))
            if j<len(_split)-1:
             topline.append(" "*4)
            
        elif i==1:
            midline.append(sign[j].ljust(0))  
            midline.append(op2[j].rjust( max( len(op1[j]), len(op2[j]) ) + 1))
            if j<len(_split)-1:
             midline.append(" "*4)
                         
        elif i==2:
          dashes.append( "-"*(max( len(op1[j]) , len(op2[j]) ) + 2 ) )
          if j<len(_split)-1:
            dashes.append(" "*4)
        else :
            if sign[j]=="+":
                bottomline.append( str( int(op1[j]) + int(op2[j]) ).rjust( max( len(op1[j]) , len(op2[j]) ) + 2) )
                if j<len(_split)-1:
                 bottomline.append(" "*4)
            else : 
                bottomline.append( str( int(op1[j]) - int(op2[j]) ).rjust( max( len(op1[j]) , len(op2[j]) ) + 2) )
                if j<len(_split)-1:
                 bottomline.append(" "*4)
                
 _topline="".join(topline)
 _midline="".join(midline)
 _dashes="".join(dashes)
 _bottomline="".join(bottomline)   
  
   
 if condition:
    #,_midline,_dashes,_bottomline
    arranged_problems = _topline + "\n" + _midline + "\n" + _dashes + "\n" + _bottomline
    
    return arranged_problems                            
 else:
    #,_midline,_dashes,_bottomline    
    arranged_problems = _topline + '\n' + _midline + '\n' + _dashes 
    return arranged_problems