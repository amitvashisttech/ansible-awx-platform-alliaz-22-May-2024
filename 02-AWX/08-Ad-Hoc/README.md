# Running Ad Hoc Commands

To run an ad hoc command:
1. Select an inventory source from the list of hosts or groups. The inventory source can be a single group or host,a selection of multiple hosts, or a selection of multiple groups.
2. Click the button.
3. Enter the details for the following fields:
• Module: Select one of the modules that Tower supports running commands against
```
command apt_repository mount win_service
shell apt_rpm ping win_updates
yum service selinux win_group
apt group setup win_user
apt_key user win_ping
```

• Arguments: Provide arguments to be used with the module you selected.
• Limit: Enter the limit used to target hosts in the inventory. To target all hosts in the inventory enter all or *, or leave the field blank. This is automatically populated with whatever was selected in the previous view prior to clicking the launch button.
• Machine Credential: Select the credential to use when accessing the remote hosts to run the command. Choose the credential containing the username and SSH key or password that Ansbile needs to log into the remote hosts.
• Verbosity: Select a verbosity level for the standard output.
• Forks: If needed, select the number of parallel or simultaneous processes to use while executing the command.
• Show Changes: Select to enable the display of Ansible changes in the standard output. The default is OFF.
• Enable Privilege Escalation: If enabled, the playbook is run with administrator privileges. This is the equivalent of passing the --become option to the ansible command.
• Extra Variables: Provide extra command line variables to be applied when running this inventory. Enter variables using either JSON or YAML syntax. Use the radio button to toggle between the two.

4. Click the button to run this ad hoc command.
