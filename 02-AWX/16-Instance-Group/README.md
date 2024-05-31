# Instance Groups

Instances can be grouped into one or more Instance Groups. Instance groups can be assigned to one or more of the resources listed below.

- Organizations
- Inventories
- Job Templates

When a job associated with one of the resources executes, it will be assigned to the instance group associated with the resource. During the execution process, instance groups associated with Job Templates are checked before those associated with Inventories. Similarly, instance groups associated with Inventories are checked before those associated with Organizations. Thus, Instance Group assignments for the three resources form a hierarchy: Job Template > Inventory > Organization.


## Create an instance group
To create a new instance group:
1. Click the icon from the left navigation menu to open the Instance Groups configuration window.
2. Click the button and select Create Instance Group
3. Enter the appropriate details into the following fields:
```
• Name. Names must be unique and must not be named tower.
• Policy Instance Minimum. Enter the minimum number of instances to automatically assign to this group when new instances come online.
• Policy Instance Percentage. Use the slider to select a minimum percentage of instances to automatically assign to this group when new instances come online.
```
