# NiceLLM: A Python LLM toolkit

## About

NiceLLM is a Python package that homologates mainstream library functions of Large Language Models (LLMs), such as OpenAI, MistralAI, and Google Generative AI, into a unique and simple interface for the user.

## Main Features

- Simplified handling of API connections
- Simplified interface to use images in the prompt

## Installation

The source code can be found at https://github.com/idealab-udec/nicellm.

```
pip install nicellm
```

## Initial config

To initialize the functions of `nicellm`, you will need to set some environment variables, which will contain the API keys for OpenAI and Google Generative AI. We suggest to create a file called `.env` in your root folder with the following information:

```
APIKEY_GOOGLE="YOUR-API-KEY-FROM-GENERATIVE-AI"
APIKEY_OPENAI="YOUR-API-KEY-FROM-OPEN-AI"
APIKEY_MISTRAL="YOUR-API-KEY-FROM-MISTRAL"
```

It is not mandatory to set up all env variables. However, you must set up at least the ones corresponding to the models you want to use.

To obtain your API keys, please visit:

- OpenAI: https://platform.openai.com/account/api-keys
- Google Generative AI: https://makersuite.google.com/app/apikey
- Mistral AI: https://console.mistral.ai/user/api-keys/

## Usage

Interact with `gpt-3.5-turbo`:

```
import nicellm as llm

llm.get_response(
    model_id="gpt-3.5-turbo",
    prompt="Who is the best LLM in the world?"
)
```

The same question can be easily replicated using `gemini-pro`:

```
llm.get_response(
    model_id="gemini-pro",
    prompt="Who is the best LLM in the world?"
)
```

By using `mistral-tiny`:

```
llm.get_response(
    model_id="mistral-tiny",
    prompt="Who is the best LLM in the world?"
)
```

## Contributions

This project is maintained by the Interdisciplinary Education & Artificial Intelligence Lab, IDEALAB, from the University of Concepción, Chile.

All contributions and ideas are welcome and well received. Please send us your PRs, and we will revise them as soon as possible.

## License

This project is under an MIT-License.
