# Applying the v1.0.2 patch

Always work from a copy of your legally obtained GDI dump. Do not modify or
share the original game files.

## Standard BPS method

Use this method with a BPS program such as
[Floating IPS (Flips)](https://github.com/Alcaro/Flips/releases).

### You need

- A clean, legally obtained GDI dump of *Tricolore Crise*.
- A BPS-compatible patcher.
- `tricolore_crise_english_patch_v1.0.2.bps`.

### Steps

1. Find `track03.bin` in the clean dump.
2. Verify its SHA-1 is `5608009f040cbed33e4b29da33fc36e29bc24b62`.
3. Apply the BPS patch. A compatible patcher will reject the wrong source.
4. Put the patched `track03.bin` back into a copy of the GDI folder. Leave the
   other tracks and the `.gdi` file unchanged.
5. Open the copied `.gdi` in a Dreamcast emulator or on compatible hardware.

## Windows JSON helper — no BPS program required

1. Download `Apply_JSON_Patch.bat`, `apply_json_patch.py`, and
   `tricolore_crise_english_patch_v1.0.2.json` from the GitHub release. Keep
   all three files in the same folder.
2. Double-click `Apply_JSON_Patch.bat`, drag your clean `track03.bin` onto the
   black window, and press Enter. This requires the normal Windows Python
   launcher (`py`); install Python from python.org if `py` is not recognized.
3. The helper verifies the source, creates `track03_english_v1.0.2.bin`, and
   verifies the completed file. Copy that output into a **copy** of your GDI
   folder and rename it to `track03.bin`.

The expected patched `track03.bin` SHA-1 is
`1bc0fe1da334be249a9e8c96d346d218dc9e913d`.

Do not share game images or track files. Distribute the patch files only.
