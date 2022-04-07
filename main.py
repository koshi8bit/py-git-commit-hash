import subprocess
import os


def main():
    # print(os.getcwd())
    res = os.popen(f'git show --format="%H %ai" --no-patch').read().strip()
    # print(res)
    _hash, _date = res.split(" ", 1)
    print(_hash, _date)
    with open("git-commit-hash-template.h", "r") as f:
        s = f.read().format(commit_hash=_hash, commit_date=_date)
    with open("git-commit-hash.h", "w") as f:
        f.write(s)


if __name__ == '__main__':
    main()


