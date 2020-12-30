---
layout: paper
ref: "vandenbroeck2020tractability"
title:  "On the Tractability of SHAP Explanations"
date:   2021-01-28 00:00
tags: pcs exp the
image: ""
authors: "Van den Broeck, Guy and Lykov, Anton and Schleich, Maximilian and Suciu, Dan"
pdf: "http://starai.cs.ucla.edu/papers/VdBAAAI21.pdf"
venue: "AAAI 2021"
abstract: "SHAP explanations are a popular feature-attribution mechanism for explainable AI. They use game-theoretic notions to measure the influence of individual features on the prediction of a machine learning model. Despite a lot of recent interest from both academia and industry, it is not known whether SHAP explanations of common machine learning models can be computed efficiently. In this paper, we establish the complexity of computing the SHAP explanation in three important settings. First, we consider fully-factorized data distributions, and show that the complexity of computing the SHAP explanation is the same as the complexity of computing the expected value of the model. This fully-factorized setting is often used to simplify the SHAP computation, yet our results show that the computation can be intractable for commonly used models such as logistic regression. Going beyond fully-factorized distributions, we show that computing SHAP explanations is already intractable for a very simple setting: computing SHAP explanations of trivial classifiers over naive Bayes distributions. Finally, we show that even computing SHAP over the empirical distribution is #P-hard."
bibtex: "@inproceedings{vandenbroeck2020tractability,<br/>  author    = {Van den Broeck, Guy and Lykov, Anton and Schleich, Maximilian and Suciu, Dan},<br/>  title     = {On the Tractability of {SHAP} Explanations},<br/>  booktitle   = {AAAI},<br/>   year      = {2021}<br/>}"
---
