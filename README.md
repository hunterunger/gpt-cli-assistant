# GPT-CLI-Assistant
## Use AI to make terminal commands!

![screencap.gif](assets/screencap.gif)

## Requirements

* Basic shell knowledge
* Python 3
* Mac or Linux


## Quick Start 🏎️

Clone this repo to your machine and `cd` into it.

Install requirements with `python3 -m pip install -r requirements.txt`

Simply run `python3 main.py "check what shell im using"`

It will prompt you to set up your API key with [OpenAI](https://openai.com/api/). Currently it is free to use during the beta period.

Also, it will give you an alias snippet for Alias Setup. 

You will get an output like `echo $SHELL`. If you did, run it again with the `-e` flag. This will automatically run the command.

So like this: `python3 main.py "check what shell im using" -e`

## Alias Setup 🔩

### Set up your alias

Run `echo $SHELL` to check your shell.
In this repo run `echo $PWD` to get it's absolute path or use the snippet from earlier.

#### If you're using BASH:

```
echo 'alias gpt="python3 ~/path/to/main.py"' >> .bashrc 
```

#### If you're using ZSH:

```
echo 'alias gpt="python3 ~/path/to/main.py"' >> .zshrc 
```

#### If you're using FISH:

```
function gpt
    python3 ~/path/to/main.py $argv
end
funcsave gpt
```

---

Now you should be able to run
```
gpt "check what shell I'm using"
```

# Usage 🥧

### Simple usage:

`gpt "your request in simple english"`
This will simply output the command to accomplish the requested task.
![simple_example.png](assets/simple_example.png)

### Automatic Execution

Add `-e` to automatically run the command.

`gpt "your request in simple english" -e`

This will run the command instantly. 
![exe_example.png](assets/exe_example.png)
### More help

Run `gpt -h` to get more commands and info.
![help.png](assets/help.png)
## Tips 😎

* Questions are cached so you can re-run the same command without using additional api requests
* Make commands like `gpt "list hidden files"` and NOT like `gpt "make a command to list files"`
  git log --pretty=format:"%h %ad %s" --date=short | vim -
