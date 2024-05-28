# Credentials

Ansible Tower uses SSH to connect to remote hosts (or the Windows equivalent). In order to pass the key from Tower to SSH, the key must be decrypted before it can be written a named pipe. Tower then uses that pipe to send the key to SSH (so that it is never written to disk).
If passwords are used, Ansible Tower handles those by responding directly to the password prompt and decrypting the password before writing it to the prompt. 

## Getting Started with Credentials
Access the Credentials page by clicking the Credentials ( ) icon from the left navigation bar. The Credentials
page displays a search-able list of all available Credentials and can be sorted by Name.

### Add a New Credential

To create a new credential:
1. Click the button located in the upper right corner of the Credentials screen.
2. Enter the name for your new credential in the Name ﬁeld.
3. Optionally enter or select the name of the organization with which the credential is associated.

Note: A credential with a set of permissions associated with one organization will remain even after the credential is reassigned to another organization.
4. Enter or select the credential type you want to create.
5. Enter the appropriate details depending on the type of credential selected, as described in the next section,

### Credential Types.
6. Click Save when done.

The following credential types are supported with Ansible Tower:
```
• Amazon Web Services
• Ansible Galaxy/Automation Hub API Token
• Ansible Tower
• GitHub Personal Access Token
• GitLab Personal Access Token
• Google Compute Engine
• Insights
• Machine
• Microsoft Azure Resource Manager
• Network
• OpenShift or Kubernetes API Bearer Token
• OpenStack
• Red Hat Satellite 6
• Red Hat Virtualization
• Source Control
• Vault
• VMware vCenter
```

The credential types associated with CyberArk, HashiCorp Vault, and Microsoft Azure Key Management System (KMS) are part of the credential plugins capability. See the Secret Management System section for further detail.

### Amazon Web Services
Selecting this credential type enables synchronization of cloud inventory with Amazon Web Services.
Tower uses the following environment variables for AWS credentials and are ﬁelds prompted in the user interface:
```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_SECURITY_TOKEN
```

### Google Compute Engine
Selecting this credential type enables synchronization of cloud inventory with Google Compute Engine (GCE).
Tower uses the following environment variables for GCE credentials and are ﬁelds prompted in the user interface:
```
GCE_EMAIL
GCE_PROJECT
GCE_CREDENTIALS_FILE_PATH
```


### Machine
Machine credentials enable Tower to invoke Ansible on hosts under your management. Just like using Ansible on the command line, you can specify the SSH username, optionally provide a password, an SSH key, a key password, or even have Tower prompt the user for their password at deployment time. They deﬁne ssh and user-level privilege escalation access for playbooks, and are used when submitting jobs to run playbooks on a remote host. Network connections (httpapi, netconf, and network_cli) use Machine for the credential type.
Machine/SSH credentials do not use environment variables. Instead, they pass the username via the ansible -u ﬂag, and interactively write the SSH password when the underlying SSH client prompts for it.

Machine credentials have several attributes that may be conﬁgured:
```
• Username: The username to be used for SSH authentication.
• Password: The actual password to be used for SSH authentication. This password will be stored encrypted in the Tower database, if entered. Alternatively, you can conﬁgure Tower to ask the user for the password at launch time by selecting Prompt on launch. In these cases, a dialog opens when the job is launched, promoting the user to enter the password and password conﬁrmation.
• SSH Private Key: Copy or drag-and-drop the SSH private key for the machine credential.
• Private Key Passphrase: If the SSH Private Key used is protected by a password, you can conﬁgure a Key
Password for the private key. This password will be stored encrypted in the Tower database, if entered. Alternatively, you can conﬁgure Tower to ask the user for the password at  launch time by selecting Prompt on launch. In these cases, a dialog opens when the job is launched, prompting the user to enter the password and password
conﬁrmation.
• Privilege Escalation Method: Speciﬁes the type of escalation privilege to assign to speciﬁc users. This is equivalent to specifying the --become-method=BECOME_METHOD parameter, where BECOME_METHOD could be any of the typical methods described below, or a custom method you’ve written. Begin entering the name of the method, and the appropriate name auto-populates. 
```
