<div id="top"></div>

<!-- omit in toc -->
# From Zero Linear Algebra

<p align="center">
  A public, beginner-friendly linear algebra textbook repository for Chinese-speaking self-learners, make-up exam preparation, and AI-assisted study workflows.
</p>

<p align="center">
  <a href="https://github.com/ShuoMeng66/Linear-Algebra/graphs/contributors"><img src="https://img.shields.io/github/contributors/ShuoMeng66/Linear-Algebra.svg?style=for-the-badge" alt="Contributors"></a>
  <a href="https://github.com/ShuoMeng66/Linear-Algebra/network/members"><img src="https://img.shields.io/github/forks/ShuoMeng66/Linear-Algebra.svg?style=for-the-badge" alt="Forks"></a>
  <a href="https://github.com/ShuoMeng66/Linear-Algebra/stargazers"><img src="https://img.shields.io/github/stars/ShuoMeng66/Linear-Algebra.svg?style=for-the-badge" alt="Stars"></a>
  <a href="https://github.com/ShuoMeng66/Linear-Algebra/issues"><img src="https://img.shields.io/github/issues/ShuoMeng66/Linear-Algebra.svg?style=for-the-badge" alt="Issues"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey.svg?style=for-the-badge" alt="License"></a>
</p>

<p align="center">
  <a href="dist/from_zero_linear_algebra.pdf"><strong>Read the PDF</strong></a>
  ·
  <a href="README-zh.md"><strong>简体中文</strong></a>
  ·
  <a href="https://github.com/ShuoMeng66/Linear-Algebra/issues">Report Bug</a>
  ·
  <a href="https://github.com/ShuoMeng66/Linear-Algebra/issues">Request Feature</a>
</p>

## Table of Contents

