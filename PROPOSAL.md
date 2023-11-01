# DevOps Project Proposal

## Problem Statement & Description

### The Problem

In the realm of DevOps, one recurring issue is the manual intervention required for deploying, testing, and maintaining software systems. The problem at hand is the cumbersome and error-prone process of deploying applications in a production environment, particularly when dealing with complex, multi-tiered applications and infrastructure configurations. Manual deployment procedures are time-consuming and prone to human errors, which can lead to service downtime, performance issues, and increased operational costs which often lead to problematic situations that require urgent fixes. This inefficiency can result in frustrated users, loss of revenue, and decreased developer productivity.

### Why it Matters

This problem matters because it impacts both developers and end-users. Developers face delays in delivering new features and bug fixes due to these deployment complexities, while users may experience service disruptions or reduced performance during updates. Automation is the key to mitigating these challenges. Automating the deployment process is critical to reducing these challenges and ensuring a seamless, error-free deployment experience.

In particular, the coffee app may seem like a simple app now, but it doesn't take long before it will have multiple developers working on it every day. This might include adding new features, fixing existing bugs, and scaling up/down the infrastructure to ensure the users have a good experience. As the app grows and the number of developers working on it increases, the following problems arise:

1. Every developer has different code styles, making it difficult for other developers to follow through or ramp-up.
2. There have to be 1-2 developers dedicated to ensuring the new code being added by other developers doesn't introduce new bugs or break the system and is tested extensively. This can get pretty time-consuming as the code base expands resulting in wastage of valuable developer hours.
3. A dedicated team of infrastructure and release engineers, needs to ensure the infrastructure is up to date with the latest code, run multiple test suits to ensure the application works as expected, and then plan out the release to end users.
4. All the above points indicate a major problem, i.e. longer time to production. A team's efficiency is measured by the average time it takes for a code to be written, tested, verified, and deployed to customers. Automating with DevOps is what helps with reducing this time and making the development team efficient.

### Our Solution - The Pipeline

To address this problem, a robust CI/CD (Continuous Integration/Continuous Deployment) pipeline is a highly effective solution. This pipeline automates the entire software delivery process, from source code changes to deployment in the production environment. The pipeline consists of various stages, including code compilation, testing, linting, code coverage analysis, and infrastructure provisioning. It ensures that changes are thoroughly tested and validated before they reach the production environment, reducing the likelihood of issues that could impact users.

This pipeline does not merely respond to code changes; it is a proactive process triggered by code commits or merge requests. By automating the deployment process, this pipeline minimizes human intervention and standardizes the deployment procedures, making it more efficient and reliable. This solution matters because it not only accelerates the development process but also minimizes the risk of service disruptions, ultimately providing a better user experience.

### Tagline

 "From Code Chaos to Deployment Symphony"


## Use Case: 
```
Use Case: PR Merged to Main Branch Triggers Series of Automated and Manual Deployments to Production.
1 Preconditions
   The Node application has been successfully built.
   All tests have passed.
   Code coverage is greater than 90%.
   The mailer has been configured to deliver emails in case of failures.
   The deployment machine(s) (VCL) has been configured and provisioned for passwordless SSH access.
   The Ansible inventory file is updated with the list of hosts.
   The Self-Hosted GitHub Actions system has been provisioned.
2 Main Flow
   The developer initiates the pipeline by creating a PR to the main branch [S1].
   The PR is approved and merged by the Release Engineer [S2].
   Tests are run [S3].
   The Docker image is deployed to the Development Environment [S4].
   The Docker image is deployed to the Testing Environment [S5].
   The image is deployed to the Baking Environment [S6].
   Performance is monitored in both the Production and Baking Environments [S7].
   If performance is similar, deployment to Production is triggered [S8].
3 Subflows
   [S1] User provides a PR message and requests appropriate reviewers, including the Release Engineer.
   [S2] The PR is approved by the Release Engineer.
   [S3] GitHub Actions perform lint checks, run unit tests, and check code coverage.
   [S4] The Docker image is pushed to the Docker Registry and deployed to the Development Environment by Ansible.
   [S5] The Docker image is pulled from the Docker Registry and deployed to the Testing Environment.
   [S6] A user manually triggers deployment to the Baking Environment.
   [S7] App performance is monitored and compared between production and the Baking Environment.
   [S8] Similar performance triggers deployment to production.
4 Alternative Flows
  [E1] Compilation fails.
  [E2] Test suite failes.
```



## Pipeline Design

### High Level

![High Level Pipeline](https://media.github.ncsu.edu/user/26488/files/bc26c9ab-1e09-4d06-9e99-50cd25b7a0e1)


### Low Level

#### Part-1

<img src="https://media.github.ncsu.edu/user/26488/files/94c62250-1933-491a-a4c3-1205b15704c5" width="500" height="800">


#### Part-2

<img src="https://media.github.ncsu.edu/user/26488/files/172fb72f-797e-4742-8318-0a6e85811f2c" width="500" height="800">

