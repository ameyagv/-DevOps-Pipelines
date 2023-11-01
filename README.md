
# DevOps Project Overview
###  "From Code Chaos to Deployment Symphony"


## Problem Statement
The problem this DevOps project aims to address is the need for a streamlined and automated software deployment pipeline. In today's software development landscape, delivering high-quality software rapidly is essential. Manual deployments are error-prone and time-consuming, which can impact both developers and end-users. Automating the deployment process is the key to solving this problem.

### Why It Matters
This problem matters because it affects both developers and end-users. Manual deployments are error-prone, causing downtime and frustration for users. Developers are often required to perform repetitive and error-prone tasks, such as server restarts at inconvenient hours. An automated deployment pipeline can mitigate these issues and ensure the reliable, rapid, and efficient delivery of software.

### What Our Pipeline Does
Our continuous deployment pipeline automates the deployment process of the code hosted at [GitHub Repository](https://github.ncsu.edu/CSC-519/coffee-project). It leverages GitHub Actions, a linting step, a testing step, and an Ansible playbook to deploy the application. This pipeline is triggered automatically in response to events like pull requests to the release branch.


## Use Case


## Pipeline Design

![High Level Pipeline](https://media.github.ncsu.edu/user/26488/files/bc26c9ab-1e09-4d06-9e99-50cd25b7a0e1)

### Architecture Components
Our DevOps pipeline consists of the following components:
- **GitHub Actions:** For automation and orchestration of the deployment pipeline.
- **Linting Step:** Ensures code quality and consistency.
- **Testing Step:** Runs automated tests to verify the application's correctness.
- **Ansible Playbook:** Manages deployment and configuration.
- **Branch Protections Rules:** Ensure code quality and compliance.
- **Release Branch Trigger:** Automatically triggers the pipeline upon PR to the release branch.
- **Deployment in a Container:** Applications are deployed within Docker containers for consistency and portability.


## Mentors
- Prof. John-Paul Ore (jwore)
- Md Rayhanur Rahman (mrahman)


## Team Members
- Ameya Vaichalkar (agvaicha)
- Deep Mehta (dmmehta2)
- Subodh Gujar (sgujar)

## License
This project is licensed under the [MIT License](LICENSE).

