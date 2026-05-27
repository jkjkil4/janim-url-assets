[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)
[![PyPI Latest Release](https://img.shields.io/pypi/v/janim-url-assets.svg?style=flat&logo=pypi)](https://pypi.org/project/janim-url-assets/)

<div align="center">

[English](README.md) | **> 简体中文 <**

</div>

## 简介

`janim-url-assets` 是一个 JAnim 插件，用于直接从 URL 加载线上素材。

主要提供了如下的物件：

- `UrlSVGItem`：从 URL 加载 SVG，并按普通 `SVGItem` 使用
- `UrlImageItem`：从 URL 加载图片，并按普通 `ImageItem` 使用

## 安装

（还未发布）

```bash
pip install janim-url-assets
```

在安装后，`janim examples` 会出现该插件的示例

## 使用方式

### 导入

```python
from janim_url_assets.imports import *
```

### 从 URL 加载 SVG

```python
UrlSVGItem('https://dev.w3.org/SVG/tools/svgweb/samples/svg-files/ibm.svg')
```

### 从 URL 加载图片

```python
UrlImageItem('https://raw.githubusercontent.com/jkjkil4/JAnim/main/assets/logo.png')
```

### 使用特定素材站的资源

```python
Iconify('skill-icons:aftereffects', width=1)
```

图标名称可在 <https://icon-sets.iconify.design/> 中检索。
