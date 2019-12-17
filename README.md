# GCP CI/CD

## This is project is under active development
This WIP projecr for developing an understanding of GCP build and deploy. PRs are not solicited at this time.

## Scope
The overall objective of this project is to deploy a TensorFlow BERT NLP model and a Flask app that exposes a UI that allows interaction with it. Implement [Cloud Build](https://ordina-jworks.github.io/cloud/2019/03/28/Building-With-Google-Cloud-Build.html) for CI/CD.

## Will support the following use cases:
- Use GPC Cloud Build for continuous integration.
- Use GOC Cloud Run for continuous deployment on pushes to master.
- Fail build on push to any branch if all cells in a notebook don't run successfully.
- Tests that fail will cause the Cloud Build step to fail.
- On successful build after push to master archive an existing notebook version and deploy the new version.
- If a notebook trains a deep learning model, a parameter will be passes that triggers model training. Without the trigger the training step will be skipped.
- If model training on a GPU is required, an instance will be spun up to run the training job then shut down after training has completed.

## Components:
- GCP [Cloud Build](https://ordina-jworks.github.io/cloud/2019/03/28/Building-With-Google-Cloud-Build.html)
- GPC Cloud Run
- TensorFlow V2
- [Transformers](https://medium.com/tensorflow/using-tensorflow-2-for-state-of-the-art-natural-language-processing-102445cda54a) to support BERT with the current version on TensorFlow V2

## Setup
- [x] Create GCP project `gdb-gcp-cicd
- [x] Create VM instance
- [x] Enable CloudBuild on GitHub
- [ ] Create virtual environment
- [ ] Create `requirements.txt` and add intitial packages
- [ ] Create `cloudbuild.yaml`
- [ ] Add "push to any branch" trigger on Cloud Build
- [ ] Run Jupyter Notebook on VM
- [ ] Run 
- [ ] Set up least-priviledge deployment for Cloud Build
- [ ] Create Service on [Cloud Run](https://console.cloud.google.com/marketplace/details/google-cloud-platform/cloud-run)
- [ ] Create continuous deployment service on Cloud Run. See "Continuous deployment with minimal IAM permissions" on [this page](https://cloud.google.com/run/docs/continuous-deployment-with-cloud-build?_ga=2.84679130.-275958949.1574294967).

## Sub-Projects
We'll step through some of the tutorials offered on the GCP site.

### [Hello World - App Engine](https://console.cloud.google.com/home/dashboard?project=gdb-gcp-cicd&folder=&organizationId=&walkthrough_tutorial_id=go_gae_quickstart)
