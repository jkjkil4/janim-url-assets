[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)
[![PyPI Latest Release](https://img.shields.io/pypi/v/janim-url-assets.svg?style=flat&logo=pypi)](https://pypi.org/project/janim-url-assets/)

<div align="center">

**> English <** | [简体中文](README_zh_CN.md)

</div>

## Introduction

`janim-url-assets` is a JAnim plugin for loading remote assets directly from URLs.

Main provided items are:

- `UrlSVGItem`: load an SVG from a URL and use it as a normal `SVGItem`
- `UrlImageItem`: load an image from a URL and use it as a normal `ImageItem`


## Installation

(not published yet)

```bash
pip install janim-url-assets
```

After installation, examples from this plugin will appear in `janim examples`.

## Usage

### Import

```python
from janim_url_assets.imports import *
```

### Load SVG from URL

```python
UrlSVGItem('https://dev.w3.org/SVG/tools/svgweb/samples/svg-files/ibm.svg')
```

### Load image from URL

```python
UrlImageItem('https://raw.githubusercontent.com/jkjkil4/JAnim/main/assets/logo.png')
```

### Use resources from specific asset sites

```python
Iconify('skill-icons:aftereffects', width=1)
```

You can search icon names at <https://icon-sets.iconify.design/>.
