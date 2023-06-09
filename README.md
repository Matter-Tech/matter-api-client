# matter-api-client

**Table of Contents**

- [Installation](#installation)
- [License](./LICENSE)

## Background

The Matter API Client Library in Python is a comprehensive tool for making HTTP/HTTPS API calls to other web services. It is designed to simplify the process of making API calls and handling the responses. The library supports both synchronous and asynchronous operations, allowing developers to choose the best approach for their use case.

One of the key features of the library is its ability to send JSON payloads, making it easy to work with APIs that require JSON data. It also automatically parses JSON responses, saving developers time and effort.

The library is designed with reliability in mind. It includes built-in error handling to catch client connection errors and throw exceptions when necessary. This ensures that developers can quickly identify and fix issues that may arise during API calls.

To further improve reliability, the library includes auto-retry functionality. This means that if an API call fails due to a network issue or other transient error, the library will automatically retry the call. This helps to ensure that the application can continue to function even in the face of occasional network disruptions.

Overall, the Python API Client Library is a powerful and flexible tool that can help developers to quickly and easily integrate with a wide range of APIs. With support for JSON payloads, automatic parsing of responses, error handling, and auto-retries, it is a reliable and robust solution for any project that requires API integration.



## Installation

```console
pip install matter-api-client
```

Also, make sure to set the following ENV variables:
```console
SERVER_LOG_LEVEL=debug or info or error
```


## Usage

### Sync API Calls:

Get:
```python
from matter_api_client.http_client import get
result = get(url="some url")
```

Post:
```python
from matter_api_client.http_client import post
result = post(url="some url", payload=payload, headers=headers)
```

Put:
```python
from matter_api_client.http_client import put
result = put(url="some url", payload=payload, headers=headers)
```

Delete:
```python
from matter_api_client.http_client import delete
result = delete(url="some url", payload=payload, headers=headers)
```

### Async API Calls:

Get:
```python
from matter_api_client.http_client_async import get
result = await get(url="some url")
```

Post:
```python
from matter_api_client.http_client_async import post
result = await post(url="some url", payload=payload, headers=headers)
```

Put:
```python
from matter_api_client.http_client_async import put
result = await put(url="some url", payload=payload, headers=headers)
```

Delete:
```python
from matter_api_client.http_client_async import delete
result = await delete(url="some url", payload=payload, headers=headers)
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

