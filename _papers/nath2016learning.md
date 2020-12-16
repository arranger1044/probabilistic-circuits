---
layout: paper
ref: "nath2016learning"
title:  "Learning Tractable Probabilistic Models for Fault Localization"
date:   2016-06-11 00:00
tags: spns misc
image: ""
authors: "Nath, Aniruddh and Domingos, Pedro"
pdf: "http://homes.cs.washington.edu/~pedrod/papers/aaai16.pdf"
venue: "AAAI 2016"
abstract: "In recent years, several probabilistic techniques have been applied to various debugging problems. However, most existing probabilistic debugging systems use relatively simple statistical models, and fail to generalize across multiple programs. In this work, we propose Tractable Fault Localization Models (TFLMs) that can be learned from data, and probabilistically infer the location of the bug. While most previous statistical debugging methods generalize over many executions of a single program, TFLMs are trained on a corpus of previously seen buggy programs, and learn to identify recurring patterns of bugs. Widely-used fault localization techniques such as TARANTULA evaluate the suspiciousness of each line in isolation; in contrast, a TFLM defines a joint probability distribution over buggy indicator variables for each line. Joint distributions with rich dependency structure are often computationally intractable; TFLMs avoid this by exploiting recent developments in tractable probabilistic models (specifically, Relational SPNs). Further, TFLMs can incorporate additional sources of information, including coverage-based features such as TARANTULA. We evaluate the fault localization performance of TFLMs that include TARANTULA scores as features in the probabilistic model. Our study shows that the learned TFLMs isolate bugs more effectively than previous statistical methods or using TARANTULA directly."
bibtex: "@inproceedings{nath2016learning, <br/>
  title={Learning Tractable Probabilistic Models for Fault Localization}, <br/>
  author={Nath, Aniruddh and Domingos, Pedro M}, <br/>
  booktitle={Thirtieth AAAI Conference on Artificial Intelligence}, <br/>
  year={2016} <br/>
}"
---
