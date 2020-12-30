---
layout: paper
ref: "lowd2008learning"
title:  "Learning Arithmetic Circuits"
date:   2008-08-28 00:00
tags: acs str-le
image: ""
authors: "Lowd, Daniel and Domingos, Pedro M."
pdf: "https://arxiv.org/pdf/1206.3271"
venue: "UAI 2008"
abstract: "Graphical models are usually learned without regard to the cost of doing inference with them. As a result, even if a good model is learned, it may perform poorly at prediction, because it requires approximate inference. We propose an alternative: learning models with a score function that directly penalizes the cost of inference. Specifically, we learn arithmetic circuits with a penalty on the number of edges in the circuit (in which the cost of inference is linear). Our algorithm is equivalent to learning a Bayesian network with context-specific independence by greedily splitting conditional distributions, at each step scoring the candidates by compiling the resulting network into an arithmetic circuit, and using its size as the penalty. We show how this can be done efficiently, without compiling a circuit from scratch for each candidate. Experiments on several real-world domains show that our algorithm is able to learn tractable models with very large treewidth, and yields more accurate predictions than a standard context-specific Bayesian network learner, in far less time."
bibtex: "@inproceedings{lowd2008learning,<br/>  author    = {Lowd, Daniel and Domingos, Pedro M.},<br/>  title     = {Learning Arithmetic Circuits},<br/>  booktitle = {{UAI}},<br/>  pages     = {383--392},<br/>  publisher = {{AUAI} Press},<br/>  year      = {2008}<br/>}"
---
