---
title: english-to-latin
emoji: 🔥
colorFrom: pink
colorTo: purple
sdk: gradio
sdk_version: 4.24.0
app_file: app.py
pinned: false
---

### 🛰️ CICD to Huggingface Hub with Github Actions

This repo utlizes `github actions` to sync changes to huggingface hub. As pull requests merged to the main branch in this repo, changes will then be synced on huggingface hub. The [Gradio App published on huggingface space](https://huggingface.co/spaces/MenaWANG/english-to-latin) will then be updated automatically. 😎

## Troubleshooting notes

* ReadMe file setting for huggingface space: The huggingface space demands specific metadata in specific format at the top. This ReadMe has been revised to comply to the requirement. More on the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

* "No application file" error: The app returns this error at certain point and upon search, recreating `app.py` did fix the error (see [discussions here](Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference)).  

## Useful link: 

* Learned this from a Coursera course on MLOps tools: [link to the course](https://www.coursera.org/learn/mlops-mlflow-huggingface-duke)
* Original repo from the lecturer 🌹: https://github.com/nogibjj/hugging-face


