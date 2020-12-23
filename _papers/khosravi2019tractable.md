---
layout: paper
ref: "khosravi2019tractable"
title:  "On Tractable Computation of Expected Predictions"
date:   2019-08-30 00:00
tags: pcs exp xai
image: ""
authors: "Khosravi, Pasha and Choi, YooJung and Liang, Yitao and Vergari, Antonio and Van den Broeck, Guy"
pdf: "https://papers.nips.cc/paper/9296-on-tractable-computation-of-expected-predictions.pdf"
venue: "NeurIPS 2019"
abstract: "Computing expected predictions of discriminative models is a fundamental task in machine learning that appears in many interesting applications such as fairness, handling missing values, and data analysis. Unfortunately, computing expectations of a discriminative model with respect to a probability distribution defined by an arbitrary generative model has been proven to be hard in general. In fact, the task is intractable even for simple models such as logistic regression and a naive Bayes distribution. In this paper, we identify a pair of generative and discriminative models that enables tractable computation of expectations, as well as moments of any order, of the latter with respect to the former in case of regression. Specifically, we consider expressive probabilistic circuits with certain structural constraints that support tractable probabilistic inference. Moreover, we exploit the tractable computation of high-order moments to derive an algorithm to approximate the expectations for classification scenarios in which exact computations are intractable. Our framework to compute expected predictions allows for handling of missing data during prediction time in a principled and accurate way and enables reasoning about the behavior of discriminative models. We empirically show our algorithm to consistently outperform standard imputation techniques on a variety of datasets. Finally, we illustrate how our framework can be used for exploratory data analysis."
bibtex: "@inproceedings{khosravi2019tractable,<br/>  author    = {Khosravi, Pasha and Choi, YooJung and Liang, Yitao and Vergari, Antonio and Van den Broeck, Guy},<br/>  title     = {On Tractable Computation of Expected Predictions},<br/>  booktitle = {NeurIPS},<br/>  pages     = {11167--11178},<br/>  year      = {2019}<br/>}"
---
