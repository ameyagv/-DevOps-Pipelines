# Status Report 2 - 11/17/2023

## Accomplishments

Following work has been accomplished so far in setting up a DevOps infrastructure for the coffee project:

### Docker Image

- We created the [docker image](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/blob/master/coffee-project/Dockerfile) required to run the coffee-project as container.

- We also created GitHub Packages repository in GitHub.com as it wasn't supported in GitHub.ncsu.edu, where we publish our docker images to be consumed during deployment.

### Branch Protection Rules

We currently have the following [branch protection rules](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/settings/branch_protection_rules/1603) in place for the master branch:

1. Minimum one reviewer required
2. Build-Test step should succeed before the pull request can be merged

### Build, Test & Publish

Workflow: [build-test-publish.yml](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/blob/master/.github/workflows/build-test-publish.yml)

This workflow has 2 stages:

1. [build-test](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/actions/runs/74797/job/153096): This installs the required dependencies and runs the following checks:

    - Application Lint: We add eslint configuration to the existing coffee-project to run the es lint checks on the code base. The existing application has many errors that are printed in [deployment logs](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/actions/runs/74797/job/153096) but it currently has continue-on-error parameter set as true which lets the step pass even with errors as we currently do not intend to fix there errors.

    - [Unit Tests and Coverage](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/actions/runs/74797/job/153096): We run the existing unit tests in the coffee-project app and ensure the test coverage is greater than 90% to pass the step.

    - [Ansible Lint](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/actions/runs/74797/job/153096): We run ansible linting checks for the anible playbooks in the repository. We currently have 4 errors but we haven't fixed it just to showcase how the errors show up in the summary of workflow as [annotations](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/actions/runs/74797). We will fix this before the final submission.

