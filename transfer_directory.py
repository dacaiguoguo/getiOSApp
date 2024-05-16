#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import paramiko
from scp import SCPClient
import os

def ssh_connect_via_tunnel(local_port, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('127.0.0.1', port=local_port, username=username, password=password)
        print("SSH connection established")
        return ssh
    except Exception as e:
        print(f"Failed to connect via SSH: {e}")
        return None

def tar_directory(ssh, remote_dir, tar_file):
    try:
        command = f'tar -czf {tar_file} -C {remote_dir} .'
        stdin, stdout, stderr = ssh.exec_command(command)
        stdout.channel.recv_exit_status()  # Wait for the command to finish
        print(f"Directory {remote_dir} compressed to {tar_file}")
    except Exception as e:
        print(f"Failed to compress directory: {e}")

def scp_transfer_file(ssh, remote_file, local_file):
    try:
        with SCPClient(ssh.get_transport()) as scp:
            print(f"Transferring {remote_file} to {local_file}")
            scp.get(remote_file, local_path=local_file)
            print("Transfer complete")
    except Exception as e:
        print(f"Failed to transfer file: {e}")

def remove_remote_file(ssh, remote_file):
    try:
        command = f'rm {remote_file}'
        stdin, stdout, stderr = ssh.exec_command(command)
        stdout.channel.recv_exit_status()  # Wait for the command to finish
        print(f"Removed remote file {remote_file}")
    except Exception as e:
        print(f"Failed to remove remote file: {e}")

def main():
    local_port = 2222
    username = 'root'
    password = 'alpine'
    remote_dir = '/var/mobile/Containers/Data/Application/E4B9D9A2-3F80-42EF-9A0C-AF74F6843065'
    tar_file = '/var/mobile/Containers/Data/Application/E4B9D9A2-3F80-42EF-9A0C-AF74F6843065.tar.gz'
    local_file = '/Users/yanguosun/Developer/getiOSApp/sand/SnapEdit.tar.gz'

    ssh = ssh_connect_via_tunnel(local_port, username, password)
    if ssh is None:
        print("SSH connection failed")
        return

    try:
        tar_directory(ssh, remote_dir, tar_file)
        scp_transfer_file(ssh, tar_file, local_file)
        remove_remote_file(ssh, tar_file)
    finally:
        ssh.close()

    # 解压传输过来的文件
    # os.system(f'tar -xzf {local_file} -C /Users/yanguosun/Developer/getiOSApp/sand/SnapEdit')

if __name__ == '__main__':
    main()
