---
layout: paper
ref: "amer2012sum"
title:  "Sum-Product Networks for Modeling Activities with Stochastic Structure"
date:   2012-02-10 00:00
tags: spns cv act
image: ""
authors: "Amer, Mohamed R. and Todorovic, Sinisa"
pdf: "http://web.engr.oregonstate.edu/~sinisa/research/publications/cvpr12_SPN.pdf"
venue: "CVPR 2012"
abstract: "This paper addresses recognition of human activities with stochastic structure, characterized by variable spacetime arrangements of primitive actions, and conducted by a variable number of actors. We demonstrate that modeling aggregate counts of visual words is surprisingly expressive enough for such a challenging recognition task. An activity is represented by a sum-product network (SPN). SPN is a mixture of bags-of-words (BoWs) with exponentially many mixture components, where subcomponents are reused by larger ones. SPN consists of terminal nodes representing BoWs, and product and sum nodes organized in a number of layers. The products are aimed at encoding particular configurations of primitive actions, and the sums serve to capture their alternative configurations. The connectivity of SPN and parameters of BoW distributions are learned under weak supervision using the EM algorithm. SPN inference amounts to parsing the SPN graph, which yields the most probable explanation (MPE) of the video in terms of activity detection and localization. SPN inference has linear complexity in the number of nodes, under fairly general conditions, enabling fast and scalable recognition. A new Volleyball dataset is compiled and annotated for evaluation. Our classification accuracy and localization precision and recall are superior to those of the state-of-the-art on the benchmark and our Volleyball datasets."
bibtex: "@inproceedings{amer2012sum, <br/>
  title={Sum-product networks for modeling activities with stochastic structure}, <br/>
  author={Amer, Mohamed R and Todorovic, Sinisa}, <br/>
  booktitle={2012 IEEE Conference on Computer Vision and Pattern Recognition}, <br/>
  pages={1314--1321}, <br/>
  year={2012}, <br/>
  organization={IEEE} <br/>
}"
---
