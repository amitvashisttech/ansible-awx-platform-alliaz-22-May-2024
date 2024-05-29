# PROJECTS
A Project is a logical collection of Ansible playbooks, represented in Tower.

You can manage playbooks and playbook directories by either placing them manually under the Project Base Path on your Tower server, or by placing your playbooks into a source code management (SCM) system supported by Tower,including Git, Subversion, Mercurial, and Red Hat Insights.

## Add a new project
To create a new project:
1. Click the button, which launches the Create Project window.
2. Enter the appropriate details into the following required fields:
```
• Name
• Description (optional)
• Organization - A project must have at least one organization. Pick one organization now to create the project,and then after the project is created you can add additional organizations.
• Ansible Environment (optional) - Select from the drop-down menu list a custom virtual environment on which to run this project. This field is only present if custom environments were previously created. See Using virtualenv with Ansible Tower in the Ansible Tower Upgrade and Migration Guide.
• SCM Type - Select from the drop-down menu list an SCM type associated with this project. The options in the subsequent section become available depend on the type you choose. Refer to Manage playbooks manually or Manage playbooks using source control in the subsequent sections for more detail.
```

## Work with Permissions
The set of Permissions assigned to this project (role-based access controls) that provide the ability to read, modify, and administer projects, inventories, job templates, and other Tower elements are Privileges.

You can access the project permissions via the Permissions tab next to the Details tab. This screen displays a list of users that currently have permissions to this project. The list may be sorted and searched by User, Role, or Team Role.


## Add Permissions
The Permissions tab allows you to review, grant, edit, and remove associated permissions for users as well as team members. To assign permissions to a particular user for this resource:
1. Click the Permissions tab.
2. Click the button to open the Add Users/Teams window.
3. Specify the users or teams that will have access then assign them specific roles:
a. Click to select one or multiple check boxes beside the name(s) of the user(s) or team(s) to select them.

Different resources have different options available:
• Admin allows read, run, and edit privileges (applies to all resources)
• Use allows use of a resource in a job template (applies all resources except job templates)
• Update allows updating of project via the SCM Update (applies to projects and inventories)
• Ad Hoc allows use of Ad Hoc commands (applies to inventories)
• Execute allows launching of a job template (applies to job templates)
• Read allows view-only access (applies to all resources)

4. Review your role assignments for each user and team.


## Work with Notifications

Clicking the Notifications tab allows you to review any notification integrations you have setup.
Use the toggles to enable or disable the notifications to use with your particular project. For more detail, see Enable and Disable Notifications.
If no notifications have been set up, click the NOTIFICATIONS link from inside the gray box to create a new notification.



