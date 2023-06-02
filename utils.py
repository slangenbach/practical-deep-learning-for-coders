"""Utility functions."""

from duckduckgo_search import ddg_images
from fastcore.foundation import L
from fastdownload import download_url
from fastai.vision.all import Image


def search_images(term: str, max_images: int = 200) -> L:
    """Search images using DuckDuckGo."""
    return L(ddg_images(keywords=term, max_results=max_images)).itemgot("image")


def download_and_show_image(url: str, image_name: str):
    """Download ans show a thumbnail of an image"""
    download_url(url=url, dest=f"{image_name}.jpg", show_progress=False)
    image = Image.open(f"{image_name}.jpg")
    return image.to_thumb(256, 256)
