# Overview

[![Python application test with Github Actions](https://github.com/m2rtenm/nd082-Azure-CI-CD/actions/workflows/pythonapp.yml/badge.svg?branch=main)](https://github.com/m2rtenm/nd082-Azure-CI-CD/actions/workflows/pythonapp.yml)

This project includes a Python Flask web app hosted in Azure which makes predictions for housing prices in Boston. It is a pretrained sklearn ML model.
<TODO: complete this with an overview of your project>

## Architecture of the project

![Screenshot of the architecture](https://github.com/m2rtenm/nd082-Azure-CI-CD/blob/main/screenshots/architecture.jpg?raw=true)

## Project Plan
<TODO: Project Plan

* A link to a Trello board for the project - [Trello board for the project](https://trello.com/b/K2zL9BSl/nd082-azure-devops-project-plan)
* A link to a spreadsheet that includes the original and final project plan> [Google Spreadsheets Project plan](https://docs.google.com/spreadsheets/d/17agPpru1mXOnrbVipbrwf9mjVlIdUZzcj_kymhJ2JQ8/edit?usp=sharing)

# Instructions

## Set up Azure Cloud Shell

### Dependencies

* Create an account in [Azure](https://portal.azure.com)
* Create an account in [Github](https://github.com)

### Getting started

* Open the Azure Cloud Shell
* Create SSH keys for accessing the Github repo

```bash
ssh-keygen -t rsa
```

* Copy the public key file content: id_rsa.pub

```bash
cat ~/.ssh/id_rsa.pub
```

* Add the public key content to your Github account (Settings -> SSH and GPG keys -> New SSH key)

* Clone the repository to Azure Cloud Shell

```bash
git@github.com:m2rtenm/nd082-Azure-CI-CD.git
```

After cloning the repo you should be seeing a similar view:

![Screenshot of git clone](https://github.com/m2rtenm/nd082-Azure-CI-CD/blob/main/screenshots/az_cloud_shell_git_clone.png?raw=true)

### Create a Python virtual environment

```bash
python3 -m venv ~/.devops
source ~/.devops/bin/activate
```

### Prepare the virtual environment

```
make all
```

The output should be similar:
![Screenshot of make all](https://github.com/m2rtenm/nd082-Azure-CI-CD/blob/main/screenshots/make_all.png?raw=true)

```
az webapp up -n nd082-marten -l westeurope --sku FREE
```

The `az webapp up` command creates a web app and also a resource group which contains the App Service:

![Screenshot of App Service](https://github.com/m2rtenm/nd082-Azure-CI-CD/blob/main/screenshots/app_service.png?raw=true)

NB! Don't forget to add a different name for the Web App. Every web app has to have a unique name.

If you open the web app URL, then you should see something like this:

![Screenshot of web app](https://github.com/m2rtenm/nd082-Azure-CI-CD/blob/main/screenshots/project_running.png?raw=true)

### How to run the app locally

* Run `make all`
* Run `python3 app.py` in Azure Cloud Shell

![Screenshot of local app](https://github.com/m2rtenm/nd082-Azure-CI-CD/blob/main/screenshots/local_test_app.png?raw=true)

* Run `./make_prediction.sh` in a separate Azure Cloud Shell session

![Screenshot of local prediction](https://github.com/m2rtenm/nd082-Azure-CI-CD/blob/main/screenshots/local_test_prediction.png?raw=true)

## Configure Github Actions


<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


