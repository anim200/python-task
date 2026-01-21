port_str = "8080"

# Convert string to integer
try:
    port = int(port_str)
except ValueError:
    print(ValueError)
    print("Invalid")
    exit()

# Check valid range (1-65535)
if 1 <= port <= 65535:
    print("Valid")
else:
    print("Invalid")
