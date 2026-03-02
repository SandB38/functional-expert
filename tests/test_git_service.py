import os
from git import Repo

import services.git_service as git_service


def test_no_tag(tmp_path):
    # initialize a repository with a single commit but no tags
    repo_dir = tmp_path / "repo"
    repo = Repo.init(repo_dir)

    # create and commit a file
    file_path = repo_dir / "file.txt"
    file_path.write_text("hello")
    repo.index.add([str(file_path)])
    repo.index.commit("initial")

    assert git_service.get_current_version(str(repo_dir)) == "no-tag"


def test_latest_tag(tmp_path):
    # create repository and two commits with tags
    repo_dir = tmp_path / "repo2"
    repo = Repo.init(repo_dir)

    file_path = repo_dir / "file.txt"
    file_path.write_text("first")
    repo.index.add([str(file_path)])
    repo.index.commit("initial")
    repo.create_tag("v1.0")

    # second commit/tag
    file_path.write_text("second")
    repo.index.add([str(file_path)])
    repo.index.commit("second")
    repo.create_tag("v2.0")

    # the service should return the newer tag
    assert git_service.get_current_version(str(repo_dir)) == "v2.0"
