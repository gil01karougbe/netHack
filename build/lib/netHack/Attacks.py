from distutils.util import copydir_run_2to3
import subprocess

#============================================ARP POISONNING==========================================
def ARPpoisonning():
    # Victim(192.168.2.10)
    cmd1 = 'gnome-terminal -- bash -c "docker run -it --rm -h \'--Victim--\' --name Victim --network=NET --ip 192.168.2.10 arp_victim bash"'

    # Attacker(192.168.2.20)
    cmd2 = 'gnome-terminal -- bash -c "docker run -it --rm -h \'--Attacker--\' --name Attacker --network=NET --ip 192.168.2.20 arp_attacker bash"'

    # Wireshark to visualize the traffic
    cmd3 = 'gnome-terminal -- bash -c "docker run --rm -h \'--wireshark--\' --privileged --cap-add=NET_ADMIN --name Sniffing --net=host tcpdump -i lig -w - | wireshark -k -i - "'

    # Run in new terminal
    subprocess.Popen(cmd1, shell=True)
    subprocess.Popen(cmd2, shell=True)
    subprocess.Popen(cmd3, shell=True)


#==============================================SYN FLOOD=============================================
def SYNflood():
    # Victim(192.168.2.10) 
    cmd1 = 'gnome-terminal -- bash -c "docker run -it --rm -h \'--Victim--\' --name Victim --network=NET --ip 192.168.2.10 syn_victim bash"'

    # Attacker(192.168.2.20)
    cmd2 = 'gnome-terminal -- bash -c "docker run -it --rm -h \'--Attacker--\' --name Attacker --network=NET --ip 192.168.2.20 syn_attacker bash"'

    # Wireshark to visualize the traffic
    cmd3 = 'gnome-terminal -- bash -c "docker run --rm -h \'--wireshark--\' --user root --privileged --cap-add=NET_ADMIN --name Sniffing --net=host tcpdump -i lig -w - | wireshark -k -i -"'

    # Run in new terminal
    subprocess.Popen(cmd1, shell=True)
    subprocess.Popen(cmd2, shell=True)
    subprocess.Popen(cmd3, shell=True)


#==============================================HTTP FLOOD============================================
def HTTPflood():
    # Victim(192.168.2.10) 
    cmd1 = 'gnome-terminal -- bash -c "docker run -it --rm -h \'--Victim--\' --name Victim --network=NET --ip 192.168.2.10 http_victim bash"'

    # Attacker(192.168.2.20)
    cmd2 = 'gnome-terminal -- bash -c "docker run -it --rm -h \'--Attacker--\' --name Attacker --network=NET --ip 192.168.2.20 http_attacker bash"'

    # Wireshark to visualize the traffic
    cmd3 = 'gnome-terminal -- bash -c "docker run --rm -h \'--wireshark--\' --user root --privileged --cap-add=NET_ADMIN --name Sniffing --net=host tcpdump -i lig -w - | wireshark -k -i -"'

    # Run in new terminal
    subprocess.Popen(cmd1, shell=True)
    subprocess.Popen(cmd2, shell=True)
    subprocess.Popen(cmd3, shell=True)

#==============================================SMURF ATTACK==========================================
def smurf():
    # Victim(192.168.2.10) 
    cmd1 = 'gnome-terminal -- bash -c "docker run -it --rm -h \'--Victim1--\' --name Victim1 --network=NET --ip 192.168.2.10 smurf_victim bash"'
    
    # Victim1(192.168.2.30) 
    cmd4 = 'gnome-terminal -- bash -c "docker run -it --rm -h \'--Victim2--\' --name Victim2 --network=NET --ip 192.168.2.30 smurf_victim1 bash"'

    # Attacker(192.168.2.20)
    cmd2 = 'gnome-terminal -- bash -c "docker run -it --rm -h \'--Attacker--\' --name Attacker --network=NET --ip 192.168.2.20 smurf_attacker bash"'


    # Wireshark to visualize the traffic
    cmd3 = 'gnome-terminal -- bash -c "docker run --rm -h \'--wireshark--\' --user root --privileged --cap-add=NET_ADMIN --name Sniffing --net=host tcpdump -i lig -w - | wireshark -k -i -"'


    # Run in new terminal
    subprocess.Popen(cmd1, shell=True)
    subprocess.Popen(cmd4, shell=True)
    subprocess.Popen(cmd2, shell=True)
    subprocess.Popen(cmd3, shell=True)

