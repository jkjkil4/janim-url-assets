"""
该文件中包含了一些辅助函数

其中最主要的是 :py:func:`download` 用于下载 URL 内容
"""

import hashlib
import os
import sys
from contextlib import contextmanager
from urllib.request import Request, urlopen

from janim.utils.config import Config
from janim.utils.file_ops import guarantee_existence


def download(url: str, suffix: str = '', *, timeout: int = 10) -> str:
    """
    下载 ``url`` 的内容，返回暂存的文件路径

    曾下载过的 ``url`` 会被缓存

    :param url: 要下载的 URL
    :param suffix: 暂存文件的附加后缀名，若要表示文件扩展名，需带上点，如 ``.svg``
    """
    file_dir = guarantee_existence(os.path.join(Config.get.temp_dir, 'url_downloads'))

    md5 = hashlib.md5(url.encode()).hexdigest()
    file_path = os.path.join(file_dir, f'{md5}{suffix}')

    if os.path.exists(file_path):
        return file_path

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    with loading(f'Downloading {url} ...'):
        with urlopen(req, timeout=timeout) as resp:
            buffer = resp.read()
    with open(file_path, 'wb') as f:
        f.write(buffer)

    return file_path


@contextmanager
def loading(message: str):
    print(message, end='', flush=True, file=sys.stderr)
    try:
        yield
        # 有意没将该句放在 try-finally 中
        print('\r\033[K', end='', flush=True, file=sys.stderr)  # ]
    except Exception:
        print()
        raise