- [About The Project](#about-the-project)
- [Built With](#built-with)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Repository Structure](#repository-structure)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## About The Project

![Cover Preview](assets/images/preview/cover.png)

`Linear-Algebra` is centered on a Chinese textbook project called `从零开始的线性代数教程`.

Instead of introducing linear algebra as a pile of disconnected definitions, this project follows a smoother learning path:

```text
Gaussian elimination and linear systems
-> basic matrix operations
-> eigenvalues and diagonalization
-> orthogonal diagonalization
-> quadratic forms and positive definiteness
```

The goal is simple: make the subject easier to start, easier to review, and easier to keep learning when someone gets stuck halfway through a problem.

This repository combines:

- a readable PDF textbook for beginners and make-up exam review
- full LaTeX source for open collaboration and long-term maintenance
- Cherry Studio assistant presets and a manually deployable learning Agent
- a tutoring skill tailored to the book instead of generic math chat
- a validation script used to re-check key examples, parameter problems, and answer hints

### Why this project exists

- Many students first meet linear algebra through fragmented formulas rather than a usable problem-solving path.
- Learners preparing for make-up exams often need common patterns, hand-computation practice, and mistake prevention more than abstract formalism.
- Beginner-facing Chinese materials are often either too compressed or too professional in tone.

### What makes this repository different

- It keeps a stable five-chapter storyline instead of drifting into disconnected topics.
- It stays friendly in tone and avoids unnecessarily rigid textbook language.
- It adds more exam-style multiple choice, fill-in, and computational practice around core chapters.
- It treats Cherry Studio as a study companion for this book, not as a generic answer bot.

<p align="right">(<a href="#top">back to top</a>)</p>

## Built With

- [XeLaTeX](https://www.latex-project.org/) for textbook typesetting
- [Python](https://www.python.org/) and [SymPy](https://www.sympy.org/) for content checks
- [Cherry Studio](https://docs.cherry-ai.com/cherry-studio/download) for study companion deployment
- Markdown and JSON for project documentation, prompts, and assistant configuration

<p align="right">(<a href="#top">back to top</a>)</p>

## Getting Started

### Prerequisites

- A LaTeX environment with `xelatex` available, such as TeX Live or MiKTeX
- Python 3 with `sympy` installed if you want to run the validation script
- Cherry Studio if you want to use the assistant subscription or the manual learning Agent

### Installation

1. Clone the repository.

   ```bash
   git clone git@github.com:ShuoMeng66/Linear-Algebra.git
   cd Linear-Algebra
   ```

2. Build the PDF from source.

   ```bash
   cd src
   xelatex -interaction=nonstopmode -halt-on-error from_zero_linear_algebra.tex
   xelatex -interaction=nonstopmode -halt-on-error from_zero_linear_algebra.tex
   ```

3. Optionally copy the generated PDF back into `dist/`.

   ```bash
   cp from_zero_linear_algebra.pdf ../dist/from_zero_linear_algebra.pdf
   ```

   On PowerShell, you can use:

   ```powershell
   Copy-Item from_zero_linear_algebra.pdf ..\dist\from_zero_linear_algebra.pdf
   ```

4. Optionally install validation dependencies and run the checker.

   ```bash
   cd ..
   python -m pip install sympy
   python scripts/validate_content.py
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

## Usage

### Read the textbook directly

If you only want to study the material, open:

```text
dist/from_zero_linear_algebra.pdf
```

### Import the Cherry Studio assistants

Use the public subscription file:

```text
https://raw.githubusercontent.com/ShuoMeng66/Linear-Algebra/main/cherry-studio/assistants.json
```

Useful files:

- `cherry-studio/assistants.json`
- `skills/from-zero-linear-algebra-tutor/SKILL.md`

### Manually create a Cherry Studio learning Agent

If you want a longer-term study companion, follow:

- `cherry-studio/agent-deployment.md`
- `cherry-studio/linear-algebra-learning-agent.prompt.md`

Safety note:

- Use `Normal` mode or `Plan` mode only.
- Do not enable `Full Auto` mode for this math learning Agent.

### Validate key content before publishing changes

The repository includes a checker for selected examples, parameter problems, and answer hints:

```bash
python scripts/validate_content.py
```

### Typical use cases

- beginner self-study
- make-up exam review
- classroom handout refinement
- Cherry Studio textbook tutoring
- future expansion into a larger public textbook project

<p align="right">(<a href="#top">back to top</a>)</p>

## Repository Structure

```text
.
├─ assets/
├─ cherry-studio/
├─ dist/
├─ scripts/
├─ skills/
├─ src/
├─ CONTRIBUTING.md
├─ LICENSE
├─ README.md
├─ README-zh.md
├─ RELEASE_NOTES.md
└─ THIRD_PARTY_ASSETS.md
```

Key directories:

- `src/`: LaTeX source for the textbook
- `dist/`: compiled PDF output
- `scripts/`: validation utilities
- `cherry-studio/`: assistant subscription, Agent deployment guide, and prompt files
- `skills/`: the tutoring skill and its references
- `assets/`: cover images, preview images, and other visual resources

<p align="right">(<a href="#top">back to top</a>)</p>

## Roadmap

- [ ] Add more rigorously checked multiple choice and fill-in exercises for high-frequency topics
- [ ] Expand chapter-by-chapter operation workflows for the most important problem types
- [ ] Publish a more complete companion answer and explanation set
- [ ] Package versioned GitHub releases with attached PDF artifacts
- [ ] Continue improving Cherry Studio tutoring prompts, safety guidance, and learning flows

See the [open issues](https://github.com/ShuoMeng66/Linear-Algebra/issues) for more ideas and ongoing discussion.

<p align="right">(<a href="#top">back to top</a>)</p>

## Contributing

Contributions are welcome, especially when they improve mathematical accuracy, beginner readability, exercise quality, or Cherry Studio learning support.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Good contributions for this project usually include:

- correcting mathematical errors or weak explanations
- adding representative three-by-three examples and carefully verified exercises
- improving Cherry Studio prompts, tutoring flows, and deployment documentation
- refining the public-facing documentation for readers and contributors

If you plan to contribute new media assets, please also review [THIRD_PARTY_ASSETS.md](THIRD_PARTY_ASSETS.md) first.

<p align="right">(<a href="#top">back to top</a>)</p>

## License

This repository is a public educational project, but it is **not** released under a standard software OSS license.

The original textbook text, LaTeX structure, teaching notes, Cherry Studio prompts, assistant configuration, and documentation are released under:

- `CC BY-NC-SA 4.0`

Important notes:

- attribution is required
- commercial reuse is not allowed without separate permission
- derivative public releases should keep the same or a compatible non-commercial share-alike license
- third-party images, logos, and externally sourced visual assets are **not** covered by that license

Please read [LICENSE](LICENSE) and [THIRD_PARTY_ASSETS.md](THIRD_PARTY_ASSETS.md) carefully before redistribution, remixing, or reuse.

<p align="right">(<a href="#top">back to top</a>)</p>

## Contact

ShuoMeng66

- GitHub: [@ShuoMeng66](https://github.com/ShuoMeng66)
- Email: `3067938917@qq.com`
- Project Link: [https://github.com/ShuoMeng66/Linear-Algebra](https://github.com/ShuoMeng66/Linear-Algebra)

<p align="right">(<a href="#top">back to top</a>)</p>

## Acknowledgments

- [Best README Template](https://github.com/othneildrew/Best-README-Template)
- [Cherry Studio Documentation](https://docs.cherry-ai.com/)
- [SymPy](https://www.sympy.org/)

<p align="right">(<a href="#top">back to top</a>)</p>
