import argparse
import secrets
import string
import sys
import pathlib

if len(sys.argv) == 1:
    print(pathlib.Path(__file__).with_name("README.md").read_text(encoding="utf-8"))
    sys.exit(0)

parser = argparse.ArgumentParser(description="Генератор паролей")
parser.add_argument("-l", "--length", type=int, default=16, help="длина пароля")
parser.add_argument("-n", "--count", type=int, default=1, help="сколько паролей")
parser.add_argument("--no-symbols", action="store_true", help="без спецсимволов")
args = parser.parse_args()

chars = string.ascii_letters + string.digits
if not args.no_symbols:
    chars += "!@#$%^&*"

for _ in range(args.count):
    print("".join(secrets.choice(chars) for _ in range(args.length)))