"""
该文件中提供了开箱即用的，线上素材站资源的封装
"""

from janim_url_assets.items import UrlSVGItem


class Iconify(UrlSVGItem):
    """
    使用方式：

    在 https://icon-sets.iconify.design/ 中查找你需要使用的图标，点进图标后，点击 ``Copy Name:`` 那一行最右边的复制按钮，即可传入该类使用

    .. tip::

        iconify 上的图标大部分默认为黑色，你可以给该类传入类似 ``color=WHITE`` 的参数来修改
    """

    def __init__(self, name: str, **kwargs):
        url = f'https://api.iconify.design/{name}.svg?width=32'
        super().__init__(url, **kwargs)
