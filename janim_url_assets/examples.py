# ruff: noqa
# type: ignore
# fmt: off
from janim.imports import *
from janim_url_assets.imports import *


class IconifyExample(Timeline):
    def construct(self):
        adobe_icon_names = [
            'skill-icons:audition',
            'skill-icons:aftereffects',
            'skill-icons:premiere',
            'skill-icons:photoshop',
            'skill-icons:xd',
        ]

        adobe_icons = Group.from_iterable(
            Iconify(name, width=1) 
            for name in adobe_icon_names
        ).show()
        adobe_icons.points.arrange()
        UrlSVGItem('https://dev.w3.org/SVG/tools/svgweb/samples/svg-files/ibm.svg').show()
