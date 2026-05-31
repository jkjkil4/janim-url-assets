.. janim-url-assets documentation master file, created by
   sphinx-quickstart on Wed May 27 22:19:36 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

janim-url-assets 文档
==========================

``janim-url-assets`` 是一个用于直接从 URL 加载线上素材的 JAnim 插件。

主要提供了如下的物件：

- :class:`~.UrlSVGItem` : 从 URL 加载 SVG，并按普通 ``SVGItem`` 使用

- :class:`~.UrlImageItem` : 从 URL 加载图片，并按普通 ``ImageItem`` 使用

安装
----------------

.. code-block:: python

   pip install janim-url-assets

在安装后， ``janim examples`` 会出现该插件的示例

使用方式
-------------------

导入
~~~~~~~~~~~~~~~

.. code-block:: python

   from janim_url_assets.imports import *

从 URL 加载 SVG
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    UrlSVGItem('https://dev.w3.org/SVG/tools/svgweb/samples/svg-files/ibm.svg')

具体请参考 :class:`~.UrlSVGItem` 的文档

从 URL 加载图片
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    UrlImageItem('https://raw.githubusercontent.com/jkjkil4/JAnim/main/assets/logo.png')

具体请参考 :class:`~.UrlImageItem` 的文档

使用特定素材站的资源
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    Iconify('skill-icons:aftereffects', width=1)

具体请参考 :class:`~.Iconify` 的文档

.. toctree::
    :maxdepth: 2
    :caption: 参考文档

    janim_url_assets/modules

内容索引
---------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
