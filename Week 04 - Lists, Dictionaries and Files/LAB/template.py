"""
RECORD CHECK  -  my version
===========================

Name  :PERLE Hope Gloria
Lane  :  IT      
Date  :18/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(record):
    """Check whether a record is over its limit."""
    if record["value"] > record["limit"]:
        return "OVER LIMIT"
    else:
        return "WITHIN LIMIT"


def print_report(record, status):
    """Print the report for one record."""
    print("Label:", record["label"])
    print("Value:", record["value"])
    print("Limit:", record["limit"])
    print("Status:", status)
    print("--------------------")


def load_records(path):
    """Read records from a file and return a list."""
    records = []

    with open(path, "r") as file:
        for line in file:
            label, value, limit = line.strip().split(",")

            record = {
                "label": label,
                "value": float(value),
                "limit": float(limit)
            }

            records.append(record)

    return records


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

records = []   # replace with your code

records = load_records("records.txt")
# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
over_limit_count = 0

for record in records:
    status = check_record(record)
    print_report(record, status)

    if status == "OVER LIMIT":
        over_limit_count = over_limit_count + 1

print("Number over limit:", over_limit_count)



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
with open("results.txt", "w") as file:
    for record in records:
        status = check_record(record)
        file.write(record["label"] + ", " + status + "\n")

print("Results saved to results.txt")
