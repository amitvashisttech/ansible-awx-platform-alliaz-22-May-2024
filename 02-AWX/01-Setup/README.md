AWX Installation on K3s
=======================>


Below mentioned command should be able to download and deploy the k3s platform on Ubuntu:

# curl -sfL https://get.k3s.io | sh -

Once deployed, we can run the “kubectl” commands to validate the installation.

# kubectl version

At this point, you would be able to list the nodes:

# kubectl get nodes

Create the required yaml file in your home directory (/home/adminusr in my case). Name it exactly “kustomization.yml”

```
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  # Find the latest tag here: https://github.com/ansible/awx-operator/releases
  - github.com/ansible/awx-operator/config/default?ref=2.5.3

# Set the image tags to match the git version from above
images:
  - name: quay.io/ansible/awx-operator
    newTag: 2.5.3

# Specify a custom namespace in which to install AWX
namespace: awx
```

This deploys the image “awx-operator” under namespace “awx”.

3. Install kustomize

curl -s "https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/hack/install_kustomize.sh"  | bash

3. Initiate the build process

#  ./kustomize build . | kubectl apply -f -


4. Validate the deployment of the required pods. It will probably take a minute for it to come in a ready state.

# kubectl get pods -n awx


5. Now we will create the awx-demo.yml file and expose the application to the nodeport. <awx-demo.yml>
```
---
apiVersion: awx.ansible.com/v1beta1
kind: AWX
metadata:
  name: awx-demo
spec:
  service_type: nodeport
```

Modify the “kustomization.yml”

```
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  # Find the latest tag here: https://github.com/ansible/awx-operator/releases
  - github.com/ansible/awx-operator/config/default?ref=2.5.3
  - awx-demo.yml
# Set the image tags to match the git version from above
images:
  - name: quay.io/ansible/awx-operator
    newTag: 2.5.3
# Specify a custom namespace in which to install AWX
namespace: awx
```



6. Run the deployment again. It will spin additional pods for the application including the postgres db.

# ./kustomize build . | kubectl apply -f -


7. Next, we need to find the port number that we will use to access the application from browser:

# kubectl get svc -n awx


8. Fetch the secret password for the admin user.

# kubectl get secret awx-demo-admin-password -o jsonpath={.data.password} -n awx | base64 -d | more


9. AWX is accessible from the browser:

https://<vm-ip>:<nodeport> (port number would be different in your case)

Login with username “admin” and password (what you got from Step 9).


