# Tricolore Crise English Patch v1.0.0

An unofficial English fan translation for Sega Dreamcast's *Tricolore Crise*.
This repository contains patch data and documentation only—never game files,
BIOS files, or an emulator.

## Final release scope

- Complete event script: 11,224 unique strings across 14,995 disc locations.
- 1,175 translated system-text entries and all 43 identified battle-UI entries.
- In-disc English image UI for the title menu, 26 status/magic plates, Options,
  and the system-message plates. These edits work on Dreamcast hardware as
  well as emulators.
- Fixed-width text, format tokens, line breaks, source hashes, and overlapping
  replacements are validated during the build. The final validation covered
  16,875 replacements.

The patch is considered functionally complete. Some replacement art favors
readability and coverage over a polished recreation of the original styling.
The Japanese name-entry character grids remain intentionally: they are input
tables, not ordinary interface copy. A few non-blocking title/splash and
accessory-notice graphics may retain Japanese presentation text.

## Apply the patch

Download `tricolore_crise_english_patch_v1.0.0.bps` from the release and apply
it to `track03.bin` from a clean, legally obtained GDI dump. The required
source SHA-1 is:

`5608009f040cbed33e4b29da33fc36e29bc24b62`

See [PATCHING.md](PATCHING.md) for the full procedure and
[RELEASE_NOTES.md](RELEASE_NOTES.md) for the technical release scope.

## Legal

*Tricolore Crise* and all original assets belong to their respective rights
holders. This is an unofficial, non-commercial fan project. Use the patch only
with a legally obtained copy of the game.
