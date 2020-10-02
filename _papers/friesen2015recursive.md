---
layout: paper
ref: "friesen2015recursive"
title: "Recursive Decomposition for Nonconvex Optimization"
date: 2015-01-20 00:00
tags: spns the
image: ""
authors: "Friesen, Abram L. and Domingos, Pedro"
pdf: "https://arxiv.org/pdf/1611.02755"
venue: "IJCAI 2015"
abstract: "Continuous optimization is an important problem in many areas of AI, including vision, robotics, probabilistic inference, and machine learning. Unfortunately, most real-world optimization problems are nonconvex, causing standard convex techniques to find only local optima, even with extensions like random restarts and simulated annealing. We observe that, in many cases, the local modes of the objective function have combinatorial structure, and thus ideas from combinatorial optimization can be brought to bear. Based on this, we propose a problem-decomposition approach to nonconvex optimization. Similarly to DPLL-style SAT solvers and recursive conditioning in probabilistic inference, our algorithm, RDIS, recursively sets variables so as to simplify and decompose the objective function into approximately independent sub-functions, until the remaining functions are simple enough to be optimized by standard techniques like gradient descent. The variables to set are chosen by graph partitioning, ensuring decomposition whenever possible. We show analytically that RDIS can solve a broad class of nonconvex optimization problems exponentially faster than gradient descent with random restarts. Experimentally, RDIS outperforms standard techniques on problems like structure from motion and protein folding."
bibtex: "@article{friesen2016recursive, <br/>
  title={Recursive decomposition for nonconvex optimization}, <br/>
  author={Friesen, Abram L and Domingos, Pedro}, <br/>
  journal={arXiv preprint arXiv:1611.02755}, <br/>
  year={2016} <br/>
}"
---
