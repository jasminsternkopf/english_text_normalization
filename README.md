# english-text-normalization

[![PyPI](https://img.shields.io/pypi/v/english-text-normalization.svg)](https://pypi.python.org/pypi/english-text-normalization)
[![PyPI](https://img.shields.io/pypi/pyversions/english-text-normalization.svg)](https://pypi.python.org/pypi/english-text-normalization)
[![MIT](https://img.shields.io/github/license/jasminsternkopf/english_text_normalization.svg)](https://github.com/jasminsternkopf/english_text_normalization/blob/main/LICENSE)

CLI and library to normalize English texts.

## Installation

```sh
pip install english-text-normalization --user
```

## Usage as CLI

```sh
# Show supported normalizing operations
norm-eng-cli list-operations -h

# Normalize
norm-eng-cli normalize -h
```

## Usage as a library

```py
from english_text_normalization import *
```

### Methods

- `expand_abbreviations`
- `normalize_am_and_pm`
- ...

### Dependencies

- pyenchant
- nltk
- inflect

## Contributing

If you notice an error, please don't hesitate to open an issue.

## Citation

If you want to cite this repo, you can use this BibTeX-entry:

```bibtex
@misc{stetn22,
  author = {Sternkopf, Jasmin and Taubert, Stefan},
  title = {english-text-normalization},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/jasminsternkopf/english_text_normalization}}
}
```
