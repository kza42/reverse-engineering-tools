#  The MIT License (MIT)
#
#  Copyright (c) 2019 kza
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
import optparse


def main():
    header()
    parser = optparse.OptionParser("usage: %prog -f <input file name> -o <output file name> -p <hex pattern>")
    parser.add_option('-f', dest='input_file', type='str', help='input file')
    parser.add_option('-o', dest='output_file', type='str', help='output file')
    parser.add_option('-p', dest='hex_pattern', type='str', help='hex pattern')
    (options, args) = parser.parse_args()
    input_file = options.input_file
    output_file = options.output_file
    hex_pattern = options.hex_pattern
    if input_file is None:
        error('[-] You must specify an input file')
    if output_file is None:
        error('[-] You must specify an output file')
    if hex_pattern is None:
        error('[-] You must specify a hex pattern')

    pattern = get_byte_array_from_str(options.hex_pattern)
    file_data = read_input_file(input_file)
    data = xor_data(file_data, pattern)
    write_output_file(output_file, data)


def get_byte_array_from_str(hex_str: str) -> bytearray:
    try:
        return bytearray.fromhex(hex_str)
    except:
        error('[-] Invalid hex pattern')


def read_input_file(filename: str) -> bytes:
    try:
        data = open(filename, "rb").read()
        print('[+] Read file: ' + filename)
        return data
    except:
        error('[-] Error reading file ' + filename)


def write_output_file(filename: str, data: str):
    try:
        f = open(filename, "w")
        f.write(data)
        print('[+] Written data to: ' + filename)
    except:
        error('[-] Error writing to output file ' + filename)


def xor_data(data: bytes, pattern: bytearray) -> str:
    output = ""
    pattern_length = len(pattern)
    for index, c in enumerate(data):
        val = ord(c) ^ pattern[index % pattern_length]
        output += chr(val)
    print('[+] XOR:ed data')
    return output


def header():
    print('XOR file by kza 2019')


def error(message: str):
    print(message)
    exit(1)


if __name__ == "__main__":
    main()
