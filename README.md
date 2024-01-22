# NiceLLM: A Python LLM toolkit

## About

NiceLLM is a Python package that homologates mainstream libraries of Large Language Models (LLMs), such as OpenAI and Google Generative AI, into a unique and simple interface for the user.

## Main Features

- Simplified handling of API connections
- Simplified interface to use images in the prompt

## Installation

The source code can be found at https://github.com/cnavarreteliz/nicellm.

```
pip install nicellm
```

## Usage

```
import nicellm as llm

llm.get_response(
    model_id="gpt-3.5-turbo",
    prompt="Who is the best LLM in the world?"
)
```

## Contributions

All contributions and ideas are welcome and well received. Please send us your PRs, and we will revise them as soon as possible.

## License

This project is under an MIT-License.
