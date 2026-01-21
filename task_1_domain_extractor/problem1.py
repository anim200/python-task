url = "https://api.github.com/v3"
host_with_sub = url.split("//")[1].split("/")[0]
print(host_with_sub)
parts = host_with_sub.split(".")  
print(parts[-2:])
domain = ".".join(parts[-2:])
print(domain)
