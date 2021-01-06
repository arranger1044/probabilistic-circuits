---
layout: paper
ref: "arenas2021tractabilitySHAP"
title:  "The Tractability of SHAP-Score-Based Explanations over Deterministic and Decomposable Boolean Circuits"
date:   2021-02-02 00:00
tags: pcs exp the
image: ""
authors: "Arenas, Marcelo and Bertossi, Pablo Barcelo Leopoldo and Monet, Mikael"
pdf: "https://arxiv.org/abs/2007.14045"
venue: "AAAI 2021"
abstract: "Scores based on Shapley values are widely used for providing explanations to classification results over machine learning models. A prime example of this is the influential SHAP-score, a version of the Shapley value that can help explain the result of a learned model on a specific entity by assigning a score to every feature. While in general computing Shapley values is a computationally intractable problem, it has recently been claimed that the SHAP-score can be computed in polynomial time over the class of decision trees. In this paper, we provide a proof of a stronger result over Boolean models: the SHAP-score can be computed in polynomial time over deterministic and decomposable Boolean circuits. Such circuits, also known as tractable Boolean circuits, generalize a wide range of Boolean circuits and binary decision diagrams classes, including binary decision trees, Ordered Binary Decision Diagrams (OBDDs) and Free Binary Decision Diagrams (FBDDs). We also establish the computational limits of the notion of SHAP-score by observing that, under a mild condition, computing it over a class of Boolean models is always polynomially as hard as the model counting problem for that class. This implies that both determinism and decomposability are essential properties for the circuits that we consider, as removing one or the other renders the problem of computing the SHAP-score intractable (namely, #P-hard)."
bibtex: "@inproceedings{arenas2020tractability,<br/>  author={Arenas, Marcelo and Bertossi, Pablo Barcel{\'o} Leopoldo and Monet, Mika{\"e}l},<br/>  title     = {The Tractability of SHAP-scores over Deterministic and Decomposable Boolean Circuits<br/>               Maps},<br/>  booktitle = {{AAAI}},<br/>  pages     = {4547--4555},<br/>  publisher = {{AAAI} Press},<br/>  year      = {2021}<br/>}"
---
