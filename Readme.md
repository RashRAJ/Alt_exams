# Deploying a falsk app and socks microservice app on kubernates, and setting up using argocd and gitOps and monitoring with Prometheus and Grafana

## Prerequisites
- AWS CLI
- Terraform
- Docker
- Flask
- Kubectl

## Using this Repository

# Create the EKS cluster using by following the following Terraform commands
- git clone this repository

- Get your acces keys from your aws console and configure aws cli using this command ` aws configure` and follow the prompts with your details

- Move to the terraform directory `cd eks-terraform`

- Create an S3 bucket for your terraform state files 
`aws s3api create-bucket --bucket <bucket-name> --region <region> --create-bucket-configuration LocationConstraint=<region>`

- comment out the helm.tf file so you dont run into errrors

- Run ` Terraform init`
- `Terraform plan` go over the configurations
- Then run `Terraform apply`

Update your Kubeconfig file by running the following command `aws eks update-kubeconfig --name <clustername> --region <cluster region>` 

`run kubctle get nodes` to confirm everything is okay

## Setting up Argocd

- When your cluster is created uncomment the helm.tf file and run `teraform apply` to install the argo cd app in your cluster

- To get argocd login detalils run `kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d`
tap on the url and sign in username: `admin` and use the password generated

- Create a base app and connect argocd to the argocd apps folder on the github repository
- Place your flask app deployment manifest in the argocd folder
- Use kustomize to convert te socks app docker compose file to a manifest.
- Install prometheus and grafana by placing the manifest files on the argocd apps folder forautomatc deployment
- Get your grafana password using this command `kubectl get secret --namespace argocd grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo`

- Set up your ingress controller






