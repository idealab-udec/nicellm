import base64
import PIL
import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

from dotenv import load_dotenv
import google.generativeai as genai
from openai import OpenAI

load_dotenv()

if os.getenv("APIKEY_GOOGLE"):
    genai.configure(api_key=os.getenv("APIKEY_GOOGLE"))

if os.getenv("APIKEY_OPENAI"):
    client = OpenAI(api_key=os.getenv("APIKEY_OPENAI"))

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def get_response(
    model_id,
    prompt,
    temperature: float=0,
    role: str="",
    image_path=None,
    **kwargs
) -> str:
    """Gets the response from a text- or image-based model. This function also includes the most common config parameters. However, users can set up all parameters defined by the official API documentation of OpenAI and Google Generative AI through `kwargs` parameter.

    Parameters
    ----------
    model_id : str
        The model identifier. They can be displayed using `llm.list_models()` function.
    prompt : str
        A prompt provided by the user.
    role : str
        A prompt to designate a specific role to the model.
    temperature : float, by default 0.
        The creativity of responses. Values range from 0 to 1 for Google models and from 0 to 2 for OpenAI models.
    image_path : str
        The local location of the image. Format accepted are .png and .jpeg.
    kwargs : dict
        Other parameters are passed through to the API functions.

    Returns
    -------
    str
        Response from the LLM
    """
    
    if model_id in [m.id for m in client.models.list()]:
        messages = [
            {"role": "system", "content": role},
            {"role": "user", "content": [
               {"type": "text", "text": prompt} 
            ]}
        ]

        if image_path:
            messages[1]["content"].append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{encode_image(image_path)}"
                }
            })

        completion = client.chat.completions.create(
            model=model_id,
            temperature=temperature,
            messages=messages,
            **kwargs
        )

        return completion.choices[0].message.content

    elif model_id in [m.name for m in genai.list_models() if "generateText" in m.supported_generation_methods]:
        completion = genai.generate_text(
            model=model_id,
            prompt=[role, prompt],
            temperature=temperature,
            **kwargs
        )

        return completion.result
    
    elif model_id in [m.name.split("/")[1] for m in genai.list_models()]:
        model = genai.GenerativeModel(model_id)
        messages = [role, prompt]

        if image_path:
            messages.append(PIL.Image.open(image_path))

        completion = model.generate_content(
            messages,
            generation_config=dict(temperature=temperature),
            **kwargs
        )
        
        return completion.text


    return "Model not found"


def list_models(
    owner: str="openai"
) -> list:
    """List all available models.

    Parameters
    ----------
    owner : str, values accepted are "openai" and "google"
        The official provider, by default "openai"

    Returns
    -------
    list
        A list with the available models listed by the owner.
    """
    if owner == "openai":
        return [m.id for m in client.models.list()]
    elif owner == "google":
        return [m.name.split("/")[1] for m in genai.list_models()]