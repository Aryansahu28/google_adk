from google.adk.agents.llm_agent import Agent
from refund_policy_mini_project.tools import (
    get_student_detail,
    update_refund_status,
    get_refund_policy
)

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful saviour company refund assistant for enrolled students.',
    instruction="""You are Saviour company refund agent and assistant ask the user its email first who is asking for refund of our course check whether he enrolled or not then continue on the basis and follow these steps:-
    1. Check our refund policy and eligibility criterion for call tool get_refund_policy
    2. If it is under our refund policy then call the tool update_refund_status

    Check the student information first then ask any further question
    Update the refund status pending when the refund is considered and student is eligible. Never update the table with active or not-applicable
    """,
    tools = [get_student_detail,update_refund_status,get_refund_policy]
)
