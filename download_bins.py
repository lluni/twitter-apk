import requests
import re
from utils import download


def download_release_asset(repo: str, regex: str, out_dir: str, filename=None, include_prereleases: bool = False, version = None):
    url = f"https://api.github.com/repos/{repo}/releases"

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch github")

    releases = [r for r in response.json() if include_prereleases or not r["prerelease"]]

    if not releases:
        raise Exception(f"No releases found for {repo}")

    if version is not None:
        releases = [r for r in releases if r["tag_name"] == version]

    if len(releases) == 0:
        raise Exception(f"No release found for version {version}")

    latest_release = releases[0]

    assets = latest_release["assets"]

    link = None
    for i in assets:
        if re.search(regex, i["name"]):
            link = i["browser_download_url"]
            if filename is None:
                filename = i["name"]
            break

    download(link, f"{out_dir.lstrip('/')}/{filename}")

    return latest_release


def download_apkeditor():
    print("Downloading APKEditor")
    download_release_asset("REAndroid/APKEditor", "APKEditor", "bins", "apkeditor.jar")


def download_cli():
    print("Downloading CLI")
    download_release_asset(
        "MorpheApp/morphe-cli", "^morphe-cli.*-all\.jar$", "bins", "cli.jar", version="v1.3.0"
    )
