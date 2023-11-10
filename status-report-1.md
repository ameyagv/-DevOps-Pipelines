# Status Report 1

## Accomplishments

- [![Build, Test & Publish](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/actions/workflows/build-test-publish.yml/badge.svg)](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/actions/workflows/build-test-publish.yml) Setup which builds the coffee project, runs es lint checks and runs all the unit tests defined in the project and verify that code coverage is greater than 90%
- Publish workflow setup which build and publishes docker image of the application to GitHub packages.
- [![Deploy](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/actions/workflows/run-ansible.yml/badge.svg)](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/actions/workflows/run-ansible.yml) workflow setup with variables and templates to reduce repitions across environments. Currently deploys to only development environment.
- [GitHub environments](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/deployments) setup done 
- [Ansible playbooks](https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/tree/master/playbooks) in place to setup infrastructure on host machine and deploy coffee project on host machine.

### Contributions

1. Ameya (agvaicha)
- All Commits: https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/commits?author=agvaicha
- Primary Contributions: Ansible Playbook and Deployment Workflow ()

2. Deep (dmmehta2)
- All Commits: https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/commits?author=dmmehta2 + (Commits in name Deep Mehta)
- Primary Contributions: Linting, Code Coverage Checks and Deployment Templates (https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/pull/3)

3. Subodh (sgujar)
- All Commits: https://github.ncsu.edu/CCDS-CSC-519/DevOps-Pipelines/commits?author=sgujar
- Primary Contributions: Build, Test, Publish Workflow and Deployment Workflow ()

## Next Steps 

- Add remianing environments in deployment pipeline, i.e. QA, UAT, Baking and Prod
- Include appropriate tests in each environment apart from deployment

## Retrospective
