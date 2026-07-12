# Tricolore Crise English Patch v1.0.1

This is a post-release spelling correction for the final functional release of
the *Tricolore Crise* English patch.

## v1.0.1 correction

- Replaces `Ranan` with **`Lanan`** everywhere in active dialogue, menus,
  battle UI, system text, and generated patch metadata. `Lanan` matches the
  original game's baked Latin name header on her status screen.
- Added a JSON patch plus a drag-and-drop Windows helper for players who do
  not use a BPS application.

## Included

- Complete event dialogue: 11,224 unique strings covering 14,995 locations.
- Major system text (1,175 entries) and all identified battle UI (43 entries).
- English title-menu, status, familiar-status, magic/skill, Options, and
  system-message image plates baked directly into the disc patch.
- Source-verified BPS distribution for clean `track03.bin` SHA-1
  `5608009f040cbed33e4b29da33fc36e29bc24b62`.

The final build validates 16,875 non-overlapping replacements. Image edits
preserve their original allocation and are re-encoded into the game's native
formats; the patch contains no game data.

## Release position

v1.0.0 is a completion release, not a claim that every replacement graphic is
artistically final. The remaining Japanese visual material is non-blocking
branding, splash, or accessory-notice presentation; the name-entry character
grids are intentionally retained as input tables. The playable story and
required navigation/UI coverage are complete.

## Verification

- BPS SHA-256: `58339b4786510685c8a34314fb6d18de5a2200a65d3cc9d41d66bc258d5c0ecf`
- Build validation: 16,884 replacements.
- Options and all shipped status/magic plates were checked in Flycast; the
  plate route is in-disc and suitable for hardware use.
