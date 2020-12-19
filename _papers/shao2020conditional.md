---
layout: paper
ref: "shao2020conditional"
title:  "Conditional Sum-Product Networks: Imposing Structure on Deep Probabilistic Architectures"
date:   2020-08-2 00:00
tags: spns par-le cv
image: ""
authors: "Shao, Xiaoting and Molina, Alejandro and Vergari, Antonio and Stelzner, Karl and Peharz, Robert and Liebig, Thomas and Kersting, Kristian"
pdf: "https://arxiv.org/pdf/1905.08550"
venue: "PGM 2020"
abstract: " Probabilistic graphical models are a central tool in AI; however, they are generally not as expressive as deep neural models, and inference is notoriously hard and slow. In contrast, deep probabilistic models such as sum-product networks (SPNs) capture joint distributions in a tractable fashion, but still lack the expressive power of intractable models based on deep neural networks. Therefore, we introduce conditional SPNs (CSPNs), conditional density estimators for multivariate and potentially hybrid domains which allow harnessing the expressive power of neural networks while still maintaining tractability guarantees. One way to implement CSPNs is to use an existing SPN structure and condition its parameters on the input, e.g., via a deep neural network. This approach, however, might misrepresent the conditional independence structure present in data. Consequently, we also develop a structure-learning approach that derives both the structure and parameters of CSPNs from data. Our experimental evidence demonstrates that CSPNs are competitive with other probabilistic models and yield superior performance on multilabel image classification compared to mean field and mixture density networks. Furthermore, they can successfully be employed as building blocks for structured probabilistic models, such as autoregressive image models."
bibtex: "@inproceedings{shao2020conditional,<br/>    author    = {Shao, Xiaoting and Molina, Alejandro and Vergari, Antonio and Stelzner, Karl and Peharz, Robert and Liebig, Thomas and Kersting, Kristian},<br/>  title     = {Conditional Sum-Product Networks: Imposing Structure on Deep Probabilistic<br/>               Architectures},<br/>  booktitle   = {PGM},<br/>  series    = {Proceedings of Machine Learning Research},<br/>  year      = {2020}<br/>}"
---
