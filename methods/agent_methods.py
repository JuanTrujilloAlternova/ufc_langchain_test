from langchain.agents import create_openai_functions_agent, AgentExecutor

def initialize_openai_agent(llm, prompt, tools, memory):
    agent = create_openai_functions_agent(
        llm=llm,
        prompt=prompt,
        tools=tools,
    )
    return AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory
    )
