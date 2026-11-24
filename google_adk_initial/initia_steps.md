# CampusX Bot --- Setup and Run Guide

Follow these steps to create and run the agent project.

## 1. Create a project folder

Create a folder for the project and open it in VS Code.

## 2. Create a virtual environment

``` bash
python3 -m venv .venv
```

## 3. Activate the virtual environment

**macOS / Linux:**

``` bash
source .venv/bin/activate
```

**Windows (PowerShell):**

``` powershell
.venv\Scripts\Activate.ps1
```

## 4. Install Google ADK

``` bash
pip install google-adk
```

## 5. Check the ADK version

``` bash
adk --version
```

## 6. Create the agent project

``` bash
adk create campusx_bot
```

## 7. Get a Gemini API key

Get a Gemini API key and add it to your project's `.env` file.

## 8. Run the agent

``` bash
adk run campusx_bot
```

## 9. Run the web interface

``` bash
adk web
```

## 10. Run the API service

``` bash
adk api_server
```

## 11. Run the agent with other models

1.  Install LiteLLM:

    ``` bash
    pip install litellm
    ```

2.  Set the model in your agent configuration:

    ``` python
    model = LiteLlm(model="openai/gpt-4o")
    ```

3.  Get an OpenAI API key and add it to your `.env` file.

## 12. Add model configuration

The visible note in the source image shows the following configuration:

``` python
generate_content_config = types.GenerateContentConfig(
    temperature=0.3,  # Lower values give more consistent support answers
)
```

> **Note:** The source image cuts off after the `temperature` comment,
> so this last configuration is transcribed only from the visible
> portion.
