---
layout: paper
ref: "stelzner2019faster"
title:  "Faster Attend-Infer-Repeat with Tractable Probabilistic Models"
date:   2019-08-13 00:00
tags: spns cv
image: ""
authors: "Stelzner, Karl and Peharz, Robert and Kersting, Kristian"
pdf: "http://proceedings.mlr.press/v97/stelzner19a/stelzner19a.pdf"
venue: "ICML 2019"
abstract: "The recent Attend-Infer-Repeat (AIR) framework marks a milestone in structured probabilistic modeling, as it tackles the challenging problem of unsupervised scene understanding via Bayesian inference. AIR expresses the composition of visual scenes from individual objects, and uses variational autoencoders to model the appearance of those objects. However, inference in the overall model is highly intractable, which hampers its learning speed and makes it prone to suboptimal solutions. In this paper, we show that the speed and robustness of learning in AIR can be considerably improved by replacing the intractable object representations with tractable probabilistic models. In particular, we opt for sum-product networks (SPNs), expressive deep probabilistic models with a rich set of tractable inference routines. The resulting model, called SuPAIR, learns an order of magnitude faster than AIR, treats object occlusions in a consistent manner, and allows for the inclusion of a background noise model, improving the robustness of Bayesian scene understanding."
bibtex: "@inproceedings{stelzner2019faster,<br/>  author    = {Stelzner, Karl and Peharz, Robert and Kersting, Kristian},<br/>  title     = {Faster Attend-Infer-Repeat with Tractable Probabilistic Models},<br/>  booktitle = {{ICML}},<br/>  series    = {Proceedings of Machine Learning Research},<br/>  volume    = {97},<br/>  pages     = {5966--5975},<br/>  publisher = {{PMLR}},<br/>  year      = {2019}<br/>}"
---
