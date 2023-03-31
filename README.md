# matter-api-client

**Table of Contents**

- [Installation](#installation)
- [License](./LICENSE)

## Getting started

After you have created a project using this template, rename all occurrences of *matter_library_template*
to the new library's name.

## Installation

```console
pip install matter-api-client
```

## Contributing

Make sure you have all supported python versions installed in your machine:

* 3.10
* 3.11

### Install hatch in your system

```https://hatch.pypa.io/latest/install/```

### Create the environment

```console
hatch env create
```

Do your changes...

### Run the tests

```console
hatch run test
```

The command above will run the tests against all supported python versions
installed in your machine. For testing in other operating system you may use the
configured CI in github. 

### Bump a new version

In general, you just need to execute:

```console
hatch version
```

This command will update the minor version. i.e.:
No breaking changes and new feature has been added

We are using [semantic version](https://semver.org/), if you are doing a bug fix:

```console
hatch version fix
```

## Github workflows

If you want to reuse fully the github actions defined by this template make sure your [workflow permissions for Actions](../../settings/actions) settings is configured as followed: 


![image](https://user-images.githubusercontent.com/349498/227478670-37eed4c1-151a-4bd7-8e97-ed3395047942.png)

