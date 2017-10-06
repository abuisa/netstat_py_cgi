import subprocess
import psutil
import socket

def get_appname(pid):
	ps = psutil.Process(int(pid))
	return ps.name()
	
def get_dn(ip):
	try:	
		ip = ip.rpartition(':')[0]
		dn = socket.gethostbyaddr(ip)
		dn = dn[0]
		return dn
	except:
		pass	
		

def out2list(sf,kode):
	cmd_out = subprocess.Popen(['netstat', '-ano'], stdout=subprocess.PIPE).communicate()
	out2list = list(cmd_out)
	out2list = out2list[0].splitlines()

	listku = []
	for row in out2list:
		row2list = row.decode('utf-8').split()
		if row2list: 
			lx = len(row2list)
			if lx == 4: 
				listku += [row2list.insert(3,' - ')]
			listku += [row2list]
	if kode:
		newlistku = [];no = 0	
		newlistku += [["NO","PROTO","LOCAL_IP","FOREIGN_IP","HOST_NAME","STATE","PID","APP_NAME"]]
		for l in listku:	
			if l:
				if l[0].upper() == 'TCP' or l[0].upper() == 'UDP':
					pid = l[-1];exe = get_appname(pid);dn = get_dn(l[2])
					if any(sf.upper() in el.upper() for el in l) or (sf.upper() in exe.upper()) and sf != '':
						no +=1;l.insert(0,str(no));l.insert(4,dn);l.insert(len(l),exe);newlistku += [l]
	
	if kode == False:
		newlistku = [];no = 0	
		newlistku += [["NO","PROTO","LOCAL_IP","FOREIGN_IP","STATE","PID","APP_NAME"]]
		for l in listku:	
			if l:
				if l[0].upper() == 'TCP' or l[0].upper() == 'UDP':
					pid = l[-1];exe = get_appname(pid)
					if any(sf.upper() in el.upper() for el in l) or (sf.upper() in exe.upper()) and sf != '':
						no +=1;l.insert(0,str(no));l.insert(len(l),exe);newlistku += [l]
				
	return newlistku

	
