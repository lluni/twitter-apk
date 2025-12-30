from apkmirror import Version
from utils import patch_apk


def build_apks(latest_version: Version):
    # patch
    apk = "big_file_merged.apk"
    patches = "bins/patches.rvp"
    cli = "bins/cli.jar"

    common_includes = [
        "Enable app downgrading",
        "Hide FAB",
        "Disable chirp font",
        "Add ability to copy media link",
        "Hide Banner",
        "Hide promote button",
        "Hide Community Notes",
        "Delete from database",
        "Customize Navigation Bar items",
        "Remove premium upsell",
        "Control video auto scroll",
        "Force enable translate",
    ]

    common_excludes = []

    patch_apk(
        cli,
        patches,
        apk,
        includes=["Dynamic color"] + common_includes,
        excludes=common_excludes,
        out=f"x-piko-material-you-v{latest_version.version}.apk",
    )

    patch_apk(
        cli,
        patches,
        apk,
        includes=common_includes,
        excludes=["Dynamic color"] + common_excludes,
        out=f"x-piko-v{latest_version.version}.apk",
    )

    patch_apk(
        cli,
        patches,
        apk,
        includes=["Bring back twitter", "Dynamic color"] + common_includes,
        excludes=common_excludes,
        out=f"twitter-piko-material-you-v{latest_version.version}.apk",
    )

    patch_apk(
        cli,
        patches,
        apk,
        includes=["Bring back twitter"] + common_includes,
        excludes=["Dynamic color"] + common_excludes,
        out=f"twitter-piko-v{latest_version.version}.apk",
    )
