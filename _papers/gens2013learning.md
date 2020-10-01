---
layout: paper
ref: "gens2013learning"
title:  "Learning the Structure of Sum-Product Networks"
date:   2013-05-10 00:00
tags: spns str-le
image: ""
authors: "Gens, Robert and Domingos, Pedro"
pdf: "http://www.jmlr.org/proceedings/papers/v28/gens13.pdf"
code: "http://spn.cs.washington.edu/learnspn/"
venue: "ICML 2013"
abstract: "Sum-product networks (SPNs) are a new class of deep probabilistic models. SPNs can have unbounded treewidth but inference in them is always tractable. An SPN is either a univariate distribution, a product of SPNs over disjoint variables, or a weighted sum of SPNs over the same variables.  We  propose the first algorithm for learning the structure of SPNs that takes full advantage of their expressiveness. At each step, the algorithm attempts to divide the current variables into approximately independent subsets. If successful, it returns the product of  recursive calls on the subsets; otherwise it returns the sum of recursive calls on subsets of  similar instances from the current training set. A comprehensive empirical study shows that the learned SPNs are typically comparable to graphical models in likelihood but superior in inference speed and accuracy."
bibtex: "@inproceedings{gens2013learning, <br/>
  title={Learning the structure of sum-product networks}, <br/>
  author={Gens, Robert and Pedro, Domingos}, <br/>
  booktitle={International conference on machine learning}, <br/>
  pages={873--880}, <br/>
  year={2013} <br/>
}"
---
