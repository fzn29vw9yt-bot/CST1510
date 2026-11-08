"""
RECORD CHECK  -  my version
===========================

Name  :PERLE HOPE GLORIA 
Lane  :  IT     
Date  :8/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS


def parse_line(raw_line):
    """Clean and parse one raw IT storage record into a dictionary."""

    line = raw_line.strip().lower()

    hostname_part, rest = line.split(",", 1)

    hostname = hostname_part.strip()

    fields = {}

    for piece in rest.split(","):
        key, value = piece.split("=", 1)

        key = key.strip()
        value = value.strip()

        fields[key] = float(value)

    return {
        "hostname": hostname,
        "used": fields["used"],
        "total": fields["total"]
    }
def status_of(record):
    """Classify an IT server according to its storage usage."""

    percentage = (record["used"] / record["total"]) * 100

    if percentage >= 100:
        return "OVER LIMIT"
    elif percentage >= 90:
        return "WARNING"
    else:
        return "OK"


# ====================================================================== INPUT
from pathlib import Path

file_path = Path(__file__).parent / "it_record.txt"

with open(file_path) as file:
    raw_records = file.readlines()



# =============================================================== PROCESS + OUTPUT



total_records = 0
flagged_records = 0

for raw_record in raw_records:

    try:
        record = parse_line(raw_record)
        status = status_of(record)

        total_records += 1

        percentage = (record["used"] / record["total"]) * 100

        print(record)
        print(f"Status: {status} ({percentage:.1f}%)")
        print()

        if status != "OK":
            flagged_records += 1

    except ValueError:
        print("Could not parse:", raw_record.strip())
        print()



# ==========================================================================


print(f"Total valid records: {total_records}")
print(f"Flagged records: {flagged_records}")
