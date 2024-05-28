# Tags & Limits

```
  321  ansible-playbook site.yaml --check
  322  ansible-playbook site.yaml
  323  ansible-playbook site.yaml --tags "webserver"
  325  ansible-playbook site.yaml --tags "firewall"
  332  ansible-playbook site.yaml --tags "firewall" --limit 172.31.0.100
  335  ansible-playbook site.yaml --tags "firewall" --limit "web:db"
  336  ansible-playbook site.yaml --tags "firewall" --limit "web:&prod"
  341  ansible-playbook site.yaml --tags "firewall" --limit 'web:&prod:!ansible'
  342  ansible-playbook site.yaml --tags "webserver" --limit 'web:&prod:!ansible'
```
