---
layout: paper
ref: "trapp2019bayesian"
title:  "Bayesian Learning of Sum-Product Networks"
date:   2019-08-20 00:00
tags: spns str-le
image: ""
authors: "Trapp, Martin and Peharz, Robert and Ge, Hong and Pernkopf, Franz and Ghahramani, Zoubin"
pdf: "https://papers.nips.cc/paper/8864-bayesian-learning-of-sum-product-networks.pdf"
venue: "NeurIPS 2019"
abstract: "Sum-product networks (SPNs) are flexible density estimators and have received significant attention due to their attractive inference properties. While parameter learning in SPNs is well developed, structure learning leaves something to be desired: Even though there is a plethora of SPN structure learners, most of them are somewhat ad-hoc and based on intuition rather than a clear learning principle. In this paper, we introduce a well-principled Bayesian framework for SPN structure learning. First, we decompose the problem into i) laying out a computational graph, and ii) learning the so-called scope function over the graph. The first is rather unproblematic and akin to neural network architecture validation. The second represents the effective structure of the SPN and needs to respect the usual structural constraints in SPN, i.e. completeness and decomposability. While representing and learning the scope function is somewhat involved in general, in this paper, we propose a natural parametrisation for an important and widely used special case of SPNs. These structural parameters are incorporated into a Bayesian model, such that simultaneous structure and parameter learning is cast into monolithic Bayesian posterior inference. In various experiments, our Bayesian SPNs often improve test likelihoods over greedy SPN learners. Further, since the Bayesian framework protects against overfitting, we can evaluate hyper-parameters directly on the Bayesian model score, waiving the need for a separate validation set, which is especially beneficial in low data regimes. Bayesian SPNs can be applied to heterogeneous domains and can easily be extended to nonparametric formulations. Moreover, our Bayesian approach is the first, which consistently and robustly learns SPN structures under missing data."
bibtex: "@inproceedings{trapp2019bayesian,<br/>  author    = {Trapp, Martin and Peharz, Robert and Ge, Hong and Pernkopf, Franz and Ghahramani, Zoubin},<br/>  title     = {Bayesian Learning of Sum-Product Networks},<br/>  booktitle = {NeurIPS},<br/>  pages     = {6344--6355},<br/>  year      = {2019}<br/>}"
---
