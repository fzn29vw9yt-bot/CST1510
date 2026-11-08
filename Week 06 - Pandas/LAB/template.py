"""
RECORD CHECK  -  my version
===========================

Name  :PERLE HOPE GLORIA
Lane  :  IT      
Date  : 7/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

# ==================================================================== LOAD


#  Read the CSV file
df = pd.read_csv("it_usages.csv")


# ================================================================= PROCESS



# Calculate percentage of storage used
df["percent"] = (df["used_gb"] / df["total_gb"]) * 100

# Add a status column using apply() and lambda
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100
    else "WARNING" if p >= 90
    else "OK"
)


# ================================================================== OUTPUT

# Print the DataFrame
print("Complete DataFrame")
print(df)

# Print rows that are not OK
print("\nRows requiring attention")
attention = df[df["status"] != "OK"]
print(attention)

# Group by status and count each group
print("Count per status")

status_counts = df.groupby("status").size()

print(status_counts)



# ==========================================================================

