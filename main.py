from dotenv import load_dotenv
load_dotenv()
from langgraph.graph import StateGraph
import agents
from typing import TypedDict

reviewer_credibility_agent = agents.reviewer_credibility_agent
content_authenticity_agent = agents.content_authenticity_agent
purchase_verification_agent = agents.purchase_verification_agent
final_decision_agent = agents.final_decision_agent

class ReviewState(TypedDict):
    # Initial inputs
    reviewer_info: str
    review_text: str
    purchase_info: str
    # Agent outputs
    reviewer_result: str
    content_result: str
    purchase_result: str
    final_result: str

def load_input_from_file(file_path="input.txt"):
    with open(file_path, "r") as f:
        content = f.read()

    sections = {}
    current_section = None

    for line in content.splitlines():
        line = line.strip()
        if not line:
            continue

        if line.startswith("[") and line.endswith("]"):
            current_section = line[1:-1]
            sections[current_section] = []
        else:
            sections[current_section].append(line)

    return {
        "reviewer_info": " ".join(sections.get("REVIEWER_INFO", [])),
        "review_text": " ".join(sections.get("REVIEW_TEXT", [])),
        "purchase_info": " ".join(sections.get("PURCHASE_INFO", [])),
    }

def input_node(state):
    return state

graph = StateGraph(ReviewState)

graph.add_node("input", input_node)
graph.add_node("reviewer_agent", reviewer_credibility_agent)
graph.add_node("content_agent", content_authenticity_agent)
graph.add_node("purchase_agent", purchase_verification_agent)
graph.add_node("final_agent", final_decision_agent)

graph.set_entry_point("input")

# Fan-out from input
graph.add_edge("input", "reviewer_agent")
graph.add_edge("input", "content_agent")
graph.add_edge("input", "purchase_agent")

# Fan-in to final
graph.add_edge("reviewer_agent", "final_agent")
graph.add_edge("content_agent", "final_agent")
graph.add_edge("purchase_agent", "final_agent")

graph.set_finish_point("final_agent")

app = graph.compile()


# ----------- TEST INPUT -----------
input_state = load_input_from_file("input.txt")

# print("INPUT_STATE", input_state)
result = app.invoke(input_state)

print("\nFINAL SYSTEM OUTPUT:\n")
print(result["final_result"])
