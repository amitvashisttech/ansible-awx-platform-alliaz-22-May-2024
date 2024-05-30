## To Run the playbook. 

mkdir group_vars/{all,db,web} -p
vim db/vault.yaml
vim web/vault.yaml

ansible-vault encrypt all/vault.yaml
cp -rf all/vault.yaml db/vault.yaml
cp -rf all/vault.yaml web/vault.yaml

ansible-vault edit web/vault.yaml
ansible-vault edit db/vault.yaml
  
tree group_vars/
cat group_vars/all/vault.yaml
cat group_vars/web/vault.yaml
