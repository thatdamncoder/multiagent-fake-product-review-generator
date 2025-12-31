from langgraph.graph import StateGraph
import agents

reviewer_credibility_agent = agents.reviewer_credibility_agent
content_authenticity_agent = agents.content_authenticity_agent
purchase_verification_agent = agents.purchase_verification_agent
final_decision_agent = agents.final_decision_agent

class ReviewState(dict):
    pass

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

graph = StateGraph(ReviewState)

# Add nodes
graph.add_node("reviewer_agent", reviewer_credibility_agent)
graph.add_node("content_agent", content_authenticity_agent)
graph.add_node("purchase_agent", purchase_verification_agent)
graph.add_node("final_agent", final_decision_agent)

# Entry
graph.set_entry_point("reviewer_agent")

# Parallel execution
graph.add_edge("reviewer_agent", "final_agent")
graph.add_edge("content_agent", "final_agent")
graph.add_edge("purchase_agent", "final_agent")

graph.add_edge("reviewer_agent", "content_agent")
graph.add_edge("reviewer_agent", "purchase_agent")

graph.set_finish_point("final_agent")

app = graph.compile()

# ----------- TEST INPUT -----------
input_state = load_input_from_file("input.txt")

result = app.invoke(input_state)

print("\nFINAL SYSTEM OUTPUT:\n")
print(result["final_result"])
