---
layout: paper
ref: "trapp2020thesis"
title:  "Sum-Product Networks for Complex Modelling Scenarios"
date:   2020-12-10 00:00
tags: spns
image: ""
authors: "Trapp, Martin"
venue: "Thesis"
abstract: "Sum-Product Networks (SPNs) are flexible general-purpose probabilistic models that have received increasing attention due to their attractive inference properties. Even though there exists a large body of work on parameter and structure learning in SPNs, many of the existing approaches focus on rather simple modelling scenarios. For example, in the case of discriminative parameter learning, the labelled training examples are assumed to be abundant, and we generally consider SPNs to be defined only over a finite set of random variables. Moreover, most approaches to construct SPNs in a data-agnostic way rely on heuristic and ad-hoc strategies rather than proposing a principled solution.
In this thesis, we examine SPNs for complex modelling scenarios. We are particularly interested in: i) principled semi-supervised parameter learning in SPNs, which guarantees that the learner cannot deteriorate in performance when adding additional unlabelled data, ii) principled structure learning in SPNs that is mathematically sound, protects us from overfitting and enables learning under missing data, and iii) extending the framework of SPNs to model possibly infinitely many random variables, and thus, establishing SPNs as a stochastic process model.
As a first main contribution, we introduce an extension of the contrastive pessimistic likelihood for safe semi-supervised parameter learning in SPNs. Our approach is the first semi- supervised learning technique for SPNs, and often obtains a performance that is similar to an SPN trained on a fully labelled datasets. We first derive an objective for generative learning and later extend the approach to discriminative parameter learning. Lastly, we show empirical evidence that safe semi-supervised SPNs perform favourably compared to existing semi-supervised techniques on various classification tasks.
The second main contribution of this thesis is the introduction of principled structure learning in SPNs. While there exists a large body of work on structure learning, none of the approaches asks either of the two essential questions: “What is a good structure?” or “What is a principle to derive a good structure?”. We aim to change this practice and introduce a sound, Bayesian formulation for joint parameter and structure learning in SPNs. Our experiments show that this principled approach competes well with the prior art and that we gain several benefits, such as automatic protection against overfitting, robustness under missing data and a natural extension to nonparametric formulations.
As a third main contribution, we introduce deep structured mixtures of Gaussian processes, which combine tractable inference in SPNs with exact posterior inference in Gaussian processes. Our approach directly extends SPNs to the stochastic process case by equipping SPNs with Gaussian measures, which correspond to Gaussian processes, as leaves. We show that the resulting model allows a natural interpretation as exact Bayesian model averaging over a rich collection of naive-local expert models. In a series of experiments, we show that the proposed technique outperforms existing expert-based approaches and provides low approximation errors when used as an approximation to a Gaussian process.
In addition to the main contributions, we show that gradient-based optimisation in overparameterised SPNs results in intrinsic acceleration effects, which depend directly on the depth of the network. Furthermore, we introduce two formulations for nonparametric SPNs and discuss their advantages and limitations."
bibtex: "@phdthesis{trapp2020thesis, <br/>
  title={Sum-Product Networks for Complex Modelling Scenarios}, <br/>
  author={Trapp, Martin}, <br/>
  year={2020}, <br/>
  school={PhD thesis, Graz University of Technology} <br/>
}"
---
