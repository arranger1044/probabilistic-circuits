---
layout: paper
ref: "friesen2018submodular"
title:  "Submodular Field Grammars: Representation Inference and Application to Image Parsing"
date:   2018-08-3 00:00
tags: pcs par-le cv map
image: ""
authors: "Friesen, Abram L. and Domingos, Pedro M."
pdf: "https://papers.nips.cc/paper/7684-submodular-field-grammars-representation-inference-and-application-to-image-parsing.pdf"
venue: "NeurIPS 2018"
abstract: "Natural scenes contain many layers of part-subpart structure, and distributions over them are thus naturally represented by stochastic image grammars, with one production per decomposition of a part. Unfortunately, in contrast to language grammars, where the number of possible split points for a production A→BC is linear in the length of A, in an image there are an exponential number of ways to split a region into subregions. This makes parsing intractable and requires image grammars to be severely restricted in practice, for example by allowing only rectangular regions. In this paper, we address this problem by associating with each production a submodular Markov random field whose labels are the subparts and whose labeling segments the current object into these subparts. We call the result a submodular field grammar (SFG). Finding the MAP split of a region into subregions is now tractable, and by exploiting this we develop an efficient approximate algorithm for MAP parsing of images with SFGs. Empirically, we present promising improvements in accuracy when using SFGs for scene understanding, and show exponential improvements in inference time compared to traditional methods, while returning comparable minima."
bibtex: "@inproceedings{friesen2018submodular,<br/>  author    = {Friesen, Abram L. and Domingos, Pedro M.},<br/>  title     = {Submodular Field Grammars: Representation Inference and Application<br/>               to Image Parsing},<br/>  booktitle = {NeurIPS},<br/>  pages     = {4312--4322},<br/>  year      = {2018}<br/>}"
---
