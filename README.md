# Tricolore Crise English Patch

An unofficial English fan-translation patch for the Sega Dreamcast game
*Tricolore Crise*.

> Built with [Dreamcast Translation Kit v0.1.0](https://github.com/closedsockets/dreamcast-translation-kit/releases/tag/v0.1.0), an open, AI-friendly workflow for scanning Shift-JIS text, translating CSV worklists, validating fixed-width replacements, and building BPS patches.

## v0.9.5-alpha status

The event script is fully translated, and this release adds the first
in-disc image translations: the title menu and every status and magic
screen. It remains an alpha while the options screen art and final visual
polish are completed.

| Area | Coverage |
| --- | --- |
| Event dialogue | 11,224 / 11,224 unique strings translated |
| Event-script occurrences | 14,995 disc locations covered |
| System text | 1,175 translated entries |
| Battle UI | 43 / 43 identified entries translated |
| UI art | Title menu + 26 status/magic screen plates translated in-disc |
| Patch build | 16,875 validated replacements |

## Download and apply

Download `tricolore_crise_english_patch_v0.9.5-alpha.bps` from the latest
release. Apply it with a BPS-compatible patcher to `track03.bin` from a clean,
legally obtained GDI dump.

Required source SHA-1:

`5608009f040cbed33e4b29da33fc36e29bc24b62`

See [PATCHING.md](PATCHING.md) for the complete instructions.

## What is translated

- Complete event/dialogue script, including every matching location on disc.
- Character names, terminology, choices, counters, and color-coded terms.
- Major system/menu text and all identified battle UI strings.
- Title menu art, all 16 status screens (3 mages + 13 familiar classes), and
  all 10 magic/skill list screens — translated as baked image data, so they
  work on real hardware as well as emulators.

## Remaining work

- Options screen art (source now located; translation planned).
- Optional English portrait name tags.
- Additional emulator and hardware playtesting, plus final text polish.

The Japanese character grids used by name entry are intentionally retained:
they are input tables rather than ordinary interface text.

## Built with Dreamcast Translation Kit

This project is the first production patch created with the
[Dreamcast Translation Kit](https://github.com/closedsockets/dreamcast-translation-kit/releases/tag/v0.1.0).
The toolkit supports CSV-based translation worklists, glossary-led
AI-assisted batches, duplicate handling, fixed-width validation, BPS patch
creation, and PVR image workflows. It distributes no game files.

## Legal

This repository and its releases contain patch data only. They do not include
game files, BIOS files, or an emulator. *Tricolore Crise* and all original
assets are the property of their respective rights holders. This is an
unofficial, non-commercial fan project; use it only with a legally obtained
copy of the game.
