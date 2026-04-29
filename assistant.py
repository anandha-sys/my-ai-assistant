 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/assistant.py b/assistant.py
new file mode 100644
index 0000000000000000000000000000000000000000..48f104c8fa7ed655d81ba1ef5d3b9a955513631a
--- /dev/null
+++ b/assistant.py
@@ -0,0 +1,80 @@
+"""A lightweight, extensible AI assistant starter project.
+
+This project provides a clean baseline you can extend into a production-grade
+assistant similar to ChatGPT/Gemini-style interactions.
+"""
+
+from __future__ import annotations
+
+from dataclasses import dataclass
+from datetime import datetime, timezone
+from typing import List
+
+
+SYSTEM_PRINCIPLES = [
+    "Be helpful, clear, and concise.",
+    "Refuse harmful or illegal requests.",
+    "Admit uncertainty and avoid hallucinations.",
+    "Use step-by-step reasoning when needed.",
+]
+
+
+@dataclass
+class Message:
+    role: str
+    content: str
+
+
+class TopAIAssistant:
+    """Simple conversational engine with guardrails and pluggable behavior."""
+
+    def __init__(self, name: str = "Astra One") -> None:
+        self.name = name
+        self.history: List[Message] = []
+
+    def add_message(self, role: str, content: str) -> None:
+        self.history.append(Message(role=role, content=content.strip()))
+
+    def _is_harmful(self, text: str) -> bool:
+        blocked = ["make bomb", "steal", "malware", "exploit"]
+        lower = text.lower()
+        return any(term in lower for term in blocked)
+
+    def _identity_reply(self) -> str:
+        now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
+        return (
+            f"I am {self.name}, your high-performance AI assistant. "
+            f"Built with clear safety principles and practical reasoning. "
+            f"Session time: {now}."
+        )
+
+    def generate(self, user_input: str) -> str:
+        self.add_message("user", user_input)
+
+        if self._is_harmful(user_input):
+            reply = (
+                "I can't help with harmful or illegal activity. "
+                "I can help with safe alternatives instead."
+            )
+        elif any(x in user_input.lower() for x in ["who are you", "your name", "identity"]):
+            reply = self._identity_reply()
+        else:
+            reply = (
+                "Great idea. To make this truly top-tier, focus on: "
+                "(1) strong model quality, (2) fast UX, (3) robust safety, "
+                "(4) continuous evaluation, and (5) clear product differentiation."
+            )
+
+        self.add_message("assistant", reply)
+        return reply
+
+
+if __name__ == "__main__":
+    assistant = TopAIAssistant()
+    print(f"{assistant.name} ready. Type 'exit' to quit.")
+    while True:
+        text = input("You: ").strip()
+        if text.lower() in {"exit", "quit"}:
+            print("Goodbye.")
+            break
+        print(f"{assistant.name}: {assistant.generate(text)}")
 
EOF
)
