import subprocess

def get_git_diff(commit) -> str:
    """
    Get the git diff for a commit.
    """
    try:
        # First try to get diff against parent commit
        result = subprocess.run(
            ["git", "diff", f"{commit}^!", "--unified=0"],
            check=True,
            text=True,
            capture_output=True
        )
        if result.stdout.strip():
            return result.stdout
        
        # If no diff found (e.g., initial commit), try showing the commit content
        result = subprocess.run(
            ["git", "show", commit, "--unified=0"],
            check=True,
            text=True,
            capture_output=True
        )
        return result.stdout
        
    except subprocess.CalledProcessError as e:
        # If commit doesn't exist or has no parent, try working directory diff
        try:
            result = subprocess.run(
                ["git", "diff", "--unified=0"],
                check=True,
                text=True,
                capture_output=True
            )
            if result.stdout.strip():
                return result.stdout
            else:
                return "No changes detected in working directory or commit."
        except subprocess.CalledProcessError:
            print(f"Error getting git diff: {e}")
            return ""
