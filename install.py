###################STARTING OF DOCKERFILE INSTALLATION
import subprocess

#########REQUIREMENTS INSTALLATION
#Setting up docker network 
net = "docker network create --opt com.docker.network.bridge.name=pfa --subnet=192.168.2.0/24 NET " 
subprocess.run(net,shell=True)
print("#"*77)

#install Wireshark
net = "sudo apt install wireshark" 
subprocess.run(net,shell=True)
print("#"*77)

#install progressbar
net = "sudo pip install progressbar" 
subprocess.run(net,shell=True)
print("#"*77)

#install gnome-terminal
net = "sudo apt-get install gnome-terminal" 
subprocess.run(net,shell=True)
print("#"*77)


#########DOCKER CONTAINERS BUILDING
#ARPpoisonning victim
cmd1= "docker build -t arp_victim ./dockerfiles/ARPpoisonning/arp_victim "
subprocess.run(cmd1 ,shell=True) 
print("#"*77)

#ARPpoisonning attacker
cmd2= "docker build -t arp_attacker ./dockerfiles/ARPpoisonning/arp_attacker "
subprocess.run(cmd2 ,shell=True)
print("#"*77)

#HTTP flood victim
cmd3= "docker build -t httpflood_victim ./dockerfiles/HTTPflood/http_victim "
subprocess.run(cmd3 ,shell=True) 
print("#"*77)

#HTTP flood attacker
cmd4= "docker build -t httpflood_attacker ./dockerfiles/HTTPflood/http_attacker "
subprocess.run(cmd4 ,shell=True)
print("#"*77)

#SYN flood victim
cmd5= "docker build -t syn_victim ./dockerfiles/SYNflood/syn_victim "
subprocess.run(cmd5 ,shell=True) 
print("#"*77)

#SYN flood attacker
cmd6= "docker build -t syn_attacker ./dockerfiles/SYNflood/syn_attacker "
subprocess.run(cmd6 ,shell=True)
print("#"*77)

#smurf victim1
cmd7= "docker build -t smurf_victim1 ./dockerfiles/Smurf/smurf_victim1 "
subprocess.run(cmd7 ,shell=True) 
print("#"*77)

#smurf victim 2
cmd8= "docker build -t smurf_victim2 ./dockerfiles/Smurf/smurf_victim2 "
subprocess.run(cmd8 ,shell=True) 
print("#"*77)

#smurf attacker
cmd9= "docker build -t smurf_attacker ./dockerfiles/Smurf/smurf_attacker "
subprocess.run(cmd9 ,shell=True)
print("#"*77)

#TCP Hijacking client
cmd10= "docker build -t hijack_client ./dockerfiles/TCPhijacking/TCPhijacking_client"
subprocess.run(cmd10 ,shell=True)
print("#"*77)

#TCP Hijacking server
cmd11= "docker build -t hijack_server ./dockerfiles/TCPhijacking/TCPhijacking_server"
subprocess.run(cmd11 ,shell=True)
print("#"*77)

#TCP Hijacking attacker
cmd12= "docker build -t hijack_attacker ./dockerfiles/TCPhijacking/TCPhijacking_attacker"
subprocess.run(cmd12 ,shell=True)
print("#"*77)

#Srst client
cmd13= "docker build -t srst_client ./dockerfiles/Srst/Srst_client"
subprocess.run(cmd13 ,shell=True)
print("#"*77)

#Srst server
cmd14= "docker build -t srst_server ./dockerfiles/Srst/Srst_server"
subprocess.run(cmd14 ,shell=True)
print("#"*77)

#Srst attacker
cmd15= "docker build -t srst_attacker ./dockerfiles/Srst/Srst_attacker"
subprocess.run(cmd15 ,shell=True)
print("#"*77)

#Scan Target server
cmd16= "docker build -t scan_server ./dockerfiles/Scan/Target"
subprocess.run(cmd16 ,shell=True)
print("#"*77)

#Scan attacker Machine
cmd17= "docker build -t scan_attacker ./dockerfiles/Scan/Scanner"
subprocess.run(cmd17 ,shell=True)
print("#"*77)

#MACspoof attacker
cmd18= "docker build -t macspoof_attacker ./dockerfiles/MACspoofing/macspoof_attacker"
subprocess.run(cmd18 ,shell=True)
print("#"*77)

#MACspoof victim
cmd19= "docker build -t macspoof_victim ./dockerfiles/MACspoofing/macspoof_victim"
subprocess.run(cmd19 ,shell=True)
print("#"*77)

# MACflood victim
cmd20 = "docker build -t macflood_victim ./dockerfiles/MACflood/macflood_victim"
subprocess.run(cmd20, shell=True)
print("#" * 77)

# MACflood attacker
cmd21 = "docker build -t macflood_attacker ./dockerfiles/MACflood/macflood_attacker"
subprocess.run(cmd21, shell=True)
print("#" * 77)

#Ping Of Death victim
cmd22 = "docker build -t pod_victim ./dockerfiles/PingOfDeath/pod_victim"
subprocess.run(cmd22, shell=True)
print("#" * 77)

#Ping Of Death attacker
cmd23 = "docker build -t pod_attacker ./dockerfiles/PingOfDeath/pod_attacker"
subprocess.run(cmd23, shell=True)
print("#" * 77)


#tcpdump
tcpdump_cmd= "docker build -t tcpdump ./dockerfiles/Tcpdump "
subprocess.run(tcpdump_cmd ,shell=True) 
print("#"*77)

################## END OF DOCKERFILE INSTALLATION
