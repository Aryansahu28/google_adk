import uuid

from google import genai
from google.adk.tools import ToolContext
from google.genai import types

# Initialize the GenAI client (automatically reads GOOGLE_API_KEY from .env)
client = genai.Client()


async def generate_image(prompt: str, tool_context: ToolContext) -> dict:
    """Generates an image from a text prompt and saves it as an ADK artifact.

    Args:
        prompt: A detailed description of the image to generate.
        tool_context: The ADK tool context used to save the image artifact.

    Returns:
        A dictionary containing the status, filename, and artifact version.
    """
    try:
        # 1. Call the Gemini image generation model
        response = await client.aio.models.generate_content(
            model="gemini-nano-banana-2.1",
            contents=prompt,
        )

        # 2. Extract the image bytes and MIME type from the response
        image_bytes = None
        mime_type = "image/png"

        for part in response.candidates[0].content.parts: # type: ignore
            if part.inline_data is not None:
                image_bytes = part.inline_data.data
                mime_type = part.inline_data.mime_type or "image/png"
                break

        if not image_bytes:
            return {
                "status": "error",
                "message": "The model did not return any image data.",
            }

        # 3. Wrap the raw bytes into a types.Part object
        image_part = types.Part.from_bytes(
            data=image_bytes,
            mime_type=mime_type,
        )

        # 4. Save the image as an artifact so ADK Web UI can render/download it
        extension = mime_type.split("/")[-1]
        filename = f"generated_{uuid.uuid4().hex[:8]}.{extension}"
        version = await tool_context.save_artifact(
            filename=filename,
            artifact=image_part,
        )

        return {
            "status": "success",
            "filename": filename,
            "version": version,
            "message": f"Image successfully generated and saved as '{filename}'.",
        }

    except Exception as e:  # noqa: BLE001
        return {
            "status": "error",
            "message": f"Image generation failed: {e!s}",
        }