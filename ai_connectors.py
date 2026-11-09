import os
import json
import urllib.request
import urllib.error


class AIConnectors:

    def __init__(self):
        self.gemini_key = os.getenv("GEMINI_API_KEY")
        self.deepseek_key = os.getenv("DEEPSEEK_API_KEY")

    def ask_gemini(self, prompt):
        if not self.gemini_key:
            return "Falta configurar la API de Gemini."

        url = (
            "https://generativelanguage.googleapis.com/"
            "v1beta/models/gemini-2.0-flash:generateContent"
            "?key=" + self.gemini_key
        )

        data = {
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        }

        return self._request(url, data)

    def ask_deepseek(self, prompt):
        if not self.deepseek_key:
            return "Falta configurar la API de DeepSeek."

        url = "https://api.deepseek.com/chat/completions"

        data = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        return self._request(
            url, data, self.deepseek_key
        )

    def _request(self, url, data, api_key=None):
        headers = {
            "Content-Type": "application/json"
        }

        if api_key:
            headers["Authorization"] = "Bearer " + api_key

        request = urllib.request.Request(
            url,
            data=json.dumps(data).encode("utf-8"),
            headers=headers,
            method="POST"
        )

        try:
            with urllib.request.urlopen(
                request, timeout=30
            ) as response:
                result = json.loads(
                    response.read().decode("utf-8")
                )

            if "candidates" in result:
                return result["candidates"][0][
                    "content"
                ]["parts"][0]["text"]

            return result["choices"][0][
                "message"
            ]["content"]

        except urllib.error.HTTPError as error:
            return "Error API: " + str(error.code)

        except Exception as error:
            return "Error de conexión: " + str(error)
