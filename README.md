HotBits Python API
=========================

[![Latest Version][icon-version]][link-pypi]
[![Total Downloads][icon-downloads]][link-pypi]
[![License][icon-license]][link-license]
[![Build Status][icon-travis]][link-travis]

Python API for HotBits random data generator.

## Description

This project is random data generator. It uses is HotBits API web service for radioactively-generated random data.

The web service generates random data. Without API token, only pseudorandom data will be returned. For radioactively-generated random data, you would need to [request free API key][link-apikey].

**The project is not part of the HotBits. It is just API client for it, made by community. For any information about HotBits, you should use [the official website][link-hotbits].**

## Usage

First, you need to import the generator class:

```python
from hotbits import RandomDataGenerator
```

Then you need to init the generator client, with default service URL:

```python
generator = RandomDataGenerator()
```

Custom URL can be changed with parameters:

```python
generator = RandomDataGenerator(custom_url='https://example.com')
```

You can then generate data with specific length and API key:

```python
result = generator.generate(
    length='256',
    apikey='exampleAPIkey'
)
```

Length of 128 bytes is used by default. If no API key is specified, pseudorandom data will be returned.

Random data are returned as list:

```python
print(result[0]) # First byte
print(result[1]) # Second byte
print(result[3]) # Third byte
```

You can also look to [example file][link-example] for more examples.

## Versioning

This library uses [SemVer][link-semver] for versioning. For the versions available, see [the tags][link-tags] on this repository.

## License

This library is licensed under the GPLv3+ license. See the [LICENSE][link-license-file] file for details.

[icon-version]: https://img.shields.io/pypi/v/hotbits.svg?style=flat-square&label=version
[icon-downloads]: https://img.shields.io/pypi/dm/hotbits.svg?style=flat-square&label=downloads
[icon-license]: https://img.shields.io/pypi/l/hotbits.svg?style=flat-square&label=license
[icon-travis]: https://img.shields.io/travis/com/filips123/HotBitsPy.svg?style=flat-square&label=build+status

[link-pypi]: https://pypi.org/project/hotbits/
[link-license]: https://choosealicense.com/licenses/gpl-3.0/
[link-semver]: https://semver.org/
[link-travis]: https://travis-ci.com/filips123/HotBitsPy/

[link-example]: https://github.com/filips123/HotBitsPy/blob/master/example.py
[link-tags]: https://github.com/filips123/HotBitsPy/tags/
[link-license-file]: https://github.com/filips123/HotBitsPy/blob/master/LICENSE

[link-hotbits]: https://www.fourmilab.ch/hotbits/
[link-apikey]: https://www.fourmilab.ch/hotbits/apikey_request.html
