api_key = "AKIA1234567890EXAMPLE"

masked_key = api_key[:4] + "*" * (len(api_key) - 4)
print(masked_key)
