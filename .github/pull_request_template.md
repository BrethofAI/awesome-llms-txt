<!--
Thanks for contributing an entry! Quick checklist:

- [ ] Filename under entries/ matches the slug (e.g. `entries/my-tool.yaml` if slug is `my-tool`)
- [ ] Category is from the controlled vocabulary in CONTRIBUTING.md
- [ ] `added` date is today's date, YYYY-MM-DD
- [ ] For showcase entries: included description, features, use_cases
- [ ] For stubs: set `status: stub` so build.py marks them with 🚧
- [ ] If `llms_txt_status: published`, you've verified the URL returns 200 on a fresh fetch
- [ ] You don't need to regenerate README.md / llms.txt / llms-full.txt — CI does that

One entry per PR, please.
-->

## What does this PR change?

<!-- e.g. "Adds entry for MyTool", "Upgrades jan.ai stub to showcase", "Fixes broken llms.txt URL for X" -->

## Relationship to the tool

- [ ] I maintain or work on this tool
- [ ] I use this tool but have no affiliation with it
- [ ] I don't use the tool — submitting because it seemed missing

## For tool maintainers

If you maintain the tool and you're here because your entry was marked `missing`:
- [ ] I'm flipping `llms_txt_status` to `published` because we now publish llms.txt
- [ ] I've verified the URL `curl -sIL` returns 200 with `content-type: text/plain`
