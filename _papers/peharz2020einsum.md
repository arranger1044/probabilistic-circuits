---
layout: paper
ref: "peharz2020einsum"
title:  "Einsum Networks: Fast and Scalable Learning of Tractable Probabilistic Circuits"
date:   2020-08-4 00:00
tags: pcs spns str-le par-le
image: ""
authors: "Peharz, Robert and Lang, Steven and Vergari, Antonio and Stelzner, Karl and Molina, Alejandro and Trapp, Martin and Van den Broeck, Guy and Kersting, Kristian and Ghahramani, Zoubin"
pdf: "https://arxiv.org/pdf/2004.06231"
venue: "ICML 2020"
abstract: "Probabilistic circuits (PCs) are a promising avenue for probabilistic modeling, as they permit a wide range of exact and efficient inference routines. Recent ``deep-learning-style'' implementations of PCs strive for a better scalability, but are still difficult to train on real-world data, due to their sparsely connected computational graphs. In this paper, we propose Einsum Networks (EiNets), a novel implementation design for PCs, improving prior art in several regards. At their core, EiNets combine a large number of arithmetic operations in a single monolithic einsum-operation, leading to speedups and memory savings of up to two orders of magnitude, in comparison to previous implementations. As an algorithmic contribution, we show that the implementation of Expectation-Maximization (EM) can be simplified for PCs, by leveraging automatic differentiation. Furthermore, we demonstrate that EiNets scale well to datasets which were previously out of reach, such as SVHN and CelebA, and that they can be used as faithful generative image models."
bibtex: "@inproceedings{peharz2020einsum,<br/>  author    = {Peharz, Robert and Lang, Steven and Vergari, Antonio and Stelzner, Karl and Molina, Alejandro and Trapp, Martin and Van den Broeck, Guy and Kersting, Kristian and Ghahramani, Zoubin},<br/>  title     = {Einsum Networks: Fast and Scalable Learning of Tractable Probabilistic<br/>               Circuits},<br/>  booktitle = {{ICML}},<br/>  series    = {Proceedings of Machine Learning Research},<br/>  volume    = {119},<br/>  pages     = {7563--7574},<br/>  publisher = {{PMLR}},<br/>  year      = {2020}<br/>}"
---
