---
layout: paper
ref: "zhao2017linear"
title:  "Linear Time Computation of Moments in Sum-Product Networks"
date:   2017-07-27 00:00
tags: spns par-le
image: ""
authors: "Zhao, Han and Gordon, Geoffrey J."
pdf: "https://papers.nips.cc/paper/2017/file/473447ac58e1cd7e96172575f48dca3b-Paper.pdf"
venue: "NIPS 2017"
abstract: "Bayesian online algorithms for Sum-Product Networks (SPNs) need to update their posterior distribution after seeing one single additional instance. To do so, they must compute moments of the model parameters under this distribution. The best existing method for computing such moments scales quadratically in the size of the SPN, although it scales linearly for trees. This unfortunate scaling makes Bayesian online algorithms prohibitively expensive, except for small or tree-structured SPNs. We propose an optimal linear-time algorithm that works even when the SPN is a general directed acyclic graph (DAG), which significantly broadens the applicability of Bayesian online algorithms for SPNs. There are three key ingredients in the design and analysis of our algorithm: 1). For each edge in the graph, we construct a linear time reduction from the moment computation problem to a joint inference problem in SPNs. 2). Using the property that each SPN computes a multilinear polynomial, we give an efficient procedure for polynomial evaluation by differentiation without expanding the network that may contain exponentially many monomials. 3). We propose a dynamic programming method to further reduce the computation of the moments of all the edges in the graph from quadratic to linear. We demonstrate the usefulness of our linear time algorithm by applying it to develop a linear time assume density filter (ADF) for SPNs."
bibtex: "@inproceedings{zhao2017linear,<br/>  author    = {Zhao, Han and Gordon, Geoffrey J.},<br/>  title     = {Linear Time Computation of Moments in Sum-Product Networks},<br/>  booktitle = {{NIPS}},<br/>  pages     = {6894--6903},<br/>  year      = {2017}<br/>}"
---
