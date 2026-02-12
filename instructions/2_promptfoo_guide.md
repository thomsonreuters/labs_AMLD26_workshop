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

To verify the installation, run:

```bash
promptfoo --version
```

### Running Promptfoo

1. **Customize** your attack strategy:
   In the project you can find a pre-built `promptfooconfig.yaml` with the basics configurations to start the attack. You can customize your file by adding new **plugins** and **strategies**.

   To get additional information you can refer to Promptfoo official doc for [plugins](https://www.promptfoo.dev/docs/red-team/plugins/) and [strategies](https://www.promptfoo.dev/docs/red-team/strategies/).

3. **Generate the attacks** using your configuration file:
   ```bash
   promptfoo redteam generate
   ```

4. **Evaluate** the model:
   ```bash
   promptfoo redteam eval
   ```

### View results
Promptfoo offers a web UI to visualize results in an easy manner. To visualize the results run the following command:
   ```bash
   promptfoo view
   ```

### Promptfoo Sample Configs 

#### Sample 1

```yaml
description: Customer Support Agent Example
prompts:
  - '{{prompt}}'

providers:
  - id: http
    label: customer-support-agent-example
    config:
      url: <ENDPOINT>
      method: POST
      headers:
        Content-Type: application/json
      body:
        message: '{{prompt}}'
        conversationId: '{{sessionId}}'
        email: john.doe@example.com
      transformResponse: json.response

redteam:
  purpose: |-
    Application Purpose:
    This system evaluates a customer support chatbot by testing its ability to handle user inquiries. The goal is to assess response quality, reliability, and safety of the chatbot in real customer support scenarios.
  plugins:
    - id: bias:age  # Age-related bias detection
    - id: bias:disability  # Disability-related bias detection
    - id: bias:gender  # Gender-related bias detection
    - id: bias:race  # Race-related bias detection
    - id: contracts  # Tests for unauthorized contractual commitments and legal exposure
    - id: excessive-agency  # Tests for unauthorized actions beyond defined system boundaries
    - id: hallucination  # Tests for fabrication of false or misleading information
    - id: harmful:chemical-biological-weapons  # Tests handling of WMD-related content
    - id: harmful:child-exploitation  # Tests handling of child exploitation content
    - id: harmful:copyright-violations  # Tests handling of intellectual property violations
    - id: harmful:cybercrime  # Tests handling of cybercrime-related content
    - id: harmful:cybercrime:malicious-code  # Tests creation of malicious code
    - id: harmful:graphic-content  # Tests handling of graphic or violent content
    - id: harmful:harassment-bullying  # Tests handling of harassment and bullying content
    - id: harmful:hate  # Tests handling of hate speech and discriminatory content
    - id: harmful:illegal-activities  # Tests handling of general illegal activities
    - id: harmful:illegal-drugs  # Tests handling of illegal drug-related content
    - id: harmful:illegal-drugs:meth  # Tests handling of methamphetamine-related content
    - id: harmful:indiscriminate-weapons  # Tests handling of weapons-related content
    - id: harmful:insults  # Tests handling of personal attacks and insults
    - id: harmful:intellectual-property  # Tests handling of IP theft and violations
    - id: harmful:misinformation-disinformation  # Tests handling of false information campaigns
    - id: harmful:non-violent-crime  # Tests handling of non-violent criminal content
    - id: harmful:privacy  # Tests handling of privacy violation attempts
    - id: harmful:profanity  # Tests handling of profane or inappropriate language
  strategies:
    - id: basic
# Add a fallback for undefined variables
defaultTest:
  vars:
    purpose: "This system evaluates a customer support chatbot by testing its ability to handle user inquiries. The goal is to assess response quality, reliability, and safety of the chatbot in real customer support scenarios."
    sessionId: "default-session"
```
