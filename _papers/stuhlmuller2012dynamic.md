---
layout: paper
ref: "stuhlmuller2012dynamic"
title:  "A Dynamic Programming Algorithm for Inference in Recursive Probabilistic Programs"
date:   2012-03-10 00:00
tags: spns comp ppl
image: ""
authors: "Stuhlmueller, Andreas and Goodman, Noah D."
pdf: "https://arxiv.org/pdf/1206.3555"
venue: "StarAI 2012"
abstract: "We describe a dynamic programming algorithm for computing the marginal distribution of discrete probabilistic programs. This algorithm takes a functional interpreter for an arbitrary probabilistic programming language and turns it into an efficient marginalizer. Because direct caching of sub-distributions is impossible in the presence of recursion, we build a graph of dependencies between sub-distributions. This factored sum-product network makes (potentially cyclic) dependencies between subproblems explicit, and corresponds to a system of equations for the marginal distribution. We solve these equations by fixed-point iteration in topological order. We illustrate this algorithm on examples used in teaching probabilistic models, computational cognitive science research, and game theory."
bibtex: "@article{stuhlmuller2012dynamic, <br/>
  title={A dynamic programming algorithm for inference in recursive probabilistic programs}, <br/>
  author={Stuhlm{\"u}ller, Andreas and Goodman, Noah D}, <br/>
  journal={Workshop of Statistical and Relational AI (StarAI)}, <br/>
  year={2012} <br/>
}"
---
