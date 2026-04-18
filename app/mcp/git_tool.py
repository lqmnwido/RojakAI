from git import Repo

class GitTool:
    def latest_commit(self, repo_path: str) -> str:
        repo = Repo(repo_path)
        return repo.head.commit.message.strip()