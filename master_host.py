
with open('/etc/ansible/hosts', 'r') as f:
	content = f.readlines()

print(content)

master = ' '.join([x for x in content if "master" in x])

master_ip = master.split("@")[1]

with open('master_ip.txt', 'w') as f:
	f.write(master_ip)
print(master)

print(master_ip)