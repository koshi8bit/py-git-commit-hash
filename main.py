import subprocess
import os


def main():
    # os.chdir(r"C:\k8b\prog\python\prj\github-download\prj")
    # os.system(f"git clone -o gh {url}")
    a = os.system(f"git rev-parse HEAD")
    print(f"{a}=")
    print("asd")


if __name__ == '__main__':
    main()


