<p align = "center" draggable=”false” ><img src="https://user-images.githubusercontent.com/37101144/161836199-fdb0219d-0361-4988-bf26-48b0fad160a3.png"
     width="200px"
     height="auto"/>
</p>

# <h1 align="center" id="heading">Electronics Purchase Prediction</h1>

Today you are a machine learning engineer in the Department of Marketing and Inventory at Walmart Labs. You have access to the Walmart server data, specifically the Electronics section. However, there is no customer facing information, but you do have access to timestamped data regarding product viewing/carting/purchasing. We will use this data to build a model of whether a not some product will be purchased.

Data is adapted from [e-commerce behavior data on Kaggle](https://www.kaggle.com/mkechinov/ecommerce-behavior-data-from-multi-category-store). 

This file contains behavior data from a large multi-category store. Each row in the file rerepresents an event. All events are related to products and users. Each event is like many-many relation between users and products. 

## ☑️ Objectives
At the end of this session, you will be able to
- Detect data imbalance
- Practice more on preprocessing features
- Build logistic regression / SVM / Gradient Boosting / Random Forest models
- Evaluate models with proper metrics
- Interpret black box models

## :hammer_and_wrench: Pre-Work
The requirements for this week are:
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `sklearn`
- `shap` (will be used for optional task)

You've encountered the first five packages from previous weeks. Installing `shap` following instructions [here](https://shap.readthedocs.io/en/latest/index.html)

In addition, for task "Analyze importance of data sample balancing using a Random Forest" to render the graph properly, it requires `Graphviz`. Check [Download](https://graphviz.org/download/) for installation information.

For MacOS, you can install these packages using the following command:
```
brew install graphviz # it can take a while
```

## Background
Please review the weekly narrative [here](https://www.notion.so/Week-6-Supervised-Machine-Learning-be220755e6f94fe78f3b97f7b1b4530e)
