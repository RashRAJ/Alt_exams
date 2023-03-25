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

`run kubctl get nodes` to confirm everything is okay

## Setting up Argocd CI/CD
![argocd](https://user-images.githubusercontent.com/56790407/226378394-80f7d4d9-cbef-475f-9031-7db913ea265b.png)

- When your cluster is created uncomment the helm.tf file and run `teraform apply` to install the argo cd app in your cluster

- To get argocd login detalils run `kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d`
tap on the url and sign in username: `admin` and use the password generated

- Create a base app and connect argocd to the argocd apps folder on the github repository
- Place your flask app deployment manifest in the argocd folder
- Use kustomize to convert te socks app docker compose file to a manifest.
- you can access my argocd at www.argocd.octoarts.me

## Monitoring

![grafana dashboard](https://user-images.githubusercontent.com/56790407/226373639-14bdebd2-f549-40fa-b655-7b6bbfd37fdb.png)


- Install prometheus and grafana by placing the manifest files in the argocd apps folder for automatic deployment
- Get your grafana password and url using this command `kubectl get secret --namespace argocd grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo`
- you can Access my grafana dashboad at www.grafana.octoarts.me 

 

# Links

- Set up your ingress controller and access all apps via the link bellow

## portfolio app
- www.berlin.octorats.me       (portfolio app)
![image](https://user-images.githubusercontent.com/56790407/227743876-dbd8af3f-478b-4af0-afc1-25d8e59bd208.png)
- www.grafana.octoarts.me      (Grafana Dashboard)

## prometheus 
- www.prometheus.octoarts.me   (Prometheus)

## Socks app
- www.socksapp.octoarts.me     (Socks app)
![image](https://user-images.githubusercontent.com/56790407/227743449-1b121194-3f31-4f9b-900a-3f561af5535a.png)







