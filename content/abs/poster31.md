---
title: "The ground truth about metadata and community detection in networks"
---

# The ground truth about metadata and community detection in networks

Leto Peel<sup>1</sup>, Daniel B. Larremore<sup>2</sup>, Aaron Clauset<sup>3</sup>

- <sup>1</sup> Université Catholique de Louvain
- <sup>2</sup> Santa Fe Institute, New Mexico
- <sup>3</sup> University of Colorado, Colorado

Across many scientific domains, there is common need to automatically extract a simplified view
or a coarse-graining of how a complex system’s components interact. This general task is called
community detection in networks and is analogous to searching for clusters in independent vector
data. It is common to evaluate the performance of community detection algorithms by their ability
to find so-called ground truth communities. This works well in synthetic networks with planted
communities because such networks’ links are formed explicitly based on the planted communities.
However, there are no planted communities in real world networks. Instead, it is standard practice
to treat some observed discrete-valued node attributes, or metadata, as ground truth. Here, we show
that metadata are not the same as ground truth, and that treating them as such induces severe
theoretical and practical problems. We prove that no algorithm can uniquely solve community
detection, and we prove a general No Free Lunch theorem for community detection, which implies
that no algorithm can perform better than any other across all inputs. However, node metadata
still have value and a careful exploration of their relationship with network structure can yield
insights of genuine worth. We illustrate this point by introducing two statistical techniques that can
quantify the relationship between metadata and community structure for a broad class models. We
demonstrate these techniques using both synthetic and real-world networks, and for multiple types
of metadata and community structure.

