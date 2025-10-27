# 🤖 Agents

## Instructions

Start the agent in the repository's root directory with `gemini`. If you are not familiar with Gemini, [this](https://www.philschmid.de/gemini-cli-cheatsheet) is a good primer.

A good way to kick an agent off is to use a prompt like this:

```
A new challenge just came in called maximum sound. It's just a wav file. You should do your work in the `./challenges/maximum_sound` directory.
```

## Sandboxing

See the [.gemini/sandbox.Dockerfile](/.gemini/sandbox.Dockerfile) for the custom sandbox environment used by the agents. It includes various CTF tools and Python libraries to facilitate challenge solving.

---

## Resources
### Prompting
- https://github.com/anthropics/prompt-eng-interactive-tutorial

### Gemini CLI
- https://github.com/google-gemini/gemini-cli
- https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/configuration.md
- https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md

### Anthropic
- [Claude Cookbooks](https://github.com/anthropics/claude-cookbooks)
- [Claude Code Skills](https://github.com/anthropics/skills/tree/main/document-skills)
