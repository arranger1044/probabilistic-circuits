---
layout: paper
ref: "butz2018empirical"
title:  "An Empirical Study of Methods for SPN Learning and Inference"
date:   2018-08-6 00:00
tags: spns str-le
image: ""
authors: "Butz, Cory J. and de S. Oliveira, Jhonatan and dos Santos, Andre E. and Teixeira, Andre L. and Poupart, Pascal and Kalra, Agastya"
pdf: "http://proceedings.mlr.press/v72/butz18a/butz18a.pdf"
venue: "PGM 2018"
abstract: "In this study, we provide an empirical comparison of methods for \emph{sum-product network} (SPN) learning and inference. LearnSPN is a popular algorithm for learning SPNs that utilizes chop and slice operations. As \emph{g-test} is a standard chopping method and \emph{Gaussian mixture models} (GMM) using expectation-maximization is a common slicing method, it seems to have been assumed in the literature that this is the best pair in LearnSPN. On the contrary, our results show that g-test for chopping and \emph{k-means} for slicing yields SPNs that are just as accurate. Moreover, it has been shown that implementing SPN leaf nodes as \emph{Chow-Liu Trees} (CLTs) yields more accurate SPNs for the former pair. Our experiments show the same for the latter pair, and that neither pair dominates the other. Lastly, we report an analysis of SPN topology for unstudied pairs. With respect to inference, we derive \emph{partial propagation} (PP), which performs SPN exact inference without requiring a full propagation over all nodes in the SPN as currently done. Experimental results on SPN datasets demonstrate that PP has several advantages over full propagation in SPNs, including relative time savings, absolute time savings in large SPNs, and scalability."
bibtex: "@inproceedings{butz2018empirical,<br/>  author    = {Butz, Cory J. and de S. Oliveira, Jhonatan and dos Santos, Andr{'{e}} E. and Teixeira, Andr{'{e}} L. and Poupart, Pascal and Kalra, Agastya},<br/>  title     = {An Empirical Study of Methods for {SPN} Learning and Inference},<br/>  booktitle = {{PGM}},<br/>  series    = {Proceedings of Machine Learning Research},<br/>  volume    = {72},<br/>  pages     = {49--60},<br/>  publisher = {{PMLR}},<br/>  year      = {2018}<br/>}"
---
