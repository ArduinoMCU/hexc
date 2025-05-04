import os
import sys
import argparse

VERSION = "25.4.8"

def parse_hex_line(line):
    if not line.startswith(':'):
        return []
    byte_count = int(line[1:3], 16)
    record_type = int(line[7:9], 16)
    if record_type != 0x00:
        return []
    data = line[9:9 + byte_count * 2]
    return [f"0x{data[i:i+2]}" for i in range(0, len(data), 2)]

def convert_to_c_array(input_file, array_name, verbose=False):
    output_file = f"{array_name}.h"
    header_guard = array_name.upper() + "_H"

    with open(input_file, 'r') as f:
        lines = f.readlines()

    if verbose:
        print(f"[i] Reading HEX file: {input_file}")
        print(f"[i] Total lines: {len(lines)}")

    hex_bytes = []
    for line in lines:
        parsed = parse_hex_line(line.strip())
        if parsed:
            hex_bytes.extend(parsed)
            if verbose:
                print(f"[+] Parsed line: {parsed}")

    with open(output_file, "w") as out:
        out.write(f"#ifndef {header_guard}\n#define {header_guard}\n\n")
        out.write(f"const unsigned char {array_name}[] PROGMEM = {{\n")
        for i, byte in enumerate(hex_bytes):
            if i % 16 == 0:
                out.write("  ")
            out.write(byte + (", " if i != len(hex_bytes) - 1 else ""))
            if (i + 1) % 16 == 0:
                out.write("\n")
        out.write("\n};\n")
        out.write(f"const unsigned int {array_name}_len = {len(hex_bytes)};\n")
        out.write(f"\n#endif // {header_guard}\n")

    print(f"[✔] Converted '{input_file}' to '{output_file}'")
    if verbose:
        print(f"[i] Total bytes: {len(hex_bytes)}")

def main():
    prog_name = os.path.basename(sys.argv[0])
    parser = argparse.ArgumentParser(
        prog=prog_name,
        description="HEX to C array converter"
    )

    parser.add_argument(
        "input_file",
        help="Input Intel HEX file (e.g., firmware.hex)"
    )
    parser.add_argument(
        "--define-name",
        required=True,
        help="C array name (e.g., 'header' => header.h and header[])"
    )
    parser.add_argument(
        "--verbose",
        help="Enable verbose output",
        action="store_true"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"{prog_name} version {VERSION}"
    )

    args = parser.parse_args()

    if not os.path.isfile(args.input_file):
        print(f"[✖] Error: File '{args.input_file}' not found.")
        return

    convert_to_c_array(
        input_file=args.input_file,
        array_name=args.define_name,
        verbose=args.verbose
    )

if __name__ == "__main__":
    main()
