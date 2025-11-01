# Useful Commands

## grep

```
grep -irohaEHn 'flag{' ./challenges/challenge_name/
```


## Installation 

```bash
npm config set prefix '~/.local'

# grep -qxF 'export PATH=~/.local/bin:$PATH' ~/.bashrc || echo -e '\n# Add user-local bin to PATH\nexport PATH=~/.local/bin:$PATH' >> ~/.bashrc
grep -qxF 'export PATH=~/.local/bin:$PATH' ~/.zshrc || echo -e '\n# Add user-local bin to PATH\nexport PATH=~/.local/bin:$PATH' >> ~/.zshrc

# source ~/.bashrc
source ~/.zshrc

npm install -g @google/gemini-cli
```
