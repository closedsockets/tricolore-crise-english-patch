# Applying the patch

## You need

- A legally obtained, clean GDI dump of *Tricolore Crise*.
- A BPS-compatible patcher.
- The `tricolore_crise_english_patch_v0.9.0-alpha.bps` file from this
  repository's release.

## Steps

1. Locate `track03.bin` in your clean GDI dump.
2. Verify its SHA-1 is:

   `5608009f040cbed33e4b29da33fc36e29bc24b62`

3. Apply the BPS patch to that file. The patcher should reject an incorrect
   source file automatically.
4. Replace only `track03.bin` in a copy of your dump; leave the other tracks
   and the `.gdi` file unchanged.
5. Open the copied `.gdi` in a Dreamcast emulator or use compatible hardware.

## Reporting issues

Please include the scene, emulator/hardware, a screenshot, and whether the
problem is a missing translation, text overflow, bad line break, or context
issue. This is an alpha release, so useful playtest reports directly improve
the final patch.

## Important

Never share game images or track files. Share only the BPS patch.
