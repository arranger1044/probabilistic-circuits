# Probabilistic Circuits

This repo contains the source code for the website [https://arranger1044.github.io/probabilistic-circuits/](https://arranger1044.github.io/probabilistic-circuits/) which is a curated and reasoned list of papers on probabilistic circuits (PCs), computational graphs encoding tractable probability distributions.

## License

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

All the material in this repo is released to the Public Domain. Feel free to clone, fork or  complete and/or correct any of these lists. 

## How to contribute


To add, change or remove a paper on the website, please open a [pull request](https://github.com/arranger1044/probabilistic-circuits/pulls)!

This site harness Jekyll templates in github pages and their file-based model view. Each paper in the website is associated a markdown file under the `_papers` folder. Modifications to the key-value pairs in this single file would be reflected to the whole website.

Mandatory keys in a paper description are:
  - `layout` to be left to `paper`
  - `ref` a string acting as a unique identifier
  - `title` the complete paper title
  - `date` intended as a publication date (only the year matters)
  - `tags` a space-separated sequence of tags to classify the paper (see below)
  - `authors` a string with authors names, separated by comma
  - `venue` the publication venue (conference, journal name)
  
Optional keys are:
  - `pdf` a link to a publicly readable version of the paper
  - `code` link to the code released with the paper
  - `abstract` the paper abstract, as a single string
  - `bibtex` a string for the bibtex entry
  

The script `dblp_to_md.py` is a quick and dirt way to generate a skeleton of a markdown file entry from the condensed bibtex as available from [DBLP](https://dblp.org/) 

### Available tags

Papers on PCs can be catalogued according to the following tags.

Models:
  - `acs`: Arithmetic circuits
  - `cnets`: Cutset networks
  - `spns`: Sum-Product networks
  - `aogs`: And/Or graphs
  - `pdgs`: Probabilistic decision graphs
  - `psdds`: Probabilistic sentential decision diagrams
  - `pcs`: Other probabilistic circuits
  
Algorithms: 
  - `str-le`: Structure learning
  - `par-le`: Parameter learning
  - `comp`: Compilation
  
Inference: 
  - `mar`: Marginal inference
  - `map`: MAP inference
  - `mmap`: Marginal MAP inference
  - `div`: Divergences, IPMs
  - `exp`: Expectations
  - `mom`: Moments
  - `sam`: Sampling
  - `app`: Approximate inference
  - `imp`: Imprecise probabilities
  
Applications: 
  - `cv`: Computer vision
  - `nlp`: Natural language processing
  - `seg`: Semantic segmentation
  - `act`: Activity recognition
  - `spe`: Speech recognition and reconstruction
  - `rob`: Robotics
  - `bio`: Computational biology
  - `the`: Theory
  - `ppl`: Probabilistic Programming
  - `rep`: Representation Learning
  - `hw`: Hardware
  - `sw`: Software
  - `xai`: Explanations
  - `misc`: Other applications

## Thanks

Special thanks to [Giuseppe Lobraico](https://github.com/your) who taught me how to deal with the ruby stack behind Jekyll.
