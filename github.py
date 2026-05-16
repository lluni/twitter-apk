from dataclasses import dataclass
from urllib.parse import quote

import requests
from constants import HEADERS

REQUEST_TIMEOUT_SECONDS = 30


@dataclass
class Asset:
    browser_download_url: str
    name: str


@dataclass
class GithubRelease:
    tag_name: str
    html_url: str
    assets: list[Asset]


def _to_github_release(release) -> GithubRelease:
    assets = [
        Asset(browser_download_url=asset["browser_download_url"], name=asset["name"])
        for asset in release["assets"]
    ]

    return GithubRelease(
        tag_name=release["tag_name"], html_url=release["html_url"], assets=assets
    )


def _fetch_release(url: str) -> GithubRelease | None:
    response = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT_SECONDS)

    if response.status_code == 404:
        return None

    response.raise_for_status()
    return _to_github_release(response.json())


def get_release_by_tag(repo_url: str, tag: str) -> GithubRelease | None:
    encoded_tag = quote(tag, safe="")
    url = f"https://api.github.com/repos/{repo_url}/releases/tags/{encoded_tag}"
    return _fetch_release(url)


def get_last_build_version(repo_url: str) -> GithubRelease | None:
    url = f"https://api.github.com/repos/{repo_url}/releases/latest"
    return _fetch_release(url)
