import random
import os, errno

def cycle_length_naive(n):
    length = 1
    while n > 1:
        if (n % 2) == 0:
            n = (n // 2)
        else:
            n = (3 * n) + 1
        length += 1
    return length

def swap_if_greater(i, j):
    if i > j:
        return j, i
    return i, j

def collatz_eval (i, j) :
    max_length = 1
    for k in range(i, j + 1):
        length = cycle_length_naive(k)
        max_length = max(max_length, length)
    return max_length

def generate_range():
    return random.randint(1, 1000000), random.randint(1, 100000)

def write_in(i, j, _in):
    input_line = str(i) + " " + str(j) + "\n"
    _in.write(input_line)
    return input_line

def write_out(i, j, length, _out):
    _out.write(str(i) + " " + str(j) + " " + str(length) + "\n")

def generate_tests(n, _in, _out):
    for k in range(n):
        print("Generating test: %d/%d" % (k + 1, n), end="\r", flush=True)
        i, j = generate_range()
        read = write_in(i, j, _in)

        start, end = swap_if_greater(i, j)
        length = collatz_eval(start, end)

        write_out(i, j, length, _out)
    print("")
    print("Done. ", flush=True)

def filenames(github_username):
    return github_username + "-RunCollatz.in", github_username + "-RunCollatz.out"

def clear_files(_in, _out):
    try:
        os.remove(_in)
        os.remove(_out)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise

def prompt():
    github_username = input("What is your Github username? ")
    num_tests = eval(input("How many tests to generate? "))

    _in, _out = filenames(github_username)
    clear_files(_in, _out)
    in_file = open(_in, "x")
    out_file = open(_out, "x")
    generate_tests(num_tests, in_file, out_file)

prompt()
