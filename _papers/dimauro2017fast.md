---
layout: paper
ref: "dimauro2017fast"
title:  "Fast and Accurate Density Estimation with Extremely Randomized Cutset Networks"
date:   2017-08-11 00:00
tags: cnets str-le
image: ""
authors: "Di Mauro, Nicola and Vergari, Antonio and Basile, Teresa Maria Altomare and Esposito, Floriana"
pdf: "https://www.researchgate.net/profile/Floriana_Esposito/publication/322126866_Fast_and_Accurate_Density_Estimation_with_Extremely_Randomized_Cutset_Networks/links/5afd614a458515e9a5acc857/Fast-and-Accurate-Density-Estimation-with-Extremely-Randomized-Cutset-Networks.pdf"
venue: "ECML/PKDD 2017"
abstract: "Cutset Networks (CNets) are density estimators leveraging context-specific independencies recently introduced to provide exact inference in polynomial time. Learning a CNet is done by firstly building a weighted probabilistic OR tree and then estimating tractable distributions as its leaves. Specifically, selecting an optimal OR split node requires cubic time in the number of the data features, and even approximate heuristics still scale in quadratic time. We introduce Extremely Randomized Cutset Networks (XCNets), CNets whose OR tree is learned by performing random conditioning. This simple yet surprisingly effective approach reduces the complexity of OR node selection to constant time. While the likelihood of an XCNet is slightly worse than an optimally learned CNet, ensembles of XCNets outperform state-of-the-art density estimators on a series of standard benchmark datasets, yet employing only a fraction of the time needed to learn the competitors. Code and data related to this chapter are available at: https://github.com/nicoladimauro/cnet."
code: "https://github.com/nicoladimauro/cnet"
bibtex: "@inproceedings{dimauro2017fast,<br/>  author    = {Di Mauro, Nicola and Vergari, Antonio and Maria Altomare Basile, Teresa and Esposito, Floriana},<br/>  title     = {Fast and Accurate Density Estimation with Extremely Randomized Cutset<br/>               Networks},<br/>  booktitle = {{ECML/PKDD} {(1)}},<br/>  series    = {Lecture Notes in Computer Science},<br/>  volume    = {10534},<br/>  pages     = {203--219},<br/>  publisher = {Springer},<br/>  year      = {2017}<br/>}"
---
