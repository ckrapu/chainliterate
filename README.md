# Overview
`chainliterate` is a teaching repository showing how to incrementally build up a production-grade AI system by adding new features in stages. Each folder in this project is a deployable application with all the code and dependencies needed to operate. The core functionality of this repository is built around LlamaIndex Workflows, Chainlit, and Pydantic. The Invoke Python library is used to create command line utilities essential for application management and debugging.

This repository is meant to be used in conjunction with a short course providing step-by-step explanations of how each version works and improves over the previous version. Each folder also includes a set of exercises to help sharpen your skills.

For deployment, we assume usage of Docker containers for most cases.

# Requirements

To make the most of this, you'll want to have a Mac or Linux-based computer or virtual machine to use. If using a VM, make sure you have network access to port 8000 (and port 5432 may be helpful as well). This code may work on Windows-based machines, but it has not been extensively tested.

Before getting started, you'll want to sign up for the following services:
- [OpenRouter](https://openrouter.ai/) for LLM completions
- [Google Cloud Platform](https://console.cloud.google.com/), for creating an OAuth2 client
- [Amazon Web Services](console.aws.amazon.com) for S3, cloud PostgreSQL, and Amplify.



We'll incur modest charges on OpenRouter, AWS, and GCP over this course, and you'll also receive reminders to terminate these resources once we're finished.

# Contents

| Name | Features |
|------|----------|
|`01-getting-started`| Chainlit + OpenRouter for chat completion |
|`02-handling-user-data`| Adding persistence via PostgreSQL / S3 and authenticating users with OAuth2 |
|`03-scaling-up`| Handling concurrent users with caching/pooling and adjusting the theme |
|`04-simple-retrieval`| Adding web retrieval capabilities for grounding answers |
|`05-file-based-rag-and-eval`| Ingesting files and setting up an evaluation pipeline |
|`06-observability-analytics`| Tracking user experience and understanding system performance |
|`07-cloud-deployment`| Deploying to AWS and managing cloud resources using Terraform
|`08-agentic-retrieval`| Giving the AI more tools and autonomy for problem solving |
|`09-file-upload`| Managing user uploads for chat and performing enhanced file parsing|
|`10-k8s-deployment`| Using Kubernetes for better scaling and resilience |
