---
layout: paper
ref: "saad2021sppl"
title:  "SPPL: Probabilistic Programming With Fast Exact Symbolic Inference"
date:   2021-07-19 00:00
tags: ppl spns comp sw
image: ""
authors: "Saad, Feras A. and Rinard, Martin C. and Mansinghka, Vikash K."
pdf: "https://dl.acm.org/doi/pdf/10.1145/3453483.3454078"
code: "https://github.com/probcomp/sppl"
venue: "PLDI 2021"
abstract: "We present the Sum-Product Probabilistic Language (SPPL), a new probabilistic programming language that automatically delivers exact solutions to a broad range of probabilistic inference queries. SPPL translates probabilistic programs into sum-product expressions, a new symbolic representation and associated semantic domain that extends standard sum-product networks to support mixed-type distributions, numeric transformations, logical formulas, and pointwise and set-valued constraints. We formalize SPPL via a novel translation strategy from probabilistic programs to sum-product expressions and give sound exact algorithms for conditioning on and computing probabilities of events. SPPL imposes a collection of restrictions on probabilistic programs to ensure they can be translated into sum-product expressions, which allow the system to leverage new techniques for improving the scalability of translation and inference by automatically exploiting probabilistic structure. We implement a prototype of SPPL with a modular architecture and evaluate it on benchmarks the system targets, showing that it obtains up to 3500x speedups over state-of-the-art symbolic systems on tasks such as verifying the fairness of decision tree classifiers, smoothing hidden Markov models, conditioning transformed random variables, and computing rare event probabilities."
bibtex: "@inproceedings{saad2021sppl,<br/>
    title = {SPPL: Probabilistic Programming with Fast Exact Symbolic Inference},<br/>
    author = {Saad, Feras A. and Rinard, Martin C. and Mansinghka, Vikash K.},<br/>
    booktitle = {Proceedings of the 42nd ACM SIGPLAN International Conference on Programming Language Design and Implementation},<br/>
    pages = {804--819},<br/>
    numpages = {16},<br/>
    year = {2021},<br/>
    publisher = {Association for Computing Machinery},<br/>
    address = {New York, NY, USA},<br/>
    doi = {10.1145/3453483.3454078},<br/>
    isbn = {9781450383912},<br/>
    keywords = {probabilistic programming, symbolic execution},<br/>
    location = {Virtual, Canada},<br/>
}"
---
