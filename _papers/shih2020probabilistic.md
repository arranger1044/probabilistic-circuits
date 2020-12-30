---
layout: paper
ref: "shih2020probabilistic"
title:  "Probabilistic Circuits for Variational Inference in Discrete Graphical Models"
date:   2020-08-28 00:00
tags: spns app
image: ""
authors: "Shih, Andy and Ermon, Stefano"
pdf: "https://papers.nips.cc/paper/2020/file/31784d9fc1fa0d25d04eae50ac9bf787-Paper.pdf"
venue: "NeurIPS 2020"
abstract: "Inference in discrete graphical models with variational methods is difficult because of the inability to re-parameterize gradients of the Evidence Lower Bound (ELBO). Many sampling-based methods have been proposed for estimating these gradients, but they suffer from high bias or variance. In this paper, we propose a new approach that leverages the tractability of probabilistic circuit models, such as Sum Product Networks (SPN), to compute ELBO gradients exactly (without sampling) for a certain class of densities. In particular, we show that selective-SPNs are suitable as an expressive variational distribution, and prove that when the log-density of the target model is a polynomial the corresponding ELBO can be computed analytically. To scale to graphical models with thousands of variables, we develop an efficient and effective construction of selective-SPNs with size O(kn), where n is the number of variables and k is an adjustable hyperparameter. We demonstrate our approach on three types of graphical models -- Ising models, Latent Dirichlet Allocation, and factor graphs from the UAI Inference Competition. Selective-SPNs give a better lower bound than mean-field and structured mean-field, and is competitive with approximations that do not provide a lower bound, such as Loopy Belief Propagation and Tree-Reweighted Belief Propagation. Our results show that probabilistic circuits are promising tools for variational inference in discrete graphical models as they combine tractability and expressivity."
bibtex: "@inproceedings{shih2020probabilistic,<br/>  author    = {Shih, Andy and Ermon, Stefano},<br/>  title     = {Probabilistic Circuits for Variational Inference in Discrete Graphical<br/>               Models},<br/>  booktitle = {NeurIPS},<br/>  year      = {2020}<br/>}"
---
