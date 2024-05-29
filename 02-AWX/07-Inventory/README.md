# Inventory

An Inventory is a collection of hosts against which jobs may be launched, the same as an Ansible inventory file. 
Inventories are divided into groups and these groups contain the actual hosts. Groups may be sourced manually, by entering host names into Tower, or from one of Ansible Tower’s supported cloud providers.

## Inventory Plugins
Inventory updates have changed from using deprecated inventory scripts, to using dynamically-generated YAML files which are parsed by their respective inventory plugin. In Ansible, users can provide the new style inventory plugin config directly to Tower via the inventory source source_vars for all the following inventory sources:
• Amazon Web Services EC2
• Google Compute Engine
• Microsoft Azure Resource Manager
• VMware vCenter
• Red Hat Satellite 6
• OpenStack
• Red Hat Virtualization
• Ansible Tower

## Add a new inventory
Adding a new inventory involves several components. Click below to jump to a specific component:
• Add permissions
• Add groups
• Add hosts
• Add source
• View completed jobs
To create a new inventory or Smart Inventory

1. Click the button, and select the type of inventory to create.
2. Enter the appropriate details into the following fields:
• Name: Enter a name appropriate for this inventory.
• Description: Enter an arbitrary description as appropriate (optional).
• Organization: Required. Choose among the available organizations.
Insights Credential: (Only applicable to standard inventories) Enter the appropriate Insights credential if the inventory is used with Insights.
• Instance Groups: Click the button to open a separate window. Choose the instance groups for this inventory to run on. If the list is extensive, use the search to narrow the options.
• Variables: Variable definitions and values to be applied to all hosts in this inventory. Enter variables using either JSON or YAML syntax. Use the radio button to toggle between the two.
