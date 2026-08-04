import asyncio
from autogen_code_review.agents import coding_agent, reviewer_agent

async def main():
    # Step 1: Generate code
    coding_result = await coding_agent.run(
        task="Write a Python function to validate Indian phone numbers."
    )
    generated_code = coding_result.messages[-1].content

    print("=" * 80)
    print("CODING AGENT OUTPUT")
    print("=" * 80)
    print(generated_code)

    # Step 2: Ask reviewer to review it
    review_result = await reviewer_agent.run(
        task=f"""
Review the following Python code.

Please check:
1. Bugs
2. Edge cases
3. Readability
4. PEP 8
5. Documentation

Code:

{generated_code}
"""
    )

    review = review_result.messages[-1].content

    print("\n")
    print("=" * 80)
    print("REVIEWER OUTPUT")
    print("=" * 80)
    print(review)


if __name__ == "__main__":
    asyncio.run(main())