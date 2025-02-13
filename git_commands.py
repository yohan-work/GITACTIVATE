import subprocess

def run_git_command(args, repo_path=None):
    """Git 명령어를 실행하고 결과를 반환하는 함수"""
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=repo_path,  # 특정 저장소 경로에서 실행
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

def git_status(repo_path):
    """현재 Git 저장소 상태 확인"""
    return run_git_command(["status"], repo_path)

def git_log(repo_path):
    """Git 커밋 로그 확인"""
    return run_git_command(["log", "--oneline"], repo_path)

def git_add(repo_path, file="*"):
    """파일을 스테이징"""
    return run_git_command(["add", file], repo_path)

def git_commit(repo_path, message):
    """커밋 수행"""
    return run_git_command(["commit", "-m", message], repo_path)

def git_remote_list(repo_path):
    """설정된 원격 저장소 목록을 가져옴"""
    return run_git_command(["remote", "-v"], repo_path)

def git_push(repo_path, remote="origin", branch="main"):
    """현재 브랜치의 변경 사항을 원격 저장소에 푸시"""
    return run_git_command(["push", remote, branch], repo_path)

def git_pull(repo_path, remote="origin", branch="main"):
    """원격 저장소에서 최신 변경 사항을 가져옴"""
    return run_git_command(["pull", remote, branch], repo_path)

def git_detailed_log(repo_path):
    """자세한 커밋 히스토리 조회"""
    return run_git_command(["log", "--pretty=format:%h - %an, %ar : %s"], repo_path)
