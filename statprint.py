#!/usr/bin/env python3
from paramiko import SSHClient
from scp import SCPClient
from time import sleep
from os import system

server=""
sleeptimer = 15 
while True:
    #run llama.cpp and stdout to file
    print("running model")
    system("./randstat -m ggml-model-quant.bin -t 8 -n 128 -p 'The latest news about MLS Soccer is' > output") 
    print("model output")

    #scp file to raspi
    print("uploading file")
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(server, username="", password="")
    # SCPCLient takes a paramiko transport as an argument
    scp = SCPClient(ssh.get_transport())
    scp.put('output', remote_path="/your/path/")
    scp.close()
    print("file uploaded")

    #print file on raspi 
    print("printing file")
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("lp output")
    sleep(sleeptimer)
    print("sleeping for", sleeptimer, "seconds")
