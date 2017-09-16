
### Installations
These are the commands I used:
```sh
sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install lib32z1 lib32ncurses5 libselinux1:i386 g++-multilib libc6-dev-i386
```
### Testing it

Let's try out with a simple `helloworld.c`.
```c
#include <stdio.h>
int main(){
    printf("hello world");
    return 0;
}
```
Let's compile, run and file them!
```sh
gcc -m32 -o helloworld helloworld.c
gcc -m64 -o helloworld2 helloworld.c
./helloworld
./helloworld2
file helloworld
file helloworld2
```
