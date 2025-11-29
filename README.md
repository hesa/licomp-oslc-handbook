# licomp-oslc-handbook (Licomp Open Source License Compliance Handbook)

Licomp OSLC-Handbook provides compatibility data:

* between an Open Source outbound license and inbound Open Source licenses
* when distributing a binary, linking to (e.g. linking to a library) Open Source components
* the Open Source components are unmodified

Licomp OSLC Handbook uses Open Source License Compliance Handbook by The Fintech Open Source Foundation (www.finos.org).

## Introduction 

Licomp OSLC Handbook implements the [Licomp](https://github.com/hesa/licomp) api for communication with the Licomp resources. For a better understanding of Licomp we suggest you read:

* [Licomp basic concepts](https://github.com/hesa/licomp/#licomp-concepts)
* [Licomp reply format](https://github.com/hesa/licomp/blob/main/docs/reply-format.md)

The various licomp resources below can be accessed as a group by:
* [licomp-toolkit](https://github.com/hesa/licomp-toolkit) - (`pip install licomp-toolkit`)

Licomp is used be the following compatibility resources:
* [licomp-hermione](https://github.com/hesa/licomp-hermione) - (`pip install licomp-hermione`)
* [licomp-proprietary](https://github.com/hesa/licomp-proprietary) - (`pip install licomp-proprietary`)
* [licomp-reclicense](https://github.com/hesa/licomp-reclicense) - (`pip install licomp-reclicense`)
* [licomp-dwheeler](https://github.com/hesa/licomp-dwheeler) - (`pip install licomp-dwheeler`)
* [licomp-osadl](https://github.com/hesa/licomp-osadl) - (`pip install licomp-osadl`)

# Using Licomp OSLC-Handbook

Since Licomp OSLC-Handbook implements [Licomp](https://github.com/hesa/licomp) we refer to the Licomp guides (both cli and python api).

## Command line interface

See [Licomp Comand Line Interface](https://github.com/hesa/licomp/blob/main/docs/cli-guide.md)

_Note: the commmad line program for Licomp OSLC-Handbook is called `licomp-oslc-handbook`._

## Python module

See [Licomp Python API](https://github.com/hesa/licomp/blob/main/docs/python-api.md)

# Installing Licomp OSLC Handbook

## From pypi.org

Licomp OSLC Handbook is available via [pypi.org](https://pypi.org/) at: [https://pypi.org/project/licomp-oslc-handbook/](https://pypi.org/project/licomp-oslc-handbook/).


To install, simply do the following:

```
$ pip install licomp-oslc-handbook
```

## From github

Installing from github assumes you already have `pip` installed.

```
$ git clone https://github.com/hesa/licomp-oslc-handbook
$ pip install -r requirements.txt
$ pip install -r requirements-dev.txt
$ pip install .
```


