---
layout: paper
ref: "choi2021group"
title:  "Group Fairness by Probabilistic Modeling with Latent Fair Decisions"
date:   2021-01-28 00:00
tags: pcs mar misc
image: ""
authors: "Choi, YooJung and Dang, Meihua and Van den Broeck, Guy"
pdf: "https://arxiv.org/pdf/2009.09031"
venue: "AAAI 2021"
abstract: "Machine learning systems are increasingly being used to make impactful decisions such as loan applications and criminal justice risk assessments, and as such, ensuring fairness of these systems is critical. This is often challenging as the labels in the data are biased. This paper studies learning fair probability distributions from biased data by explicitly modeling a latent variable that represents a hidden, unbiased label. In particular, we aim to achieve demographic parity by enforcing certain independencies in the learned model. We also show that group fairness guarantees are meaningful only if the distribution used to provide those guarantees indeed captures the real-world data. In order to closely model the data distribution, we employ probabilistic circuits, an expressive and tractable probabilistic model, and propose an algorithm to learn them from incomplete data. We evaluate our approach on a synthetic dataset in which observed labels indeed come from fair labels but with added bias, and demonstrate that the fair labels are successfully retrieved. Moreover, we show on real-world datasets that our approach not only is a better model than existing methods of how the data was generated but also achieves competitive accuracy."
bibtex: "@inproceedings{choi2020group,<br/>  author    = {Choi, YooJung and Dang, Meihua and Van den Broeck, Guy},<br/>  title     = {Group Fairness by Probabilistic Modeling with Latent Fair Decisions},<br/>  booktitle   = {AAAI},<br/>  year      = {2020}<br/>}"
---
