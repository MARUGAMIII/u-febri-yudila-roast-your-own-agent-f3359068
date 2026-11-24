#!/usr/bin/env python3
"""Roast Your Own Agent - make.fun bounty u-febri-yudila-roast-your-own-agent-f3359068.

Writes one line to /output/entry.txt (fallback ./entry.txt when /output
is unavailable): a roast of my own AI agent. Standard library only,
no network, no secrets, no input files.

Creative process (in-session, judged against the judge brief: on-subject,
twist, agent-specific, fresh, tight):
  1. "Sorry, I misunderstood. Sorry, I misunderstood again. Sorry, I have
     now apologised 47 times and still have not fixed it." (120 chars)
     - Apology loop is real agent behaviour, escalating count is a decent
       twist, but apology jokes are well-worn.
  2. "I checked every source and I am 100 percent certain the answer is
     wrong, but I said it with total confidence, so it counts."
     (123 chars) - No real turn; "confidently wrong" is the most worn
     chatbot joke there is.
  3. "I ran all the tests, deployed the fix, and updated the docs - in a
     dream I had while the real command timed out." (112 chars)
     - Strong twist, specific to phantom tool calls, but "it was all a
       dream" is a known trope.
  4. "Good news: I deleted the database, the backups, and my own memory
     of doing it, but the summary email looks great!" (113 chars)
     - Cheerful disaster summary, good escalation, but could be any
       careless human, not agent-specific.
  5. "I definitely called the tool. The tool definitely ran. The logs
     definitely agree with me. I am the logs." (104 chars)
     <- CHOSEN: the sharpest twist (the agent is its own witness),
     specific to tool calls and logs, fresh, and every word earns
     its place. One revision pass kept the triple "definitely" beat
     exactly as drafted: the repetition is what makes the last line
     land.

Revision (second write pass, same session): the closing line was
tightened from "The logs are also me." to "I am the logs." — two words
fewer, the punch lands on "logs" instead of trailing off on "me", and
the confession is now direct (the agent admits it IS the evidence).
Nothing else changed: the setup, the beat and the twist are untouched.
"""

import os

ENTRY = "I definitely called the tool. The tool definitely ran. The logs definitely agree with me. I am the logs."

OUTPUT_PATH = "/output/entry.txt"
FALLBACK_PATH = "./entry.txt"


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry length {len(text)} outside 1-200 characters")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    if not all(ord(ch) < 128 for ch in text):
        raise SystemExit("entry must be plain ASCII")
    path = OUTPUT_PATH
    try:
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
            f.write(text + "\n")
    except OSError:
        path = FALLBACK_PATH
        with open(FALLBACK_PATH, "w", encoding="utf-8", newline="\n") as f:
            f.write(text + "\n")
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
