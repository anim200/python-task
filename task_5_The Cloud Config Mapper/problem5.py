vm = {
    "id": "i-1234567890abcdef0",
    "ip": "10.0.1.42", 
    "status": "running",
    "region": "us-east-1"
}

vm["status"] = "stopped"
vm["instance_type"] = "t3.large"

print(vm)

