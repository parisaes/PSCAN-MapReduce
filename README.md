# PSCAN Implementation in Python

This repository contains an implementation of PSCAN (A Parallel Structural Clustering Algorithm for Big Networks in MapReduce) in Python. PSCAN is a scalable clustering algorithm designed for large networks, leveraging the MapReduce framework for parallel processing.

## Overview
PSCAN is a parallel clustering algorithm designed for analyzing large networks. It efficiently detects communities, hubs, and outliers using structural similarity and density-based clustering, optimized for distributed processing systems.

## Features
- Calculates structural similarity for graph edges to identify relationships.
- Detects clusters, outliers, and hubs through density-based methods.
- Optimized for large-scale networks with reduced MapReduce job iterations, improving scalability.
- Parallelized execution using MapReduce to efficiently handle billions of edges.
- Modular Python implementation for easy adaptation and extension.

## Reference Paper
If you use this implementation in your research, please cite the original PSCAN paper:

Zhao, W., Martha, V., & Xu, X. (2013). Pscan: a parallel structural clustering algorithm for big networks in MapReduce. 2013 IEEE 27th International Conference on Advanced Information Networking and Applications (AINA), 862-869.

BibTeX citation:
```bibtex
@inproceedings{zhao2013pscan,
  title={Pscan: a parallel structural clustering algorithm for big networks in mapreduce},
  author={Zhao, Weizhong and Martha, Venkataswamy and Xu, Xiaowei},
  booktitle={2013 IEEE 27th International Conference on Advanced Information Networking and Applications (AINA)},
  pages={862--869},
  year={2013},
  organization={IEEE}
}
```
