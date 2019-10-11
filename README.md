[![Build Status](https://travis-ci.org/ViDA-NYU/reproducibility-news.svg?branch=master)](https://travis-ci.org/ViDA-NYU/reproducibility-news)

Reproducibility news
====================

This repository contains the recent news about reproducibility that are shown on [reproduciblescience.org](https://reproduciblescience.org/). The raw RSS feed is [here](https://vida-nyu.github.io/reproducibility-news/feed.rss).

Please, do not hesitate to provide news about your own work by opening a Pull Request here or by contacting us. A [contributing guide](CONTRIBUTING.md) is available to guide you through the process.

RSS Format
==========

The feed is generated from a YAML file, `news.yaml`, that you can [edit here](https://github.com/ViDA-NYU/reproducibility-news/edit/master/news.yaml). The format is as follow:

```
---
title: |
  Some meaningful title here (will be tweeted out)
link: link to the original article or publication
date: 2017-02-21 00:00:00
tags: [reproducibility talk]
description: |
  Multi-line description here. Will show up in RSS readers.
  Like the title field, be careful not to forget the indentation.

---
title: |
  Other entry
link: other link
date: 2016-01-12 00:00:00
tags: [data science, news article]
description: |
  Another entry.
```

RSS Tags
========
| Tag | Content |
|--------------------------------|---------------------------------------------------------------------------------------------------------|
| case studies | reproducibility case studies |
| data science | everything related to data science |
| news article | articles published by scientific bodies |
| noWorkflow | everything related to noWorkflow |
| open access | everything related to open access publishing of data and papers |
| popular news | articles published by popular reporting organizations (NY times, etc.) |
| replication study | studies that seek to replicate scientific findings |
| reproducibility bibliography | bibliographies having to do with reproducibility |
| reproducibility conference | conferences that want reproducible papers/posters accepted AND conferences that discuss reproducibility |
| reproducibility guidelines | guidelines for reproducibility |
| reproducibility infrastructure | reports/articles/papers on building reproducibility infrastructure |
| reproducibility report | reports by governing bodies on reproducibility of a field's work |
| reproducibility study | studies that seek to reproduce research |
| reproducibility talk | talks and presentations about reproducibility |
| reproducible journal | journals that work towards reproducibility efforts (requiring submissions to be reproducible, etc. |
| reproducible paper | papers that are considered reproducible |
| ReproZip | everything related to ReproZip |
| research guide | library guides for reproducibility |
| retraction | report of a paper being retracted |
| VisTrails | everything related to VisTrails |
