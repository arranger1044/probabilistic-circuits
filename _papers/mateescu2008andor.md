---
layout: paper
ref: "mateescu2008andor"
title:  "AND/OR Multi-Valued Decision Diagrams (AOMDDs) for Graphical Models"
date:   2008-08-2 00:00
tags: aogs comp
image: ""
authors: "Mateescu, Robert and Dechter, Rina and Marinescu, Radu"
pdf: "https://www.jair.org/index.php/jair/article/download/10579/25314"
venue: "J. Artif. Intell. Res. 2008"
abstract: "Inspired by the recently introduced framework of AND/OR search spaces for graphical models, we propose to augment Multi-Valued Decision Diagrams (MDD) with AND nodes, in order to capture function decomposition structure and to extend these compiled data structures to general weighted graphical models (e.g., probabilistic models). We present the AND/OR Multi-Valued Decision Diagram (AOMDD) which compiles a graphical model into a canonical form that supports polynomial (e.g., solution counting, belief updating) or constant time (e.g. equivalence of graphical models) queries. We provide two algorithms for compiling the AOMDD of a graphical model. The first is search-based, and works by applying reduction rules to the trace of the memory intensive AND/OR search algorithm. The second is inference-based and uses a Bucket Elimination schedule to combine the AOMDDs of the input functions via the the APPLY operator. For both algorithms, the compilation time and the size of the AOMDD are, in the worst case, exponential in the treewidth of the graphical model, rather than pathwidth as is known for ordered binary decision diagrams (OBDDs). We introduce the concept of semantic treewidth, which helps explain why the size of a decision diagram is often much smaller than the worst case bound. We provide an experimental evaluation that demonstrates the potential of AOMDDs."
bibtex: "@article{mateescu2008andor,<br/>  author    = {Mateescu, Robert and Dechter, Rina and Marinescu, Radu},<br/>  title     = {{AND/OR} Multi-Valued Decision Diagrams (AOMDDs) for Graphical Models},<br/>  journal   = {J. Artif. Intell. Res.},<br/>  volume    = {33},<br/>  pages     = {465--519},<br/>  year      = {2008}<br/>}"
---
