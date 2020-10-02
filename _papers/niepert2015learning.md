---
layout: paper
ref: "niepert2015learning"
title: "Learning and Inference in Tractable Probabilistic Knowledge Bases"
date: 2015-07-20 00:00
tags: spns str-le the
image: ""
authors: "Niepert, Mathias and Domingos, Pedro"
pdf: "https://homes.cs.washington.edu/~pedrod/papers/uai15.pdf"
venue: "UAI 2015"
abstract: "Building efficient large-scale knowledge bases (KBs) is a longstanding goal of AI. KBs need to be first-order to be sufficiently expressive, and probabilistic to handle uncertainty, but these lead to intractable inference. Recently, tractable Markov logic (TML) was proposed as a non-trivial tractable first-order probabilistic representation. This paper describes the first inference and learning algorithms for TML, and its application to real-world problems. Inference takes time per query sublinear in the size of the KB, and supports very large KBs via parallelization and a disk-based implementation using a relational database engine. Query answering is fast enough for interactive and real-time use. We show that, despite the data being non-i.i.d. in general, maximum likelihood parameters for TML knowledge bases can be computed in closed form. We use our algorithms to build a very large tractable probabilistic KB from numerous heterogeneous data sets. The KB includes millions of objects and billions of parameters. Our experiments show that the learned KB outperforms existing specialized approaches on challenging tasks in information extraction and integration."
bibtex: "@inproceedings{niepert2015learning, <br/>
  title={Learning and Inference in Tractable Probabilistic Knowledge Bases.}, <br/>
  author={Niepert, Mathias and Domingos, Pedro M}, <br/>
  booktitle={UAI}, <br/>
  pages={632--641}, <br/>
  year={2015} <br/>
}"
---
