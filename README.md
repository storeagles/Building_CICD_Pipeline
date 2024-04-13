# Building_CICD_Pipeline


## Overview

[![Python application test with Github Actions](https://github.com/storeagles/Building_CICD_Pipeline/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/storeagles/Building_CICD_Pipeline/actions/workflows/pythonapp.yml)

This project will demonstrate Continuous Integration and Continuous Delivery (CI/CD) for a Python-based machine learning application using the Flask web framework. Automated code testing has been implemented using GitHub Actions. An Azure DevOps pipeline has been created to test and deploy to an Azure App Service.

Using this guide you will be able to perform the following:
- Use Azure Cloud Shell to run the application
- Deploy the application as an Azure App Service
- Setup an Azure Pipeline
- Load test the application using Locust

## Project Plan

* [A link](https://trello.com/invite/b/oXYeXcdK/ATTIf425c782f362364cc7e532dea4f3eed54BC75A25/ci-cd-project-plan) to a Trello board for the project
* [A link](https://docs.google.com/spreadsheets/d/1PRr1VWrE4QDliflwwuIBh8gDe64Pxn1JKqDGBsFGBBk/edit?usp=sharing) to a spreadsheet that includes the original and final project plan

## Instructions
### Architecture
![alt text](https://github.com/storeagles/Building_CICD_Pipeline/blob/main/CI_CD_ScreenShots/diagram.png)

Once the source code is pushed to GitHub, it triggers GitHub Action for testing. Meanwhile, Azure Pipeline is triggered to build and deploy the application to Azure App Service.

### Set up Azure Cloud Shell 
#### 1. Launch Azure Cloud Shell from portal.azure.com
#### 2. Create SSH-keys and copy to GitHub account

```
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub
```
  -  In GitHub, click on you profile, then click Settings | SSH and GPG Keys.
  -  Click New SSH Key
  -  Paste in the SSH key and give it a title.
  -  Click Add SSH Key
#### 3. Create project Scaffolding
![alt text](https://github.com/storeagles/Building_CICD_Pipeline/blob/main/CI_CD_ScreenShots/Clone_github_repo_SSH.png)

```
git clone git@github.com:storeagles/Building_CICD_Pipeline.git
```

In order to create project scaffolding you should clone your GitHub repository to the Azure CLI. Then you can create Makefile, requirements.txt, virtual environment and project script file.

![alt text](https://github.com/storeagles/Building_CICD_Pipeline/blob/main/CI_CD_ScreenShots/Virtual_env.png)

#### 4. Make all
![alt text](https://github.com/storeagles/Building_CICD_Pipeline/blob/main/CI_CD_ScreenShots/make_all.png)

![alt text](https://github.com/storeagles/Building_CICD_Pipeline/blob/main/CI_CD_ScreenShots/make_all_cont.png)

#### 5. Configure GitHub Actions
![alt text](https://github.com/storeagles/Building_CICD_Pipeline/blob/main/CI_CD_ScreenShots/Passing_GitHub_Actions__Readme.png)

Configuring SaaS build server like GitHub Actions is an essential step for any software project that wants to apply DevOps best practices. By automating build server with GitHub actions you complete the process of Continuous Integration.

#### 6. Use Azure CLI to Deploy and Manage

![alt text](https://github.com/storeagles/Building_CICD_Pipeline/blob/main/CI_CD_ScreenShots/webapp.png)

![alt text](https://github.com/storeagles/Building_CICD_Pipeline/blob/main/CI_CD_ScreenShots/make_predict.png)

This prediction script is responsible for sending some data to our application via the appropriate port. Each numerical value in here represents some feature that is important for determining the price of a house. This prediction also indicates that your application is running. 

#### 7. Load Test an Application using Locust

This locust test script is running a test against the deployed application. 

![alt text](https://github.com/storeagles/Building_CICD_Pipeline/blob/main/CI_CD_ScreenShots/locust_log.png)

### CI/CD 

#### Creating an Agent into AgentPool for a Pipeline

![alt text](https://github.com/storeagles/Building_CICD_Pipeline/blob/main/CI_CD_ScreenShots/myAgent_VM.png)

Virtual Machine service in Azure Portal is an agent. And this agent is associated with an Self-hosted AgentPool. The association is provided by personal access token (PAT).

#### Create Pipeline
![alt text](https://github.com/storeagles/Building_CICD_Pipeline/blob/main/CI_CD_ScreenShots/Pipelines.png)

![alt text](https://github.com/storeagles/Building_CICD_Pipeline/blob/main/CI_CD_ScreenShots/Pipeline_build_deploy.png)

![alt text](https://github.com/storeagles/Building_CICD_Pipeline/blob/main/CI_CD_ScreenShots/pipeline_overview.png)


## Enhancements

We can also deploy our infrastructure as code by deploying terraform infrastructure with packer template. 

## Demo 
[A link](https://www.youtube.com/watch?v=m7zBF7_-3nA) Screencast on YouTube


