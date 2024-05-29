# JOB TEMPLATES

A job template is a definition and set of parameters for running an Ansible job. Job templates are useful to execute the same job many times. Job templates also encourage the reuse of Ansible playbook content and collaboration between teams. While the REST API allows for the execution of jobs directly, Tower requires that you first create a job template.


Create a Job Template
To create a new job template:
1. Click the button then select Job Template from the menu list. 
2. Enter the appropriate details into the following fields:
• Name: Enter a name for the job.
• Description: Enter an arbitrary description as appropriate (optional).
• Job Type: Choose a job type:
• Run: Execute the playbook when launched, running Ansible tasks on the selected hosts.
• Check: Perform a “dry run” of the playbook and report changes that would be made without actually making them. Tasks that do not support check mode will be skipped and will not report potential changes.
• Prompt on Launch: If selected, even if a default value is supplied, you will be prompted upon launch to choose a job type of run or check.

• Inventory: Choose the inventory to be used with this job template from the inventories available to the currently logged in Tower user.
• Prompt on Launch: If selected, even if a default value is supplied, you will be prompted upon launch to choose an inventory to run this job template against.
• Project: Choose the project to be used with this job template from the projects available to the currently logged in Tower user.

• SCM Branch: This field is only present if you chose a project that allows branch override. Specify the overriding branch to use in your job run. If left blank, the specified SCM branch (or commit hash or tag) from the project is used. For more detail, see job branch overriding.
– Prompt on Launch: If selected, even if a default value is supplied, you will be prompted upon launch to choose an SCM branch.
• Playbook: Choose the playbook to be launched with this job template from the available playbooks. This field automatically populates with the names of the playbooks found in the project base path for the selected project. Alternatively, you can enter the name of the playbook if it is not listed, such as the name of a file (like foo.yml) you want to use to run with that playbook. If you enter a filename that is not valid, the template will display an error, or cause the job to fail.
• Credentials: Click the button to open a separate window. Choose the credential from the available options to be used with this job template. Use the drop-down menu list to filter by credential type if the list is extensive. 

• Forks: The number of parallel or simultaneous processes to use while executing the playbook. A value of zero uses the Ansible default setting, which is 5 parallel processes unless overridden in /etc/ansible/ansible.cfg.
• Limit: A host pattern to further constrain the list of hosts managed or affected by the playbook. Multiple patterns can be separated by colons (“:”). As with core Ansible, “a:b” means “in group a or b”, “a:b:&c” means“in a or b but must be in c”, and “a:!b” means “in a, and definitely not in b”.
• Prompt on Launch: If selected, even if a default value is supplied, you will be prompted upon launch to choose a limit.

• Verbosity: Control the level of output Ansible produces as the playbook executes. Choose the verbosity from Normal to various Verbose or Debug settings. This only appears in the “details” report view. Verbose logging includes the output of all commands. Debug logging is exceedingly verbose and includes information on SSH operations that can be useful in certain support instances. Most users do not need to see debug mode output.

• Instance Groups: Click the button to open a separate window. Choose the instance groups on which you want to run this job template. If the list is extensive, use the search to narrow the options.
• Job Slicing: Specify the number of slices you want this job template to run. Each slice will run the same tasks against a portion of the inventory. For more information about job slices, see Job Slicing.
• Timeout: Allows you to specify the length of time (in seconds) Tower may run the task before it is canceled. Defaults to 0 for no job timeout.
• Show Changes: Allows you to see the changes made by Ansible tasks.
• Prompt on Launch: If selected, even if a default value is supplied, you will be prompted upon launch to choose whether or not to show changes.
• Options: Specify options for launching this template, if necessary.
• Enable Privilege Escalation: If enabled, run this playbook as an administrator. This is the equivalent of passing the --become option to the ansible-playbook command.
• Enable Provisioning Callbacks: Enable a host to call back to Tower via the Tower API and invoke the launch of a job from this job template. Refer to Provisioning Callbacks for additional information.
• Enable Webhook: Turns on the ability to interface with a predefined SCM system web service that is used to launch a job template. Currently supported SCM systems are GitHub and GitLab.
• Webhook Service: Select which service to listen for webhooks from
• Webhook Credential: Optionally, provide a GitHub or GitLab personal access token (PAT) as a credential to use to send status updates back to the webhook service. Before you can select it, the credential must exist. See Credential Types to create one.


3. When you have completed configuring the details of the job template, click Save.

## Add Permissions

The Permissions tab allows you to review, grant, edit, and remove associated permissions for users as well as team members. To assign permissions to a particular user for this resource:
1. Click the Permissions tab.
2. Click the button to open the Add Users/Teams window.
3. Specify the users or teams that will have access then assign them specific roles:
a. Click to select one or multiple check boxes beside the name(s) of the user(s) or team(s) to select them.
4. Review your role assignments for each user and team.
5.Click Save when done, and the Add Users/Teams window closes to display the updated roles assigned for each user and team.


## View Completed Jobs
The Completed Jobs tab provides the list of job templates that have ran. Click Expanded to view details of each job, including its status, ID, and name; type of job, time started and completed, who started the job; and which template, inventory, project, and credential were used. You can filter the list of completed jobs using any of these criteria.


## Scheduling
Access the schedules for a particular job template from the Schedules tab.

## Launch a Job Template

A major benefit of Ansible Tower is the push-button deployment of Ansible playbooks. You can easily configure a template within Tower to store all parameters you would normally pass to the ansible-playbook on the command line–not just the playbooks, but the inventory, credentials, extra variables, and all options and settings you can specify on the command line.

Easier deployments drive consistency, by running your playbooks the same way each time, and allow you to delegate responsibilities–even users who aren’t Ansible experts can run Tower playbooks written by others.

1. Click on Launch. 
