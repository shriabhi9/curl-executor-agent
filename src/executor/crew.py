from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators
from tools.api_caller_tool import ApiCallerTool
@CrewBase
class Executor():
    """Executor crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def curl_interpreter_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['curl_interpreter_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def api_executor_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['api_executor_agent'], # type: ignore[index]
            tools=[ApiCallerTool()],
            verbose=True
        )
    @agent
    def api_response_summarizer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['api_response_summarizer_agent'], # type: ignore[index]
            verbose=True
        )
    @agent
    def api_response_parser_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['api_response_parser_agent'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def parse_curl_json_task(self) -> Task:
        return Task(
            config=self.tasks_config['parse_curl_json_task'], # type: ignore[index]
        )

    @task
    def execute_api_task(self) -> Task:
        return Task(
            config=self.tasks_config['execute_api_task'], # type: ignore[index]
        )
    @task
    def summarize_response_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarize_response_task'], # type: ignore[index]
           
        )
    @task
    def structure_response_task(self) -> Task:
        return Task(
            config=self.tasks_config['structure_response_task'], # type: ignore[index]
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Executor crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
