---
layout: paper
ref: "gens2012discriminative"
title: "Discriminative Learning of Sum-Product Networks"
date:   2012-08-10 00:00
tags: spns par-le cv
image: ""
authors: "Gens, Robert and Domingos, Pedro"
pdf: "http://papers.nips.cc/paper/4516-discriminative-learning-of-sum-product-networks.pdf"
venue: "NIPS 2012"
abstract: "Sum-product networks are a new deep architecture that can perform fast, exact inference on high-treewidth models. Only generative methods for training SPNs have been proposed to date. In this paper, we present the first discriminative training algorithms for SPNs, combining the high accuracy of the former with the representational power and tractability of the latter. We show that the class of tractable discriminative SPNs is broader than the class of tractable generative ones, and propose an efficient backpropagation-style algorithm for computing the gradient of the conditional log likelihood. Standard gradient descent suffers from the diffusion problem, but networks with many layers can be learned reliably using 'hard' gradient descent, where marginal inference is replaced by MPE inference (i.e., inferring the most probable state of the non-evidence variables). The resulting updates have a simple and intuitive form. We test discriminative SPNs on standard image classification tasks. We obtain the best results to date on the CIFAR-10 dataset, using fewer features than prior methods with an SPN architecture that learns local image structure discriminatively. We also report the highest published test accuracy on STL-10 even though we only use the labeled portion of the dataset."
bibtex: "@inproceedings{gens2012discriminative,
  title={Discriminative learning of sum-product networks},
  author={Gens, Robert and Domingos, Pedro},
  booktitle={Advances in Neural Information Processing Systems},
  pages={3239--3247},
  year={2012}
}"
---
