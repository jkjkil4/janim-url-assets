"""
该文件是该包的核心部分

其中定义了若干 JAnim 原有的物件可传入 URL 路径的版本
"""

from janim.items.image_item import ImageItem
from janim.items.svg.svg_item import SVGItem

from janim_url_assets.utils import download


class UrlSVGItem(SVGItem):
    """
    解析指定 URL 链接的 SVG 素材

    比如：

    .. code-block:: python

        UrlSVGItem('https://dev.w3.org/SVG/tools/svgweb/samples/svg-files/ibm.svg')

    :param url: URL 链接
    """

    def __init__(self, url: str, **kwargs):
        super().__init__(download(url, '.svg'), **kwargs)


class UrlImageItem(ImageItem):
    """
    解析指定 URL 链接的图像素材

    比如：

    .. code-block:: python

        UrlImageItem('https://raw.githubusercontent.com/jkjkil4/JAnim/main/assets/logo.png')

    :param url: URL 链接
    """

    def __init__(self, url: str, **kwargs):
        # .img 不是一个真实的后缀，只是用来标识
        super().__init__(download(url, '.img'), **kwargs)
