   64  mkdir 02-Modules
   65  ls
   66  cd 02-Modules/
   67  ls
   68  ansible-doc -l
   69  ansible-doc -l | grep -e 'ping|yum|apt'
   70  ansible-doc -l | grep -ie 'ping|yum|apt'
   71  ansible-doc -s ping
   72  ansible-doc ping
   73  ansible-doc apt
   74  ansible-doc service
   75  ls
   76  cp -rf ../01-Inventory/hosts
   77  cp -rf ../01-Inventory/hosts  .
   78  ls
   79  vim hosts
   80  ls
   81  ansible web -m ping
   82  ansible -i hosts web -m ping
   83  ansible -i hosts web -m user -a "name=test1 password=123456"
   84  cat hosts
   85  ansible -i hosts web -m user -a "name=test1 password=123456" -b
   86  ansible -i hosts web -m command -a "cat /etc/password" -b
   87  ansible -i hosts web -m command -a "cat /etc/passwd" -b
   88  ansible -i hosts web -m user -a "name=test1 password=123456" -b
   89  ansible -i hosts web -m user -a "name=test2 password=123456" -b
   90  ansible -i hosts web -m command -a "uname -a" -b
   91  ansible -i hosts web -m command -a "hostname -f" -b
   92  df -h
   93  ansible -i hosts web -m command -a "df -h " -b
   94  cat /etc/os-release
   95  cat /etc/*-release
   96  ansible -i hosts web -m command -a "cat /etc/*-releases " -b
   97  ansible -i hosts web -m command -a "cat /etc/*-release" -b
   98  cat /etc/*-release
   99  ansible -i hosts web -m command -a "cat /etc/*-release" -b
  100  ansible -i hosts web -m shell -a "cat /etc/*-release" -b
