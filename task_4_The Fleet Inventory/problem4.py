servers = ["web01", "db01", "app01", "web02"]


web_servers = servers[0:-1:3] + servers[-1:] 


web_servers = servers[:1] + servers[-1:]

print(web_servers)  
