# Overview

[![Python application test with Github Actions](https://github.com/m2rtenm/nd082-Azure-CI-CD/actions/workflows/pythonapp.yml/badge.svg?branch=main)](https://github.com/m2rtenm/nd082-Azure-CI-CD/actions/workflows/pythonapp.yml)

This project includes a Python Flask web app hosted in Azure which makes predictions for housing prices in Boston. It is a pretrained sklearn ML model.

## Architecture of the project

![Screenshot of the architecture](https://github.com/m2rtenm/nd082-Azure-CI-CD/blob/main/screenshots/architecture.jpg?raw=true)

## Project Plan

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
git clone git@github.com:m2rtenm/nd082-Azure-CI-CD.git
```

After cloning the repo you should see a similar view:

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

Note: For cost saving purposes, use the parameter `--sku FREE`

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

## Configuration of Github Actions

### Create the Github Actions workflow

In Github go to Actions -> New workflow -> Set up a workflow yourself

Use this code to replace the default content of the template:

*Note:* For Python version, use at least version 3.7. In this project, version 3.9 has been used. Feel free to use a newer version.

```
name: Python application test with Github Actions

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.9
      uses: actions/setup-python@v1
      with:
        python-version: 3.9
    - name: Install dependencies
      run: |
        make install
    - name: Lint with pylint
      run: |
        make lint
    - name: Test with pytest
      run: |
        make test
```

Commit the yml file and after that, the build should contain a green mark. A successful build looks like this:

![Screenshot of Github Actions](https://github.com/m2rtenm/nd082-Azure-CI-CD/blob/main/screenshots/github_actions.png?raw=true)

## Configuration of Azure Pipelines

For configuring Azure Pipelines, please use the [official documentation](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

The result of a successful deployment looks something like this:

![Screenshot of the deployment](https://github.com/m2rtenm/nd082-Azure-CI-CD/blob/main/screenshots/deployment_success.png?raw=true)

## Verifying the application

The project contains a file `make_predict_azure_app.sh` which sends a POST request to the web app to return with a prediction. The response looks something like this:

![Screenshot of the Azure prediction](https://github.com/m2rtenm/nd082-Azure-CI-CD/blob/main/screenshots/prediction_success.png?raw=true)

### Logs for the application

The following command helps to see application logs, for example the logs when the prediction has been made:
```
az webapp log tail -n nd082-marten
```
Note: Replace the -n parameter with your own App Service name that you have used for the project.

The output of logs looks like this:
![Screenshot of logs](https://github.com/m2rtenm/nd082-Azure-CI-CD/blob/main/screenshots/logs_prediction.png?raw=true)

### Load testing with Locust

You have several options how to install Locust. In this project, it is specified in the `requirements.txt` but you can also install it manually like this:

```
pip install locust
```

To run the locustfile.py, use the following command:

```
locust -f locustfile.py
```

Open up http://localhost:8089/ in your browser and enter the URL of the project to the host field if not filled. In the advanced options, you can also specify the duration of the load test.

![Screenshot of locust page](https://github.com/m2rtenm/nd082-Azure-CI-CD/blob/main/screenshots/locust_test_start.png?raw=true)

After running the load test, the results page looks like this:

![Screenshot of locust results](https://github.com/m2rtenm/nd082-Azure-CI-CD/blob/main/screenshots/locust_test_results.png?raw=true)


## Enhancements

An option would be to use Docker and/or Kubernetes for such projects. Another idea is to implement the backend in another programming language, for example C#. Definitely there should be several other branches existing in Github to separate environments (development, staging, production etc). A verification pipeline could be an option to ensure that testing in lower environments has been successful. Only then the deployment can be made in production.

## Demo 

[Link to the demo](https://youtu.be/hIteXTrw6wY)