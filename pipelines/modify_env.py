import os

# Modify environment variables
os.environ['GLOBAL_VAR1'] = 'modified_value1'
os.environ['GLOBAL_VAR2'] = 'modified_value2'

# Print the modified environment variables
print(f"GLOBAL_VAR1={os.environ['GLOBAL_VAR1']}")
print(f"GLOBAL_VAR2={os.environ['GLOBAL_VAR2']}")
