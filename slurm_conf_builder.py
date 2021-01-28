import socket
host_name = socket.gethostname() 

f = open("/etc/ansible/hosts", "r")
found = False
ip_list = []
name_list = []
for x in f:
	if "[storage]" in x:
		found = False
	if found and "@" in x and "master" not in x:
		ip_list.append(x.split("@")[1].split()[0])
		name_list.append("node" + x.split("@")[1].split()[0].split(".")[-1])
	if found and "master" in x:
		host_ip = x.split("@")[1].split()[0]
	if "[compute]" in x:
		found = True
	if "[control]" in x:
		found = True

ips = str(ip_list).replace("'", "").replace(" ", "").replace('[', '').replace(']', '')
names = str(name_list).replace("'", "").replace(" ", "").replace('[', '').replace(']', '')
f.close()
f = open("raw/guineapig/specs_raw.txt", "r")
cpus = f.readline().split()[1]
threads_per_core = f.readline().split()[-1]
cores_per_socket = f.readline().split()[-1]
sockets = f.readline().split()[1]
free_mem = int(f.readline().split()[1]) - 4000
f.close()
f = open("slurm_conf_template", "r")
slurm_conf_str = f.read()
f.close()
slurm_conf_str = slurm_conf_str.replace("CPUSPH", cpus)
slurm_conf_str = slurm_conf_str.replace("TPCPH", threads_per_core)
slurm_conf_str = slurm_conf_str.replace("CPSPH", cores_per_socket)
slurm_conf_str = slurm_conf_str.replace("SOCKETSPH", sockets)
slurm_conf_str = slurm_conf_str.replace("MEMORYPH", str(free_mem))
slurm_conf_str = slurm_conf_str.replace("NODENAMES", names)
slurm_conf_str = slurm_conf_str.replace("NODEADRESSES", ips)
slurm_conf_str = slurm_conf_str.replace("CONTROLNAME", host_name)
slurm_conf_str = slurm_conf_str.replace("CONTROLIP", host_ip)
f = open("slurm.conf","w+")
f.write(slurm_conf_str)
f.close()

f = open("ntp_conf_template", "r")
ntp_conf_str = f.read()
f.close()

ntp_conf_str = slurm_conf_str.replace("MASTER", host_ip)
f = open("ntp.conf","w+")
f.write(slurm_conf_str)
f.close()


