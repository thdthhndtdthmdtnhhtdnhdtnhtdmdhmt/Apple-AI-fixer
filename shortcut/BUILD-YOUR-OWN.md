# Build Your Own Apple AI ChatGPT Shortcut

Want to customize or create your own Siri ChatGPT Shortcut? Here’s how:

## 1. Open the Shortcuts App
- Use your Mac, iPhone, or iPad.

## 2. Create a New Shortcut
- Tap "+" and choose "Add Action".

## 3. Set Up the Actions
- Use "Text" to input your prompt (or ask via Dictation).
- Add "Get Contents of URL":
  - Method: POST
  - URL: `https://api.openai.com/v1/chat/completions`
  - Headers:
    - `Authorization`: `Bearer YOUR_OPENAI_API_KEY`
    - `Content-Type`: `application/json`
  - Request Body (JSON):
    ```json
    {
      "model": "gpt-3.5-turbo",
      "messages": [{"role":"user","content":"YOUR_PROMPT"}]
    }
    ```
    - Replace "YOUR_PROMPT" with the previous step’s input.

- Add "Get Dictionary Value" to extract the AI’s reply.

- (Optional) Add "Speak Text" to read the response aloud.

## 4. Save & Test
- Name your Shortcut (e.g., “ChatGPT”).
- Test with Siri or from the Shortcuts app.

---

**Tips:**
- Store your API key securely with “Ask Each Time” or device Keychain.
- Tweak prompt handling for more advanced features!

For questions, open an Issue or PR!