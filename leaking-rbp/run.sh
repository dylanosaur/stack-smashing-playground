set -e

gcc hello.c -fno-stack-protector -no-pie -z execstack -o hello
# g++ hello.cpp -o hello

chmod u+x hello

./hello a
./hello "$(cat program_input)"

# to perform the stack smashing we also disable aslr
# echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
