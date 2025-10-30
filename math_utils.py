from ast import Return
def find_max_number(num1, num2, num3):
    X = num1
    Y = num2
    Z = num3
    if X > Y :
      if X > Z :
        return X  # Replace 'pass' with code
      else :
        return Z
    else : 
      if Y > Z :
        return Y
      else :
          return Z 





def find_mean(num1, num2, num3):
    mean = (num1 + num2 + num3)/3  
    return mean  # Replace 'pass' with code

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    std = ((((num1 - mean) ** 2 + (num2 - mean) ** 2 + (num3 - mean) ** 2) /3) ** 0.5)
    return mean, std  
