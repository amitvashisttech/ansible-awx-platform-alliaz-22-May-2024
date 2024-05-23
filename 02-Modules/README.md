## Ansible Modules Exercise

#### This README.md file provides a step-by-step guide for using various Ansible modules to perform tasks such as checking connectivity, managing users, and executing commands on remote hosts. This exercise also includes creating a directory structure and copying the inventory file.
#### Prerequisites

#### Ensure you have the following prerequisites:

    #### Ansible installed on your control node.
    #### A configured inventory file.
    #### Remote hosts configured in your Ansible inventory.

## Steps

### Create a Directory for Modules
```
mkdir 02-Modules
```

### List Available Ansible Modules

sh
```
ansible-doc -l

```

### Get Synopsis for the ping Module

```
ansible-doc -s ping

```
### Get Documentation for the ping Module
```
ansible-doc ping

```
### Get Documentation for the apt Module

```
ansible-doc apt

```
### Get Documentation for the service Module

```
ansible-doc service

```
### Copy Inventory File from Previous Directory

```
cp -rf ../01-Inventory/hosts .
```

### Ping the web Group Using Specified Inventory File

```
ansible -i hosts web -m ping
```
### Create a User on the web Group

```
ansible -i hosts web -m user -a "name=test1 password=123456"
```

### View Inventory File
```
cat hosts
```
### Create a User on the web Group with Sudo Privileges

```
ansible -i hosts web -m user -a "name=test1 password=123456" -b
```
### Execute Command to View Password File

```
ansible -i hosts web -m command -a "cat /etc/password" -b
```

### Correct Command to View Password File

```
ansible -i hosts web -m command -a "cat /etc/passwd" -b
```

### Create Another User on the web Group with Sudo Privileges
```
ansible -i hosts web -m user -a "name=test2 password=123456" -b
```
### Execute Command to View System Information
```
ansible -i hosts web -m command -a "uname -a" -b
```

### Execute Command to View Hostname
```
ansible -i hosts web -m command -a "hostname -f" -b
```

### Check Disk Space on Local Machine

```
df -h
```

### Check Disk Space on Remote Hosts

```
ansible -i hosts web -m command -a "df -h" -b
```
### View OS Release Information on Local Machine


```
cat /etc/os-release
```
### Alternative Command to View OS Release Information
```
cat /etc/*-release
```
###Execute Command to View OS Release Information on Remote Hosts

```
ansible -i hosts web -m command -a "cat /etc/*-release" -b
```

### Execute Shell Command to View OS Release Information on Remote Hosts

```    
ansible -i hosts web -m shell -a "cat /etc/*-release" -b
```

