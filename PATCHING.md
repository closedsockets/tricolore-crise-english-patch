# Applying the v1.0.2 patch

Always work from a copy of your legally obtained GDI dump. Do not modify or
share the original game files.

## You need

- A clean, legally obtained GDI dump of *Tricolore Crise*.
- A BPS-compatible patcher such as
  [Floating IPS (Flips)](https://github.com/Alcaro/Flips/releases).
- `tricolore_crise_english_patch_v1.0.2.bps`.

## Steps

1. Find `track03.bin` in the clean dump.
2. Verify its SHA-1 is `5608009f040cbed33e4b29da33fc36e29bc24b62`.
3. Apply the BPS patch. A compatible patcher will reject the wrong source.
4. Put the patched `track03.bin` back into a copy of the GDI folder. Leave the
   other tracks and the `.gdi` file unchanged.
5. Open the copied `.gdi` in a Dreamcast emulator or on compatible hardware.

The expected patched `track03.bin` SHA-1 is
`1bc0fe1da334be249a9e8c96d346d218dc9e913d`.

Do not share game images or track files. Distribute the BPS patch only.
