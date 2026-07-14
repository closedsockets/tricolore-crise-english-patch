# Tricolore Crise English Patch v1.0.2

An unofficial English fan translation for Sega Dreamcast's *Tricolore Crise*.
This repository contains patch data and documentation only—never game files,
BIOS files, or an emulator.

## Release scope

- Complete event script: 11,224 unique strings across 14,995 disc locations.
- 1,177 translated system-text entries and all 43 identified battle-UI entries.
- In-disc English image UI for the title menu, Options, two system-message
  plates, and 32 status/magic plates covering the three protagonists and 13
  familiar classes. These edits work on Dreamcast hardware as well as
  emulators.
- Fixed-width text, format tokens, line breaks, source hashes, image sizes,
  and overlapping replacements are validated during the build. The v1.0.2
  build validates 17,151 replacements.

The patch is considered functionally complete. Japanese name-entry character
grids remain intentionally because they are input tables, not ordinary
interface copy. A few non-blocking branding, splash, accessory-notice, and
portrait-name graphics may retain Japanese presentation text.

## What's new in v1.0.2

- Translates 163 unique fragments, map labels, choices, and interface strings
  missed by the earlier completion sweep, adding 269 disc replacements.
- Revises 1,197 existing disc replacements for terminology, context, and
  official/reference spellings.
- Standardizes names and places such as Aghathia, Anemea Glender, Stum
  "Burnin'", Kantalra, Sa'am, Yerum, Shanna Woods, Azul Highlands,
  HeatLord's Hill, Juno, Xian, Diadolla, Vasyar, and Saro.
- Includes newly rebuilt and independently verified BPS and JSON patch
  formats.

See [CHANGELOG.md](CHANGELOG.md) for the full release history.

## Apply the patch

Download `tricolore_crise_english_patch_v1.0.2.bps` from the release and apply
it to `track03.bin` from a clean, legally obtained GDI dump. The required
source SHA-1 is:

`5608009f040cbed33e4b29da33fc36e29bc24b62`

For a Windows helper that does not require a BPS program, download the JSON
patch and run `Apply_JSON_Patch.bat`; it verifies both the source and output
automatically. See [PATCHING.md](PATCHING.md) for the JSON-helper and standard
BPS methods.

## Verification

| Item | Digest |
| --- | --- |
| Clean `track03.bin` | SHA-1 `5608009f040cbed33e4b29da33fc36e29bc24b62` |
| Patched v1.0.2 `track03.bin` | SHA-1 `1bc0fe1da334be249a9e8c96d346d218dc9e913d` |
| v1.0.2 BPS | SHA-256 `50194b4cac099836d60decbf1074b0d8284f4f1a20f73a9904942a9b89354ed8` |
| v1.0.2 JSON | SHA-256 `5babf40c963de3723aaf68281ec09650a30cd1d6bb56624c1133b2e94b7fb6ff` |

Both patch formats were applied independently to the clean source and
produced the documented patched SHA-1.

See [RELEASE_NOTES.md](RELEASE_NOTES.md) for technical details and
[ROMHACKING_SUBMISSION.md](ROMHACKING_SUBMISSION.md) for the current listing
copy.

## Legal

*Tricolore Crise* and all original assets belong to their respective rights
holders. This is an unofficial, non-commercial fan project. Use the patch only
with a legally obtained copy of the game.
