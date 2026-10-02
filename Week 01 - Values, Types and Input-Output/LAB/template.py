"""
RECORD CHECK  -  my version
===========================

Name  :Perle Hope
Lane  :   IT      
Date  :25/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT

label = input("Label=")    
first = float(input("fisrt="))  
second = float(input("second="))    


# ================================================================== PROCESS
 

difference = first-second  # 
percent = first/second*100   # 


# =================================================================== OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# : your report lines go here
print(f"{label:>10}")
print(f"{first:>10.2f}")
print(f"{second:>10.2f}")
print(f"{difference:>+10.2f}")
print(f"{percent:>10.2f}%")
print("=" * 34)


# ==========================================================================

