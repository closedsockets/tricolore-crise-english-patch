# Changelog

## v1.0.2 — 2026-07-14

### Added

- Translated 163 unique fragments, map labels, choices, and interface strings
  missed by the earlier completion sweep. These add 269 previously absent disc
  replacements: 267 in `TC_EVENT.FAR` and two in `1ST_READ.BIN`.
- Completed the remaining magic/skill image plates, bringing the in-disc
  status/magic total to 32 plates.

### Changed

- Revised 1,197 existing disc replacements across 986 unique source/target
  pairs for terminology, context, line flow, and consistency.
- Standardized official/reference spellings throughout the active patch,
  including Aghathia, Anemea Glender, Stum "Burnin'", Kantalra, Hauk Glender,
  Sa'am, Yerum, Shanna Woods, Azul Highlands, HeatLord's Hill, Juno, Xian,
  Diadolla, Vasyar, Saro, and Arc-Shar.
- Expanded translated system-text coverage from 1,175 to 1,177 entries.

### Verified

- The build validator passes with 17,151 safe replacements.
- Independent BPS and JSON applications both produce patched `track03.bin`
  SHA-1 `1bc0fe1da334be249a9e8c96d346d218dc9e913d`.
- BPS SHA-256:
  `50194b4cac099836d60decbf1074b0d8284f4f1a20f73a9904942a9b89354ed8`.

## v1.0.1 — 2026-07-11

- Corrected the second protagonist's English spelling from `Ranan` to
  `Lanan`, following the original baked Latin status header. Applied across
  active dialogue, menus, system/battle UI, and release metadata.

## v1.0.0 — 2026-07-11

- Final functional release.
- Complete story/event translation: 11,224 unique strings at 14,995 disc
  locations; 1,175 system-text entries; 43 battle-UI entries.
- English in-disc artwork for the title menu, the first 26 status/magic
  plates, Options, and system-message plates.
- Remaining visual differences are non-blocking polish; name-entry character
  grids remain intentionally Japanese input tables.

## v0.9.5-alpha — 2026-07-11

- English title menu and the first 26 status/magic image plates.

## v0.9.0-alpha — 2026-07-09

- Complete event script, major system text, and identified battle UI.
