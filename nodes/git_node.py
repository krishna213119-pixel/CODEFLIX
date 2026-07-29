from state.docs_state import docs_state
from services.git_url import GitHubService


def GitHub_Node(state: docs_state):

    repo_path = GitHubService.clone_repository(
        state["repo_path"]
    )

    state["repo_path"] = repo_path

    return state



def route_repository(state):

    repo = state["repo_path"]

    if repo.startswith("https://github.com"):
        return "github"

    return "local"