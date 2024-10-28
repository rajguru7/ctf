# CVSS 3.1 vector values for each metric in your example
metrics = {
    "AV": {"N": 0.85, "A": 0.62, "L": 0.55, "P": 0.2},   # Attack Vector
    "AC": {"L": 0.77, "H": 0.44},                        # Attack Complexity
    "PR": {"N": 0.85, "L": 0.62, "H": 0.27},             # Privileges Required
    "UI": {"N": 0.85, "R": 0.62},                        # User Interaction
    "S": {"U": "unchanged", "C": "changed"},             # Scope
    "C": {"N": 0.0, "L": 0.22, "H": 0.56},              # Confidentiality
    "I": {"N": 0.0, "L": 0.22, "H": 0.56},              # Integrity
    "A": {"N": 0.0, "L": 0.22, "H": 0.56},              # Availability
}

# Define the CVSS vector values
vector = {
    "AV": "L",  # Local
    "AC": "L",  # Low
    "PR": "N",  # None
    "UI": "R",  # Required
    "S": "U",   # Unchanged
    "C": "H",   # High
    "I": "H",   # High
    "A": "H",   # High
}

# Exploitability Sub-score Calculation
exploitability = 8.22 * metrics["AV"][vector["AV"]] * metrics["AC"][vector["AC"]] * metrics["PR"][vector["PR"]] * metrics["UI"][vector["UI"]]

# Impact Sub-score Calculation
iss = 1 - ((1 - metrics["C"][vector["C"]]) * (1 - metrics["I"][vector["I"]]) * (1 - metrics["A"][vector["A"]]))
impact = 6.42 * iss

# Adjusting for Scope (S)
if vector["S"] == "U":  # Unchanged scope
    base_score = min(impact + exploitability, 10)
else:  # Changed scope
    impact = 7.52 * (iss - 0.029) - 3.25 * (iss - 0.02) ** 15
    base_score = min(1.08 * (impact + exploitability), 10)

# Output the CVSS base score rounded to one decimal place
base_score = round(base_score, 1)
print("CVSS Base Score:", base_score)
