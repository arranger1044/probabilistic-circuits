---
layout: paper
ref: "rahman2019cutset"
title:  "Cutset Bayesian Networks: A New Representation for Learning Rao-Blackwellised Graphical Models"
date:   2019-08-9 00:00
tags: cnets par-le mar
image: ""
authors: "Rahman, Tahrima and Jin, Shasha and Gogate, Vibhav"
pdf: "https://www.ijcai.org/Proceedings/2019/0797.pdf"
venue: "IJCAI 2019"
abstract: "Recently there has been growing interest in learning probabilistic models that admit poly-time inference called tractable probabilistic models from data. Although they generalize poorly as compared to intractable models, they often yield more accurate estimates at prediction time. In this paper, we seek to further explore this trade-off between generalization performance and inference accuracy by proposing a novel, partially tractable representation called cutset Bayesian networks (CBNs). The main idea in CBNs is to partition the variables into two subsets X and Y,  learn a (intractable) Bayesian network that represents P(X) and a tractable con-ditional model that represents P(Y|X). The hopeis that the intractable model will help improve generalization while the tractable model, by leveraging Rao-Blackwellised sampling which combines exact inference and sampling, will help improve the prediction accuracy. To compactly model P(Y|X), we introduce a novel tractable representation called conditional cutset networks (CCNs) in which all conditional probability distributions are represented using calibrated classifiers—classifiers which typically yield higher quality probability estimates than conventional classifiers. We show via a rigorous experimental evaluation that CBNs and CCNs yield more accurate posterior estimates than their tractable as well as intractable counterparts."
bibtex: "@inproceedings{rahman2019cutset,<br/>  author    = {Rahman, Tahrima and Jin, Shasha and Gogate, Vibhav},<br/>  title     = {Cutset Bayesian Networks: {A} New Representation for Learning Rao-Blackwellised<br/>               Graphical Models},<br/>  booktitle = {{IJCAI}},<br/>  pages     = {5751--5757},<br/>  publisher = {ijcai.org},<br/>  year      = {2019}<br/>}"
---


