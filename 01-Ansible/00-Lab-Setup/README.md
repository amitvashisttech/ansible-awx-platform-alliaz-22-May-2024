
# In the following demo will be setting up 3 Node ( 1 Ansible Cantrol Server & 2 Ubuntu Remote Servers & 1 CentOS Remote Server ) 

 

## Now provision three virtual machines with following commands:

### Step 1: Open Windows Powershell
### Step 2: Navigate to Vagrant Setup Directory 
```
cd Desktop/vagrant-setup/devops
```

### Step 3: Checking the status of existing virtual machines  
```
vagrant status 
```

### Step 4: Bring up all the virtual machines mentioned in Vagrantfile 
```
vagrant up 
```

### Step 5: Login inside the virtual machine via ssh 
```
vagrant ssh master 
```
### Step 6: Become a super user 
```
sudo su - 
```

### Step 7: Clone our project repo
```
git clone https://github.com/amitvashisttech/ansible-awx-platform-alliaz-22-May-2024.git 
```


