## How to install ltrace, strace

First, try to run the following. If it works, you can stop there.
```apt-get install ltrace strace```

## Modifying apt sources

By default, I realized kali doesn't have tools like `ltrace` and `strace` packages even though kali is a variant of debian.
Hence, the solution is to add debian to our apt source list.

```sh
echo "deb http://ftp.de.debian.org/debian stretch main" | tee -a /etc/apt/sources.list &&
apt-get update &&
apt-get install ltrace strace
```
