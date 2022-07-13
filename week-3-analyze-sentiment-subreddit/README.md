<p align = "center" draggable=”false” ><img src="https://user-images.githubusercontent.com/37101144/161836199-fdb0219d-0361-4988-bf26-48b0fad160a3.png"
     width="200px"
     height="auto"/>
</p>



# <h1 align="center" id="heading">Sentiment Analysis of Reddit Data using Reddit API</h1>

In this live coding session, we leverage the Python Reddit API Wrapper (`PRAW`) to retrieve data from subreddits on [Reddit](https://www.reddit.com), and perform sentiment analysis using [`pipelines`](https://huggingface.co/docs/transformers/main_classes/pipelines) from [HuggingFace ( 🤗 the GitHub of Machine Learning )](https://techcrunch.com/2022/05/09/hugging-face-reaches-2-billion-valuation-to-build-the-github-of-machine-learning/), powered by [transformer](https://arxiv.org/pdf/1706.03762.pdf).


## ☑️ Objectives
At the end of this session, you will be able to:
- [ ] Know how to work with APIs
- [ ] Feel more comfortable navigating thru documentation, even inspecting the source code
- [ ] Understand what a `pipeline` object is in HuggingFace
- [ ] perform sentiment analysis using `pipeline`
- [ ] Run a python script in command line and get the results
- [ ] Examine the quality of data
- [ ] Understand data lineage


## :hammer_and_wrench: Pre-Assignment

### Creating a Week 3 Repository
Let's get started by creating a Week 3 Repository!

<details>
  <summary>Creating your Week 3 Repository</summary>
  <br>

1. The first thing to do is create a new empty public repository!

![image](https://user-images.githubusercontent.com/19699016/176268864-0893db99-f496-4e0f-8860-fc635ec76106.png)

2. Be sure to fill out your repository name, description, and ensure it's public! NOTE: DO NOT ADD A README OR LICENSE

![image](https://user-images.githubusercontent.com/19699016/176269140-57baeb17-9e97-412b-bd9b-866dc7012e85.png)

3. Now that you've done the required set-up on GitHub.com, let's move to our terminal and clone the MLE-8 repository!

     ```console
     git clone git@github.com:FourthBrain/MLE-8.git
     ```

4. OPTIONAL: If you've already cloned the MLE-8 repository - feel free to pull the recent changes by `cd`ing into the directory that contains the MLE-8 repo, and running this command. Be sure to return to the parent directory before moving on! (`cd ..`)

     ```console
      git pull origin main
     ```

5. Now, we're going to copy the contents of the assignment to a new folder using the following command

     ```console
     cp -r MLE-8/assignments/week-3-analyze-sentiment-reddit .
     ```

6. Once that is complete, we'll `cd` into the newly created folder with

     ```console
     cd week-3-analyze-sentiment-reddit
     ```

7. Now, let's init our repository in this folder using

     ```console
     git init
     ```

8. We'll add the contents of the folder using

     ```console
     git add .
     ```

9. Let's create an initial commit!

     ```console
     git commit -m "Initial Commit"
     ```

10. Now we can add our created repository as a remote using the following command. Don't forget, you can get the SSH address from your repository by clicking the green `Code` button on GitHub.com!

     ```console
     git remote add main git@github.com:<YOUR GITHUB USERNAME>/<YOUR REPOSITORY NAME>
     ```

11. Now we'll set our branch to `main`

     ```console
     git branch -M main
     ```

12. Last, but not least, let's push the contents of our commit to our repo!

     ```console
     git push -u main main
     ```

13. That's it, that's all!

</details>

### Setting up your environment 🐍🖥️

Create a new Conda environment for sentiment anaylsis (sa). If you already have this environment, continue to the next step.
```console
  conda create -n sa python=3.8 jupyter -y
```
Activate your new environment
```console
  conda activate sa
```

Open the jupyter-notebook
```console
  jupyter-notebook
```

Navigate through the repo in the notebook to find `imports.ipynb` for this week and open it.

Run all of the cells in the notebook.


## Background
Please review the weekly narrative [here](https://www.notion.so/Week-3-Data-Centric-AI-in-the-Real-World-Weekly-Narrative-53f3bedb7e7b4994ad1227b8ad12bed6#9aad9d23be07405bb86d5ea9a9e0a6a5)
