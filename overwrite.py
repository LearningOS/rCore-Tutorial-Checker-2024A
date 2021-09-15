import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("chapter", type=int)
chapter = parser.parse_args().chapter

if chapter >= 4:
    os.system("cp overwrite/build-elf.rs ../os/build.rs")
else:
    os.system("cp overwrite/build-bin.rs ../os/build.rs")

if chapter <= 6:
    os.system("cp overwrite/Makefile-ch3 ../os/Makefile")
else:
    os.system("cp overwrite/Makefile-ch7 ../os/Makefile")
    os.system("cp overwrite/easy-fs-fuse.rs ../easy-fs-fuse/src/main.rs")

lines = []
with open("../os/Cargo.toml", 'r') as f:
    for line in f.readlines():
        processed = line.replace(' git = "https://github.com/rcore-os/riscv"', ' path = "../ci-user/riscv" ')
        lines.append(processed)
with open("../os/Cargo.toml", 'w+') as f:
    f.writelines(lines)