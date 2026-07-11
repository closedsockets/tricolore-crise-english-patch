# Tricolore Crise English Patch v0.9.5-alpha

Second public playtest release of the *Tricolore Crise* English fan
translation. The headline feature: the first in-disc image translations.

- NEW: English title menu.
- NEW: all status and magic screens translated — 3 mage status screens
  (Jamis, Ranan, Anemea), all 13 familiar class status screens, and 10
  magic/skill list screens. These are baked-pixel image edits (PAL8 twiddled
  tile plates re-encoded byte-exact inside TC_WALL.FAR), so they work on real
  hardware, not only via emulator texture packs.
- Complete event script: 11,224 / 11,224 unique strings translated across
  14,995 disc locations, plus major system text and all identified battle UI
  strings (unchanged from v0.9.0-alpha).

## Built with Dreamcast Translation Kit

This patch was created with the open-source
[Dreamcast Translation Kit v0.1.0](https://github.com/closedsockets/dreamcast-translation-kit/releases/tag/v0.1.0).
The toolkit scans a clean GDI dump into a CSV worklist, supports glossary-led
AI-assisted translation batches, validates fixed-width replacements, and
builds BPS patches without distributing game data.

## Remaining work

- Options screen art remains Japanese (source located; translation planned).
- More emulator and hardware playtesting is needed before a 1.0 release.

This download contains patch data only and requires a legally obtained clean
dump with a `track03.bin` SHA-1 of
`5608009f040cbed33e4b29da33fc36e29bc24b62`.
