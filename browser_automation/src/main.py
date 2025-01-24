from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="search for holidaychecks job website. Fill out the application for all for sotware engineer. My name is richard knoche. If they ask for some informations make them up. before submitting ask for confirmation before submitting.",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
