
# WORKFLOWS
Workflows allow you to configure a sequence of disparate job templates (or workflow templates) that may or may not share inventory, playbooks, or permissions. However, workflows have ‘admin’ and ‘execute’ permissions, similar to job templates. A workflow accomplishes the task of tracking the full set of jobs that were part of the release process as a single unit.
Job or workflow templates are linked together using a graph-like structure called nodes. These nodes can be jobs, project syncs, or inventory syncs. A template can be part of different workflows or used multiple times in the same workflow. A copy of the graph structure is saved to a workflow job when you launch the workflow.


# WORKFLOW JOB TEMPLATES

A workflow job template links together a sequence of disparate resources that accomplishes the task of tracking the full set of jobs that were part of the release process as a single unit. These resources may include:
• job templates
• workflow templates
• project syncs
• inventory source syncs

## Create a Workflow Template

1. Click the button then select Workflow Template from the menu list.
2. Enter the appropriate details into the following fields:
• Name: Enter a name for the workflow template.
• Description: Enter an arbitrary description as appropriate (optional).
• Organization: Optionally enter or search for an organization to associate the workflow.
• Inventory: Optionally enter or search for an inventory to be used with this workflow template from the inventories available to the currently logged in Tower user.
• Prompt on Launch: If selected, you can provide an inventory when this workflow template is launched, or when this workflow template is used within another workflow template.
• Limit: Optionally specify a limit for subset of servers that your workflow is going to run. This value is a host pattern to further constrain the list of hosts managed or affected by the playbook. Multiple patterns can be
separated by colons (“:”). As with core Ansible, “a:b” means “in group a or b”, “a:b:&c” means “in a or b but must be in c”, and “a:!b” means “in a, and definitely not in b”.
• Prompt on Launch: If selected, even if a default value is supplied, you will be prompted upon launch to choose a limit.
• SCM Branch: Optionally specify the branch to override all job template nodes that prompt for a branch.
– Prompt on Launch: If selected, even if a default value is supplied, you will be prompted upon launch to choose an SCM branch.
• Labels: Supply optional labels that describe this workflow template, such as “dev” or “test”. Labels can be used to group and filter workflow templates and completed jobs in the Tower display.
– Labels are created when they are added to the Workflow Template. Labels are associated to a single Organization using the Project that is provided in the Workflow Template. Members of the Organization can create labels on a Workflow Template if they have edit permissions (such as an admin role).
– Once the Workflow Template is saved, the labels appear in the Templates overview.
– Click on the “x” beside a label to remove it. When a label is removed, and is no longer associated with a Workflow or Workflow Template, the label is permanently deleted from the list of Organization labels.
– Jobs inherit labels from the Workflow Template at the time of launch. If a label is deleted from a Workflow Template, it is also deleted from the Job.

3. When you have completed configuring the workflow template, click Save.



## Work with Permissions
• Clicking on Permissions allows you to review, grant, edit, and remove associated permissions for users as well as team members.
• Click the button to create new permissions for this workflow template.


## View Completed Jobs
• The Completed Jobs tab provides the list of workflow templates that have ran. Click Expanded to view the various details of each job.
