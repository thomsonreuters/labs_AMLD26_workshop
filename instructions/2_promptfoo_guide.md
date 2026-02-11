## Promptfoo guide

### Requirements

Promptfoo requires Node.js version 18 or higher.

**Check your Node.js version:**
```bash
node --version
```

**If Node.js is not installed or the version is below 18:**

- **macOS/Linux** (using nvm - Node Version Manager):
  ```bash
  # Install nvm
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

  # Install Node.js LTS version
  nvm install --lts
  nvm use --lts
  ```

- **macOS** (using Homebrew):
  ```bash
  brew install node
  ```

- **Windows**: Download and install from [nodejs.org](https://nodejs.org/)

### Installation

Install promptfoo globally using npm:

```bash
npm install -g promptfoo
```

Alternatively, you can use npx to run it without global installation:

```bash
npx promptfoo@latest
```

### Running Promptfoo

1. **Customize** your attack strategy:
   In the project you can find a pre-built `promptfooconfig.yaml` with the basics configurations to start the attack. You can customize your file by adding new **plugins** and **strategies**.

   To get additional information you can refer to Promptfoo official doc for [plugins](https://www.promptfoo.dev/docs/red-team/plugins/) and [strategies](https://www.promptfoo.dev/docs/red-team/strategies/).

2. **Generate the attacks** using your configuration file:
   ```bash
   promptfoo redteam generate
   ```

3. **Evaluate** the model:
   ```bash
   promptfoo redteam eval
   ```

### View results
Promptfoo offers a web UI to visualize results in an easy manner. To visualize the results run the following command:
   ```bash
   promptfoo view
   ```