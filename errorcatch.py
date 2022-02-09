def HDL_mod(HDL, LDL):

    try:
        from database import HDL_mod
        DL = HDL_mod(HDL, LDL)
        
    except ImportError:
        from math import sqrt
        print("module not available")
        DL = sqrt(HDL*HDL + LDL*LDL)
    
    return DL

def main():
    HDL = 120
    LDL = 60
    DL = HDL_mod(HDL, LDL)
    print(DL)

if __name__ == "__main__":
    main()