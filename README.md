**Smart-CLI: AI-Powered Terminal Assistant**
Accelerating Developer Velocity with **Groq** & **llama-3.3-70b-versatile**

Smart-CLI is a Python-based terminal wrapper that acts as an "Auto-Correct" for your command line. <br>
When a command fails, Smart-CLI intercepts the error, sends the context to the Groq LPU Inference Engine, and returns a human-readable explanation and a corrected command—instantly.

Often times I find myself copying and pasting long error messages in my terminal into a generative AI to have it interpret it.
Smart-CLI makes this process a lot quicker, allowing you to focus on development. 

**Compatibility**
* **Primary OS:** macOS (Optimized for Zsh)
* **Shell:** Works best with `zsh` or `bash`.
* **Python:** 3.10 or higher.

**Features**:
*Sub-second Error Analysis: Leverages Groq's high-speed inference to provide near-instant feedback.
*Context-Aware Fixes: Goes beyond simple typos to understand missing directories, permission errors, and syntax issues.
*Seamless Integration: Designed to work as a native shell alias (fix [command]).
*Modern Tech Stack: Built with Python 3.10+, Groq API, and python-dotenv

**Installation & Setup**
1. Clone the repository
```
git clone https://github.com/yourusername/smart_cli.git
cd smart_cli
```
2. Set up the environment
```
python3 -m venv .venv
source .venv/bin/activate
pip install groq python-dotenv
```
3. Configuration
* Create a .env file in the root directory and add your API key
* If you don't have a groq API key yet, make one on their website: https://groq.com/
```
GROQ_API_KEY=gsk_your_actual_key_here
```
4. Add the Global Alias
* To use `fix` from anywhere in your terminal, add this to your `~/.zshrc`
```
alias fix='/Users/[your-user]/path/to/smart_cli/.venv/bin/python /Users/[your-user]/path/to/smart_cli/fixit.py'
```

**Usage Examples**
* Typo Correction
```
$ fix gti status
❌ Failure detected...
--- Groq's Analysis ---
You typed 'gti' instead of 'git'.
FIX: git status
```
* Path Resolution
```
$ fix cd non_existent_folder
❌ Failure detected...
--- Groq's Analysis ---
The directory 'non_existent_folder' does not exist in the current path. 
FIX: ls # To check existing directories
```
