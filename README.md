# Global wave completion and recognition of smooth twistor sources

Lior Isthmus · Version 1.0 · [ORCID 0009-0004-7908-9876](https://orcid.org/0009-0004-7908-9876)

We construct a global wave class for smooth globally hyperbolic vacuum spacetimes at physical scale with a specified spin structure. Its four Cauchy traces determine the class modulo globally smooth kernels. The wave class compares spacelike carriers and their point evaluations. An ordinary-pair atlas satisfying the quotient and causal tests has a unique completion up to marked full comparison. The paper also treats smooth families and the analytic comparison under its stated calibration hypotheses.

[Read the manuscript](paper/smooth-global-twistor-sources-en-v1.0.md) · [Computational supplement](computations/README.md) · [Recorded results](computations/results/verified.json)

## Version 1.0 distribution

The [GitHub release](https://github.com/lioristhmus/smooth-global-twistor-sources/releases/tag/v1.0) groups the following files. A Zenodo version DOI has yet to be assigned.

| Release file | Contents |
|---|---|
| [smooth-global-twistor-sources-en-v1.0.pdf](https://github.com/lioristhmus/smooth-global-twistor-sources/releases/download/v1.0/smooth-global-twistor-sources-en-v1.0.pdf) | Paper with a supplement locator in §17.2. |
| [smooth-global-twistor-sources-source-v1.0.zip](https://github.com/lioristhmus/smooth-global-twistor-sources/releases/download/v1.0/smooth-global-twistor-sources-source-v1.0.zip) | Markdown, standalone TeX, computations, citation files and licenses. |
| [smooth-global-twistor-sources-computations-v1.0.zip](https://github.com/lioristhmus/smooth-global-twistor-sources/releases/download/v1.0/smooth-global-twistor-sources-computations-v1.0.zip) | Programs, inputs, recorded results and the manuscript in Markdown for equation references. |
| [smooth-global-twistor-sources-v1.0.zip](https://github.com/lioristhmus/smooth-global-twistor-sources/releases/download/v1.0/smooth-global-twistor-sources-v1.0.zip) | Complete snapshot including the PDF and TeX. |
| [SHA256SUMS](https://github.com/lioristhmus/smooth-global-twistor-sources/releases/download/v1.0/SHA256SUMS) | SHA-256 digests for the four release files. |

In the complete snapshot, open `paper/smooth-global-twistor-sources-en-v1.0.pdf` to read the paper offline. Its supplement link opens `computations/README.md` in the extracted directory. The Markdown and supplement guide link to each other in all three archives. Each archive has its own manifest. From the extracted top-level directory run `shasum -a 256 -c SHA256SUMS`.

To typeset the paper from the source archive or complete snapshot, change to `paper/` and run `TZ=UTC pdflatex -no-shell-escape smooth-global-twistor-sources-en-v1.0.tex` three times with TeX Live and the standard AMS packages.

## Citation and licenses

Lior Isthmus (2026), *Global wave completion and recognition of smooth twistor sources*, version 1.0. [Citation File Format](CITATION.cff) · [BibTeX](citation.bib)

The paper, documentation, computational inputs and recorded results use CC BY 4.0. The Python programs use Apache-2.0. [License terms and file scopes](LICENSES.md)
