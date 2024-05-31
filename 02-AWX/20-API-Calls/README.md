

### Get Inventory Details
curl -X GET http://172.31.0.100:32105/api/v2/inventories/8/ -H 'Authorization: Bearer <token>' | jq


### Create a New Inventory
curl -X POST   http://172.31.0.100:32105/api/v2/inventories/ \
  -H 'Authorization: Bearer nbzEhVqTEghwHyR75kG9E9WU5HdDqW' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Test New Inventory",
    "organization": 2
  }'

### Create Host in Group:
curl -X POST \
   http://172.31.0.100:32105/api/v2/hosts/ \
  -H 'Authorization: Bearer Uqf8ZrHnZzMJtlaDP8UBG1czQQZFS9' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "New Host",
    "inventory": 21,  
    "variables": {
      "ansible_host": "192.168.1.1"
    },
    "enabled": true,
  }'

### Delete Host:

curl -X DELETE \
   http://172.31.0.100:32105/api/v2/hosts/30/ \
  -H 'Authorization: Bearer Uqf8ZrHnZzMJtlaDP8UBG1czQQZFS9' \
  -H 'Content-Type: application/json' 


### Launch Job Template: 
curl -X POST \
  http://172.31.0.100:32105/api/v2/job_templates/<templateid>/launch/ \
  -H 'Authorization: Bearer Uqf8ZrHnZzMJtlaDP8UBG1czQQZFS9' \
  -H 'Content-Type: application/json' \
  -d '{}'


### Launch Job Template with Survey Multi Choice Inputs:  
curl -X POST \
  http://172.31.0.100:32105/api/v2/job_templates/12/launch/ \
  -H 'Authorization: Bearer Uqf8ZrHnZzMJtlaDP8UBG1czQQZFS9' \
  -H 'Content-Type: application/json' \
  -d '{
    "extra_vars": {
      "user": ["Ansible"]
    }
  }'

