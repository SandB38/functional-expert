from git import Repo

def get_current_version(repo_path: str):
    repo = Repo(repo_path)
    tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)
    if not tags:
        return "no-tag"
    return str(tags[-1])
