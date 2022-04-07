import subprocess
import os


def main():
    # os.chdir(r"C:\k8b\prog\python\prj\github-download\prj")
    # os.system(f"git clone -o gh {url}")
    # a, b = os.system(f"git rev-parse HEAD")
    import subprocess
    print(os.getcwd())
    a = os.popen(f"git rev-parse HEAD").read().strip()
    print(f"{a}")
    with open("git-commit-hash-template.h", "r") as f:
        s = f.read().format(commit_hash=a)
    with open("git-commit-hash.h", "w") as f:
        f.write(s)


if __name__ == '__main__':
    main()


