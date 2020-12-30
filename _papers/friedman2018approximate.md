---
layout: paper
ref: "friedman2018approximate"
title:  "Approximate Knowledge Compilation by Online Collapsed Importance Sampling"
date:   2018-08-28 00:00
tags: acs app comp
image: ""
authors: "Friedman, Tal and Van den Broeck, Guy"
pdf: "https://papers.nips.cc/paper/8026-approximate-knowledge-compilation-by-online-collapsed-importance-sampling.pdf"
venue: "NeurIPS 2018"
abstract: "We introduce collapsed compilation, a novel approximate inference algorithm for discrete probabilistic graphical models. It is a collapsed sampling algorithm that incrementally selects which variable to sample next based on the partial compila- tion obtained so far. This online collapsing, together with knowledge compilation inference on the remaining variables, naturally exploits local structure and context- specific independence in the distribution. These properties are used implicitly in exact inference, but are difficult to harness for approximate inference. More- over, by having a partially compiled circuit available during sampling, collapsed compilation has access to a highly effective proposal distribution for importance sampling. Our experimental evaluation shows that collapsed compilation performs well on standard benchmarks. In particular, when the amount of exact inference is equally limited, collapsed compilation is competitive with the state of the art, and outperforms it on several benchmarks."
bibtex: "@inproceedings{friedman2018approximate,<br/>  author    = {Friedman, Tal and Van den Broeck, Guy},<br/>  title     = {Approximate Knowledge Compilation by Online Collapsed Importance Sampling},<br/>  booktitle = {NeurIPS},<br/>  pages     = {8035--8045},<br/>  year      = {2018}<br/>}"
---
