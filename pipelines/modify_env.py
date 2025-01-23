import os

# Modify environment variables
os.environ['GLOBAL_VAR1'] = 'modified_value1'
os.environ['GLOBAL_VAR2'] = 'modified_value2'

# Write the modified environment variables to a file
with open('env_vars.txt', 'w') as f:
    f.write(f"GLOBAL_VAR1={os.environ['GLOBAL_VAR1']}\n")
    f.write(f"GLOBAL_VAR2={os.environ['GLOBAL_VAR2']}\n")
