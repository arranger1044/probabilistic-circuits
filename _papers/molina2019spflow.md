---
layout: paper
ref: "molina2019spflow"
title:  "SPFlow: An Easy and Extensible Library for Deep Probabilistic Learning using Sum-Product Networks"
date:   2019-08-1 00:00
tags: spns sw
image: ""
authors: "Molina, Alejandro and Vergari, Antonio and Stelzner, Karl and Peharz, Robert and Subramani, Pranav and Di Mauro, Nicola and Poupart, Pascal and Kersting, Kristian"
pdf: "https://arxiv.org/pdf/1901.03704"
venue: "arXiv 2019"
abstract: "We introduce SPFlow, an open-source Python library providing a simple interface to inference, learning and manipulation routines for deep and tractable probabilistic models called Sum-Product Networks (SPNs). The library allows one to quickly create SPNs both from data and through a domain specific language (DSL). It efficiently implements several probabilistic inference routines like computing marginals, conditionals and (approximate) most probable explanations (MPEs) along with sampling as well as utilities for serializing, plotting and structure statistics on an SPN. Moreover, many of the algorithms proposed in the literature to learn the structure and parameters of SPNs are readily available in SPFlow. Furthermore, SPFlow is extremely extensible and customizable, allowing users to promptly distill new inference and learning routines by injecting custom code into a lightweight functional-oriented API framework. This is achieved in SPFlow by keeping an internal Python representation of the graph structure that also enables practical compilation of an SPN into a TensorFlow graph, C, CUDA or FPGA custom code, significantly speeding-up computations."
bibtex: "@article{molina2019spflow:,<br/>  author    = {Molina, Alejandro and Vergari, Antonio and Stelzner, Karl and Peharz, Robert and Subramani, Pranav and Di Mauro, Nicola and Poupart, Pascal and Kersting, Kristian},<br/>  title     = {SPFlow: An Easy and Extensible Library for Deep Probabilistic Learning<br/>               using Sum-Product Networks},<br/>  journal   = {CoRR},<br/>  volume    = {abs/1901.03704},<br/>  year      = {2019}<br/>}"
---
