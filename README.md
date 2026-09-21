# Dilmurat Yusuf — Portfolio

Static source for `https://dyusuf.github.io/`. This repository links to the projects
that own each analysis or software artifact; it does not duplicate their source.

## Local preview

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

## Page structure

The homepage introduces four areas: biomedical AI, omics, scientific software,
and training. Each has one short paragraph and links to supporting work.
Keep methods, benchmark results, project histories and detailed scientific
findings in the linked project pages. Preserve concise contribution labels
where they clarify design, development or supervision.

## Repository ownership

- `bioinformatics-courses` owns the vascular-repair case study and workflow.
- `BinfoNet` owns its evidence-retrieval implementation and evaluation.
- `BinfoCheck` owns its AI-search measurement implementation, tests, and project documentation.
- `BinfoWise` owns its literature-mining application.
- Upstream repositories own AxoWise, RCAS, ena-upload-cli, Galaxy, and Bioconda artifacts.
- This repository owns only the cross-project public presentation.

Public deployment is a separate candidate approval. GitHub Pages can serve the
repository root after the exact rendered page and links have been reviewed.
The public wording and its sources are recorded in [EVIDENCE.md](EVIDENCE.md).

## Font

The page uses Computer Modern Bright Roman from CM-Super. See
`assets/CM-Super-README.txt` for the retained license notice.
