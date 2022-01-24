x = __name__                    #Special variable (starts and ends with _)
                                # = "__main__"
                                
from interface import analyze_HDL   #importing runs code
import interface as it              #__name__ variable in interface code = "interface"

#Can avoid complications with 
# if __name__ == "__main__"

HDL = 55
classif = analyze_HDL(HDL)
print("{} is {}".format(HDL, classif))




