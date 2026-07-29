from graph.docs import workflow as indexing_workflow
from graph.QA import workflow as qa_workflow


# =====================================
# STEP 1: INDEX A GITHUB REPOSITORY
# =====================================

index_state = {
    "repo_path": "https://github.com/krishna213119-pixel/RNN",
    "docs": [],
    "chunks": [],
    "vectorstore": None,
    "status": "",
    "error": "",
}

print("\nStarting repository indexing...\n")

index_result = indexing_workflow.invoke(index_state)

print("Indexing Status:")
print(index_result["status"])

if index_result["error"]:
    print("Error:")
    print(index_result["error"])

    raise Exception(
        "Repository indexing failed."
    )

vectorstore = index_result["vectorstore"]

print("\nRepository indexed successfully.")

print(
    f"Documents loaded: "
    f"{len(index_result['docs'])}"
)

print(
    f"Chunks created: "
    f"{len(index_result['chunks'])}"
)


# =====================================
# STEP 2: ASK THE FIRST QUESTION
# =====================================

first_state = {
    "ques": "Explain how this repository works.",
    "retrive_docs": [],
    "ans": "",
    "vectorstore": vectorstore,
    "sources": [],
    "history": [],
}

print("\nAsking first question...\n")

first_result = qa_workflow.invoke(
    first_state
)

print("ANSWER:")
print(first_result["ans"])

print("\nSOURCES:")

for source in first_result["sources"]:
    print(f"- {source}")


# =====================================
# STEP 3: TEST CONVERSATION MEMORY
# =====================================

second_state = {
    "ques": "Which files are responsible for that?",
    "retrive_docs": [],
    "ans": "",
    "vectorstore": vectorstore,
    "sources": [],
    "history": first_result["history"],
}

print("\nAsking follow-up question...\n")

second_result = qa_workflow.invoke(
    second_state
)

print("FOLLOW-UP ANSWER:")
print(second_result["ans"])

print("\nSOURCES:")

for source in second_result["sources"]:
    print(f"- {source}")


# =====================================
# STEP 4: CHECK MEMORY
# =====================================

print("\nCHAT HISTORY:")

for message in second_result["history"]:
    print(
        f"{message.type}: "
        f"{message.content}"
    )