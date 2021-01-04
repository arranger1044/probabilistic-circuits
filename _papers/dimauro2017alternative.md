---
layout: paper
ref: "dimauro2017alternative"
title:  "Alternative Variable Splitting Methods to Learn Sum-Product Networks"
date:   2017-08-7 00:00
tags: spns str-le
image: ""
authors: "Di Mauro, Nicola and Esposito, Floriana and Ventola, Fabrizio G. and Vergari, Antonio"
pdf: "https://www.researchgate.net/profile/Floriana_Esposito/publication/319504310_Alternative_Variable_Splitting_Methods_to_Learn_Sum-Product_Networks/links/59afcc050f7e9bf3c72920bb/Alternative-Variable-Splitting-Methods-to-Learn-Sum-Product-Networks.pdf"
venue: "AI*IA 2017"
code: "https://github.com/fabriziov/alt-vs-spyn"
abstract: "Sum-Product Networks (SPNs) are recent deep probabilistic models providing exact and tractable inference. SPNs have been successfully employed as density estimators in several application domains. However, learning an SPN from high dimensional data still poses a challenge in terms of time complexity. This is due to the high cost of determining independencies among random variables (RVs) and sub-populations among samples, two operations that are repeated several times. Even one of the simplest greedy structure learner, LearnSPN, scales quadratically in the number of the variables to determine RVs independencies. In this work we investigate approximate but fast procedures to determine independencies among RVs whose complexity scales in sub-quadratic time. We propose two procedures: a random subspace approach and one that adopts entropy as a criterion to split RVs in linear time. Experimental results prove that LearnSPN equipped by our splitting procedures is able to reduce learning and/or inference times while preserving comparable inference accuracy."
bibtex: "@inproceedings{dimauro2017alternative,<br/>  author    = {Di Mauro, Nicola and Esposito, Floriana and Ventola, Fabrizio G. and Vergari, Antonio},<br/>  title     = {Alternative Variable Splitting Methods to Learn Sum-Product Networks},<br/>  booktitle = {AI*IA},<br/>  series    = {Lecture Notes in Computer Science},<br/>  volume    = {10640},<br/>  pages     = {334--346},<br/>  publisher = {Springer},<br/>  year      = {2017}<br/>}"
---
