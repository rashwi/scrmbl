

# SCRMBL : A simple utility to safely store secrets

SCRMBL is a simple python utility that can safely store your secrets. The tool will scramble and encrypt your secrets before storing it away. Encryption provides adequate security for your secrets, while scrambling makes sure your password entropy is not undone by a global password.

## How it works
Once you setup the tool using setup.py (see prerequisities), the tool will create a key encrypted with a password of your choosing. This key will be used to encrypt any secrets you use with the tool. Each secret added to the tool's storage will be scrambled using a pin (unique to each secret). The tool will use the pin to calculate an entropically similar string before encrypting it. Once encrypted, the tool is agnostic of the pin. That is, when attempting to decrypt the key, any pin will provide an output back from the tool. This prevents brute force attacks on the pin, as a "wrong" unscrambled output is indistinguishable from a "right" unscrambled output, if the original secret is not easily distinguished. 

Please note that the safety of usage for this tool depends entirely on how random your original secret is. Do not use this tool if your unencrypted secret is easily identifiable as a secret. 

## Prerequisites
You need to have python3 installed on your system for this tool to work. On a debian/ubuntu system, you can install python3 using apt:

```shell
sudo apt-get update
sudo apt-get install python3
```
Once python is installed, you will have to clone the project and then run setup.py before using the tool:

```shell
git clone github.com/rashwi/scrmbl
cd scrmbl
./setup.py
```

## Usage/Examples

For upto date documentation on the tool, run the help option:

```shell
./scrbml.py --help
```

Running **scrmbl.py** always requires at least one argument: The path (or filename) of the file to read/write secrets from/to. By default, the file will be saved to a hidden directory in your home area.

Run **scrmbl.py --add** to add secrets to your secrets file.

Run scrmbl.py filename to read secrets from your secrets file. Note that the secrets will only be printed to the screen for a limited period (5s default) and will disapper after. Furthermore, the printout will contain other random characters to obfuscate the value (your secret will be in the obfuscated code)



