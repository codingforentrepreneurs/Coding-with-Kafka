# Terraform Setup & Common Commands


## Install Terraform

Download and install from [the docs](https://developer.hashicorp.com/terraform/install) for your machine.

Open terminal/powershell and verify with:

```bash
terraform --version
```

## Files to always ignore in Git

- `*.tfvars`
- `*.tfstate`

Others listed in the [Github Terraform Gitignore](https://raw.githubusercontent.com/github/gitignore/main/Terraform.gitignore)


## Commands for Terraform

### `terraform init`

After you declare `main.tf`, run the following next to `main.tf`
```
terraform init
```
> Tip, if you are one directory up and the Terraform module is in `devops/main.tf`, you can run `terraform -chdir=devops init`

You will run `terraform init` anytime you add a new provider.

### `terraform plan`
Anytime you want to review changes you have made with terraform, run:

```bash
terraform plan
```
> Once again, if you are one directory up and the Terraform module is in `devops/main.tf`, you can run `terraform -chdir=devops plan`


### `terraform apply`
Once you are ready to apply changes you can run:

```bash
terraform apply
```

A few other items about this:
- `terraform apply` will require your input on if you are ready to make changes
- `terraform apply -auto-approve` will automatically approve changes and do them
- `terraform apply -auto-approve -destroy` will automatically destroy all changes


### `terraform destroy`
This is how you can take down everything you provisioned with Terraform:

```bash
terraform destroy
```
This command is actually a shortcut to `terraform apply -destroy` and requires using input. 


### `terraform console`
Sometimes you can use terraform console to better understand what is going on in your infrastructure.

```
terraform console
```
When you're done, you can exit with `Ctrl+C` or typing `exit` and hitting enter.