#===========================================TCP HIJACKING============================================
def TCPhijacking() :
	#Client(192.168.2.10)
	cmd1=' gnome-terminal -- bash -c " docker run -it --rm -h "--Client--" --name Client --network=NET --ip 192.168.2.10 hijack_client bash" '

	#Server(192.168.2.15)
	cmd2=' gnome-terminal -- bash -c " docker run -it --rm -h "--Server--" --name Server --network=NET --ip 192.168.2.15 hijack_server bash" '

	#Attacker(192.168.2.20)
	cmd3=' gnome-terminal -- bash -c " docker run -it --rm -h "--Attacker--" --name Attacker --network=NET --ip 192.168.2.20 hijack_attacker bash" '

	#Wireshark to visualize the traffic
	cmd4=' gnome-terminal -- bash -c " docker run --rm -h "--wireshark--" --privileged --cap-add=NET_ADMIN --name Sniffing --net=host tcpdump -i lig -w - | wireshark -k -i - " '

	#Run in new terminal
	subprocess.Popen(cmd1 ,shell=True)
	subprocess.Popen(cmd2 ,shell=True)
	subprocess.Popen(cmd3 ,shell=True)
	subprocess.Popen(cmd4 ,shell=True)

#=============================================SESSION RESET==========================================
def SessionRST() :
	#Client(192.168.2.10)
	cmd1=' gnome-terminal -- bash -c " docker run -it --rm -h "--Client--" --name Client --network=NET --ip 192.168.2.10 srst_client bash" '

	#Server(192.168.2.15)
	cmd2=' gnome-terminal -- bash -c " docker run -it --rm -h "--Server--" --name Server --network=NET --ip 192.168.2.15 srst_server bash" '

	#Attacker(192.168.2.20)
	cmd3=' gnome-terminal -- bash -c " docker run -it --rm -h "--Attacker--" --name Attacker --network=NET --ip 192.168.2.20 srst_attacker bash" '

	#wireshark
	cmd4=' gnome-terminal -- bash -c " docker run --rm -h "--wireshark--" --privileged --cap-add=NET_ADMIN --name Sniffing --net=host tcpdump -i lig -w - | wireshark -k -i - " '

	#Run in new terminal
	subprocess.Popen(cmd1 ,shell=True)
	subprocess.Popen(cmd2 ,shell=True)
	subprocess.Popen(cmd3 ,shell=True)
	subprocess.Popen(cmd4 ,shell=True)

#==================================================SCAN==============================================
def Scan() :
	#Target Server
	cmd1=' gnome-terminal -- bash -c " docker run -it --rm -h "--Server--" --name Server --network=NET --ip 192.168.2.15 target_server bash" '

	#Attacker
	cmd2=' gnome-terminal -- bash -c " docker run -it --rm -h "--Attacker--" --name Attacker --network=NET --ip 192.168.2.20 scan_attacker bash" '

	#wireshark
	cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--wireshark--" --privileged --cap-add=NET_ADMIN --name Sniffing --net=host tcpdump -i lig -w - | wireshark -k -i - " '

	#Run in new terminal
	subprocess.Popen(cmd1 ,shell=True)
	subprocess.Popen(cmd2 ,shell=True)
	subprocess.Popen(cmd3 ,shell=True)
#=============================================MAC SPOOFING===========================================
def Macspoofing() :
	#Victim
	cmd1=' gnome-terminal -- bash -c " docker run -it --rm -h "--Victim--" --name Victim --network=NET --ip 192.168.2.10 macspoof_victim bash" '

	#Attacker
	cmd2=' gnome-terminal -- bash -c " docker run -it --rm -h "--Attacker--" --name Attacker --privileged --network=NET --ip 192.168.2.20 macspoof_attacker bash" '

	#wireshark
	cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--wireshark--" --privileged --cap-add=NET_ADMIN --name Sniffing --net=host tcpdump -i lig -w - | wireshark -k -i - " '

	#Run in new terminal
	subprocess.Popen(cmd1 ,shell=True)
	subprocess.Popen(cmd2 ,shell=True)
	subprocess.Popen(cmd3 ,shell=True)


#==================================================NEXT==============================================
