def convertToBase13(num):
  if num == 0:
    return "0"
    
  base_13 = "0123456789ABC"
  result = ""
  pos_num = abs(num)
  
  while pos_num > 0:
    result += base_13[pos_num%13]
    pos_num = pos_num//13
    
  if num < 0:
    return "-" + result[::-1]
    
  return result[::-1]
