from google.adk.agents.llm_agent import Agent
from image_generation_app.generate_images import generate_image


root_agent = Agent(
    name="image_generator_agent",
    model="gemini-3.8-flash",
    description="An agent that generates images based on user prompts.",
    instruction=(
        "You are a helpful creative assistant. Whenever a user asks you to "
        "create, draw, or generate an image, expand their idea into a clear, "
        "descriptive prompt and call the `generate_image` tool. Once saved, "
        "confirm the filename to the user."
    ),
    tools=[generate_image],
)