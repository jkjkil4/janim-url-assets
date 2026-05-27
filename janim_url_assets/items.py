from janim.items.svg.svg_item import SVGItem

from janim_url_assets.utils import download


class UrlSVGItem(SVGItem):
    def __init__(self, url: str, **kwargs):
        super().__init__(download(url, '.svg'), **kwargs)
