"""
RECORD CHECK  -  my version
===========================

Name  :PERLE Hope
Lane  :IT      
Date  :03/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
overlimit_count=0
while True:
 label = input("Label=")  
 
 if label=="quit":
  break

 value = float(input("value="))  
 limit =float(input("limit="))


# ================================================================== PROCESS

difference = value -limit   
percent = (value/limit) * 100  
if percent >=100:
    status="OVER LIMIT"
    overlimit_count+=1
elif percent>=90:
    status="WARNING"
else:
    status="OK"


# =================================================================== OUTPUT

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"Label    : {label}")
print(f"Value    : {value}")
print(f"Limit    : {limit}")
print(f"Status   : {status}")

print(f"Difference: {difference:.2f}")
print(f"Percent   : {percent:.2f}%")


print("=" * 34)

print()
print(f"OVER LIMIT records:{overlimit_count}")


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
