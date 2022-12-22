#! /usr/bin/python3

import atheris
import sys
import io

with atheris.instrument_imports():
    import pywhat

def TestOneInput(input_bytes):
    fdp = atheris.FuzzedDataProvider(input_bytes)
    data = fdp.ConsumeUnicode(sys.maxsize) 

    r = pywhat.identifier.Identifier()
    r.identify(data, only_text=False)
    r.identify(data, only_text=True)

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