2. [publish](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/actions/runs/74797/job/153097): This builds the docker image of the coffee-project and publishes it to GitHub Packages. 

    - Here we have 2 identical steps of build and publish, this is because we run the [Master publish](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/blob/master/.github/workflows/build-test-publish.yml#L62) with tag latest only when the pipeline is run from master branch, but when run from any other branch it deploys with tag dev. This tag is used during the deployment stage, i.e. the docker image with tag dev is deployed in development environment while the latest tag is used to deploy in all other environments. This provides an opportunity for developers to see their changes in a deployment environment similar to production.

    - This step doesn't run when this pipeline is run as part of a PR as we don't want docker image to build and publish unnecessarily for every PR. This we have ensured by following if condition in publish step: 
    
        `if: github.ref == 'refs/heads/master' || github.ref == 'refs/heads/development' || github.event_name == 'workflow_dispatch'`

### Deploy

#### Workflows: 

1. [deploy.yml](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/blob/master/.github/workflows/run-ansible.yml)
2. [deploy-template.yml](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/blob/master/.github/workflows/deploy-template.yml)

#### Ansible Playbooks:

1. [setup-docker.yml](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/blob/master/playbooks/setup-docker.yml) - This is responsible for setting up the infratructure in the vcl, i.e. required packages and docker
2. [deploy-application.yml](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/blob/master/playbooks/deploy-application.yml) - This is responsible for pulling the docker image from github packages and deploying it onto the host
3. [open-port.yml](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/blob/master/playbooks/open-port.yml) - This is responsible for opening up port 3000 so that the website is accessible over the internet.

### Machines:

In total we plan to have 8 VCL machines for the entire project for the following purposes:

1. Control Node and GitHub Runner
2. DEV environment
3. QA environment
4. UAT environment
5. Baking environment
6. PRD environment load balancer
7. PRD machine 1
8. PRD machine 2

#### Highlights

The deployment worklfow is responsible for deploying the coffee-project onto the following environments:
1. [DEV](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/deployments/activity_log?environment%253Ddev)
2. [QA](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/deployments/activity_log?environment%253Dqa)
3. [UAT](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/deployments/activity_log?environment%253Duat)
4. [Baking](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/deployments/activity_log?environment%253Dbaking)
5. PRD - Work in Progress

We have made use of following GitHub features and some custom developed features to make the workflows reusable and efficient:

1. Variable groups: We created a github action [set-variable](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/blob/master/.github/actions/set-variable/action.yml), which allows us to have different [variable groups](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/tree/master/.github/variables) for different environments and this action converts those variables into environment variables for workflow to use.

2. Workflow Templates: We created one [template](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/blob/master/.github/workflows/deploy-template.yml) to setup infrastructure and deploy coffee project and used it across environment with input variables to allow it to deploy across environments. This template is consumed in the main workflow [deploy.yml](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/blob/master/.github/workflows/run-ansible.yml).

3. Environments: We created [environments](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/settings/environments) to allow for easy tracking of deployments and also add manual approvals for certain environments. We also output the deployed website url in the pipeline run for ease of access for developers with the help of environments in the workflow. (See the blue hyperlinks below each stage: https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/actions/runs/74800)

#### Stages

1. DEV: This stage we only setup infra and deploy the app in development environment.

2. QA: Once dev succeds, we deploy app in QA environment and thus we run the following tests:

    - [Integration Tests](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/blob/master/coffee-project/test/integration-tests/integration.test.js): We wrote integration tests for the coffee-project which invokes the deployed APIs and ensured the orders are placed successfully.

    - [UI Tests](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/blob/master/coffee-project/test/ui-tests/ui.test.js): We wrote UI tests that opens up the webpage, clicks on the order button and then ensures a popup is visible with Ordered text.

    - Security Tests: We perform a OWASP ZAP scan on the deployed application and publish the output as an [artifact](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/suites/74991/artifacts/170) with results. We currently let it continue even if security vulnerabilities are detected as we don't have a plan to fix all issues currently.

3. UAT: Once QA and all its tests succeed we deploy to UAT environment and run load tests as a [python script](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/blob/master/performance-metrics/load-test.py), by invoking the website 1000 times parallely and getting the average response time and ensure it is below the acceptable threshold which for now we have set as 3 seconds.

4. Baking: To initiate deployment to this environment we have added a manual approval check in [environment settings](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/settings/environments/3548/edit), i.e. we want someone to manually approve the deployment from UAT to Baking. In baking we intend to get more performance metrics related to deployed environment i.e. the VCL in our case, i.e. monitor its CPU and Memory and ensure its below the threshold.

### Team Contributions:

1. Ameya (agvaicha)
- All Commits: https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/commits?author=agvaicha
- Primary Contributions: Ansible Playbooks, VCL setup and configuration, Deployment Workflow, Integration Tests ([commit]())

2. Deep (dmmehta2)
- All Commits: https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/commits?author=dmmehta2 + (Commits in name Deep Mehta)
- Primary Contributions: Linting, Code Coverage, Workflow Templates, Variable Group Action, UI & OWASP Tests, Environment Setup ([commit]())

3. Subodh (sgujar)
- All Commits: https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/commits?author=sgujar
- Primary Contributions: Build, Test, Publish Workflow, GitHub Packages Setup, Ansible Playbooks, Load Testing Script ([commit]())

## Next Steps

1. Ameya (agvaicha)
- Develop script to determine performance metrics in the baking and production environment.
- This will take about 40 hours of work as it involves determining how to collect app metrics and how to measure environment metrics, and the thresholds for the same.

2. Deep (dmmehta2)
- Integrate the rollback mechanism into the deployment workflow if the production environment metrics aren't meeting the standards.
- This will take about 30-40 hours of work as it involves writing another step in the deployment workflow after the production deployment that runs after a certain wait time, and then runs the script created by Ameya. If the script fails, then the previous docker image will have to be pulled and deployed using Ansible, for this the ansible playbooks need to be modified.

3. Subodh (sgujar)
- Implement load balancing setup for the production environment and allow for blue/green deployment by using load balancer and two prod servers.
- This will take about 40 hours of work as it involves setting up the ansible playbook for the load balancer and setup the appropriate algorithm for the same. Also another important part is to determine how the blue green deployment can be made possible in the current workflow.

## Retrospective

