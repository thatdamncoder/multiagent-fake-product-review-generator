from langchain_google_genai import ChatGoogleGenerativeAI
import prompts

REVIEWER_CREDIBILITY_PROMPT = prompts.REVIEWER_CREDIBILITY_PROMPT
CONTENT_AUTHENTICITY_PROMPT = prompts.CONTENT_AUTHENTICITY_PROMPT
PURCHASE_VERIFICATION_PROMPT = prompts.PURCHASE_VERIFICATION_PROMPT
FINAL_DECISION_PROMPT = prompts.FINAL_DECISION_PROMPT

# Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0
)

def reviewer_credibility_agent(state):
    response = llm.invoke(
        REVIEWER_CREDIBILITY_PROMPT +
        f"\n\nInput:\n{state['reviewer_info']}"
    )
    return {"reviewer_result": response.content}

def content_authenticity_agent(state):
    response = llm.invoke(
        CONTENT_AUTHENTICITY_PROMPT +
        f"\n\nReview:\n{state['review_text']}"
    )
    return {"content_result": response.content}

def purchase_verification_agent(state):
    response = llm.invoke(
        PURCHASE_VERIFICATION_PROMPT +
        f"\n\nInput:\n{state['purchase_info']}"
    )
    return {"purchase_result": response.content}

def final_decision_agent(state):
    combined_input = f"""
        Reviewer Result:
        {state['reviewer_result']}

        Content Result:
        {state['content_result']}

        Purchase Result:
        {state['purchase_result']}
        """
    response = llm.invoke(
        FINAL_DECISION_PROMPT + combined_input
    )
    return {"final_result": response.content}
