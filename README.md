# PyMed-iplweb - PubMed Access through Python

[![PyPI version](https://img.shields.io/pypi/v/pymed-iplweb.svg)](https://pypi.python.org/pypi/pymed-iplweb)
[![Tests](https://github.com/mpasternak/pymed-iplweb/actions/workflows/tests.yml/badge.svg?branch=develop)](https://github.com/mpasternak/pymed-iplweb/actions/workflows/tests.yml)
[![Python versions](https://img.shields.io/pypi/pyversions/pymed-iplweb.svg)](https://pypi.python.org/pypi/pymed-iplweb)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/mpasternak/pymed-iplweb/blob/master/LICENCE)

PyMed is a Python library that provides access to PubMed through the PubMed API. This is a fork, maintained by https://IPLweb.pl

## Supported versions

| Python | Django 4.2 LTS | Django 5.0 | Django 5.1 | Django 5.2 LTS | Django 6.0 |
|--------|:--------------:|:----------:|:----------:|:--------------:|:----------:|
| 3.10   | ✅             | ✅         | ✅         | ✅             | —          |
| 3.11   | ✅             | ✅         | ✅         | ✅             | —          |
| 3.12   | ✅             | ✅         | ✅         | ✅             | ✅         |
| 3.13   | —              | —          | ✅         | ✅             | ✅         |

Django is an optional dependency.

## Why this library?

The PubMed API is not very well documented and querying it in a performant way is too complicated and time consuming for researchers. This wrapper provides access to the API in a consistent, readable and performant way.

## Features

This library takes care of the following for you:

- Querying the PubMed database (with the standard PubMed query language)
- Batching of requests for better performance
- Parsing and cleaning of the retrieved articles

## Examples

For full (working) examples have a look at the `examples/` folder in this repository. In essence you only need to import the `PubMed` class, instantiate it, and use it to query:

```python
from pymed import PubMed
pubmed = PubMed(tool="MyTool", email="my@email.address")
results = pubmed.query("Some query", max_results=500)
```

## Notes on the API

The original documentation of the PubMed API can be found here: [PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/tools/developers/). PubMed Central kindly requests you to:

> - Do not make concurrent requests, even at off-peak times; and
> - Include two parameters that help to identify your service or application to our servers
>   - *tool* should be the name of the application, as a string value with no internal spaces, and
>   - *email* should be the e-mail address of the maintainer of the tool, and should be a valid e-mail address.

## Notice of Non-Affiliation and Disclaimer

The author of this library is not affiliated, associated, authorized, endorsed by, or in any way officially connected with PubMed, or any of its subsidiaries or its affiliates. The official PubMed website can be found at https://www.ncbi.nlm.nih.gov/pubmed/.

## License

This project is licensed under the MIT License - see the [LICENCE](LICENCE) file for details.
