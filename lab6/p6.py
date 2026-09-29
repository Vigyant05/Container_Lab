import os

print("===Environment Variabls passed to container===")

for key,value in os.environ.items():
    print(f"{key}={value}")