import os
from urllib.parse import urlparse
from typing import Optional
import time


def load_file_from_url(
        url: str,
        *,
        model_dir: str,
        progress: bool = True,
        file_name: Optional[str] = None,
) -> str:
    """Download a file from `url` into `model_dir`, using the file present if possible.

    Returns the path to the downloaded file.
    """
    domain = os.environ.get("HF_MIRROR", "https://huggingface.co").rstrip('/')
    url = str.replace(url, "https://huggingface.co", domain, 1)
    os.makedirs(model_dir, exist_ok=True)
    if not file_name:
        parts = urlparse(url)
        file_name = os.path.basename(parts.path)
    cached_file = os.path.abspath(os.path.join(model_dir, file_name))
    if not os.path.exists(cached_file):
        print(f'Downloading: "{url}" to {cached_file}\n')
        from torch.hub import download_url_to_file
        max_retries = 3
        retry_delay = 5
        for attempt in range(max_retries):
            try:
                download_url_to_file(url, cached_file, progress=progress)
                break
            except Exception as e:
                if attempt < max_retries - 1:
                    print(f'Download attempt {attempt + 1} failed: {str(e)}')
                    print(f'Retrying in {retry_delay} seconds...')
                    time.sleep(retry_delay)
                    retry_delay *= 2
                else:
                    print(f'Failed to download after {max_retries} attempts: {str(e)}')
                    raise
    return cached_file
