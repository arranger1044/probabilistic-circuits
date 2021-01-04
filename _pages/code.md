---
layout: code
title: code
permalink: /code
order: 5
---

## Software Libraries

- [**Juice.jl**](https://github.com/Juice-jl/ProbabilisticCircuits.jl) a `Julia` package for logical and probabilistic circuits with fast `CUDA` bindings 
- [**SPFlow**](https://github.com/SPFlow/SPFlow) an easy and extensible `python` library for <a href="models#spns">SPNs</a> compiling them to `pytorch`, `tensorflows` and `C` code
- [**LibSPN**](http://www.libspn.org/) tensorflow implementation of <a href="models#spns">SPNs</a> with bindings in `python`
- [**Libra Toolkit**](http://libra.cs.uoregon.edu/) Learning and inference routines
     for <a href="models#acs">ACs</a> implemented in `Ocaml`
-  [**BayesianSumProductNetworks.jl**](https://github.com/trappmartin/BayesianSumProductNetworks) Julia implementation of Bayesian structure and parameter learning. 
- [**SumProductNetworks.jl**](https://github.com/trappmartin/SumProductNetworks.jl) Software package for SPNs. `julia`
-  [**Tachyon**](https://github.com/KalraA/Tachyon) structure and parameter learning in `python3`
- [**GoSPN**](https://github.com/RenatoGeh/gospn) implementing LearnSPN in Go `Go` 
     

<br/>
## Papers with code

{% assign sorted = site.papers | where_exp: "p", "p.code" | sort: 'date' | reverse %}
<ul class="paper-list">
{% for p in sorted %}
   <li>
       {% include paper.html paper=p %}
   </li>
{% endfor %}
</ul>
