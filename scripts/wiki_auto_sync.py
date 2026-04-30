import os
import subprocess
from datetime import datetime

# 仓库配置
REPOS = {
    "llm-wiki": {
        "path": "/root/hermes-shared/wiki",
        "user": "joe12803",
        "branch": "master"
    },
    "mining-toolkit": {
        "path": "/root/autonomous-mining-toolkit",
        "user": "joe12801",
        "branch": "main"
    },
    "mining-results": {
        "path": "/root/exploration-mining-results",
        "user": "joe12801",
        "branch": "main"
    }
}

def run_cmd(cmd, cwd=None):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)

def switch_gh_user(user):
    print(f"Switching to GitHub user: {user}")
    run_cmd(f"gh auth switch --hostname github.com --user {user}")

def sync_all():
    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    report = [f"### 📊 Hermes Daily Mining Report [{today}]"]

    for name, config in REPOS.items():
        path = config["path"]
        user = config["user"]
        branch = config["branch"]
        
        if not os.path.exists(path):
            continue
            
        print(f"Syncing {name}...")
        switch_gh_user(user)
        
        # Git 操作
        run_cmd("git add .", cwd=path)
        res = run_cmd(f'git commit -m "auto: Daily synchronization {today}"', cwd=path)
        
        if "nothing to commit" in res.stdout:
            report.append(f"- **{name}**: No changes today.")
            continue
            
        push_res = run_cmd(f"git push origin {branch}", cwd=path)
        
        if push_res.returncode == 0:
            report.append(f"- **{name}**: Successfully synced to GitHub.")
        else:
            report.append(f"- **{name}**: ❌ Sync failed! {push_res.stderr[:50]}")

    # 发送飞书汇总消息 (可选)
    print("\n".join(report))

if __name__ == "__main__":
    sync_all()
