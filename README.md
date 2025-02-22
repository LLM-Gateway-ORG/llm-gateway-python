<br/>
<p align="center">
  <a href="https://github.com/LLM-Gateway-ORG/llm-gateway-core">
    <img src="https://socialify.git.ci/LLM-Gateway-ORG/llm-gateway-core/image?description=1&forks=1&issues=1&language=1&name=1&owner=1&pattern=Circuit%20Board&pulls=1&stargazers=1&theme=Dark" alt="llm-gateway-core" width="640" height="320" />
  </a>

  <p align="center">
    A Python package to access different LLMs, embeddings, vector stores etc.
    <br/>
    <br/>
    <a href="https://github.com/LLM-Gateway-ORG/llm-gateway-core"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com/LLM-Gateway-ORG/llm-gateway-core">View Demo</a>
    .
    <a href="https://github.com/LLM-Gateway-ORG/llm-gateway-core/issues">Report Bug</a>
    .
    <a href="https://github.com/LLM-Gateway-ORG/llm-gateway-core/issues">Request Feature</a>
  </p>
</p>

<p align="center">
    <img alt="Update Models List" src="https://github.com/LLM-Gateway-ORG/llm-gateway-core/actions/workflows/model_list_updater.yml/badge.svg" />
    <img alt="Downloads" src="https://img.shields.io/github/downloads/LLM-Gateway-ORG/llm-gateway-core/total" />
    <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/LLM-Gateway-ORG/llm-gateway-core?color=dark-green" />
    <img alt="Github Issues" src="https://img.shields.io/github/issues/LLM-Gateway-ORG/llm-gateway-core" />
    <img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/LLM-Gateway-ORG/llm-gateway-core" />
    <img alt="Repo Size" src="https://img.shields.io/github/repo-size/LLM-Gateway-ORG/llm-gateway-core" />
    <img alt="GitHub Pull Requests" src="https://img.shields.io/github/issues-pr/LLM-Gateway-ORG/llm-gateway-core" />
    <img alt="Github License" src="https://img.shields.io/github/license/LLM-Gateway-ORG/llm-gateway-core" />
    <img alt="Deploy Docs" src="https://github.com/LLM-Gateway-ORG/llm-gateway-core/actions/workflows/deploy-docs.yml/badge.svg" />


</p>

## Table Of Contents

* [About the Project](#about-the-project)
* [Features](#features)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)

## About The Project

**LLM Gateway Core** is a Python package that simplifies access to different LLMs, embeddings, vector stores, etc. With the help of credentials (API key, username, password, etc.), you can access any LLM provider with a single package.

## Features

**Milap** comes with a multitude of features:

- **Create Google Meetings**: Automate the process of scheduling new Google meetings. Customize settings such as date, time, participants, and more.
- **Update Existing Meetings**: Modify details of scheduled meetings, such as changing the time, adding participants, or updating the agenda.
- **Delete Meetings**: Provides functionality to cancel meetings, which can be integrated into various applications to handle schedule changes dynamically.
- **Fetch Meeting Information**: Retrieve details about meetings, including participant lists, meeting times, and links, which can be used for reminders, attendance tracking, and more.


## Getting Started

To install Milap, follow these steps:

### Prerequisites

1. [Python >=3.9](https://www.python.org/)

### Installation

With pip:

```sh
pip install llm-gateway-core
```

With Poetry:

```sh
peotry add llm-gateway-core
```

## Usage

#### For Synchronous Communication

```python
chat_obj = Chat(
    model_name="groq/gemma2-9b-it",
    sync=False,
    api_key="<api-key>",
)
response = await chat_obj.generate(
    [{"role": "user", "content": "How are you?"}]
)
```

#### For Asynchronous Communication

```python
import asyncio
async def main():
    chat_obj = Chat(
        model_name="groq/gemma2-9b-it",
        sync=False,
        api_key="<api-key>",
    )
    response = await chat_obj.generate(
        [{"role": "user", "content": "How are you?"}]
    )
    async for chunk in response:
        print(chunk.choices[0].delta.content, end="")

asyncio.run(main())
```

Read the Documentation [here](https://github.com/LLM-Gateway-ORG/llm-gateway-core/blob/main/example/sample.py)


## Roadmap

See the [open issues](https://github.com/LLM-Gateway-ORG/llm-gateway-core/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/LLM-Gateway-ORG/llm-gateway-core/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/<feature>`)
3. Commit your Changes (`git commit -m 'Add some <feature>'`)
4. Push to the Branch (`git push origin feature/<feature>`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/LLM-Gateway-ORG/llm-gateway-core/blob/main/LICENSE) for more information.

## Contact
**Subhomoy Roy Choudhury** - [Github](https://src-portfolio.oderna.in/link/GITHUB) - [Linkedin](https://src-portfolio.oderna.in/link/LINKEDIN) - [Twitter](https://src-portfolio.oderna.in/link/TWITTER)

Project Link: [https://github.com/LLM-Gateway-ORG/llm-gateway-core](https://github.com/LLM-Gateway-ORG/llm-gateway-core)

## Acknowledgements

* [Poetry](https://www.poetryfoundation.org/)
* [Beautify Github Readme](https://github.com/rzashakeri/beautify-github-profile)
* [LiteLLM](https://www.litellm.ai/)
* [Huggingface](https://huggingface.co/)
