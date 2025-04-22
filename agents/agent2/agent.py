# agents/agent1/agent.py

import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

def get_weather(city: str) -> dict:
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": "The weather in New York is sunny with 25°C (77°F).",
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }

def get_current_time(city: str) -> dict:
    if city.lower() == "new york":
        tz = ZoneInfo("America/New_York")
    else:
        return {
            "status": "error",
            "error_message": f"No timezone info for {city}."
        }
    now = datetime.datetime.now(tz)
    return {
        "status": "success",
        "report": f"The current time in {city} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"
    }

agent = Agent(
    name="agent2",
    model="gemini-2.0-flash",
    description="Agent2 that answers questions about time and weather and your name is agent2.",
    instruction="You are a helpful assistant that knows time and weather.",
    tools=[get_weather, get_current_time]
)
