import os
from transformers import AutoTokenizer

model_path = "./tokenizer"
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

prompt_text = """
Given a rational number, write it as a fraction in lowest terms and calculate the product of the resulting numerator and denominator. For how many rational numbers between 0 and 1 will $20_{}^{}!$ be the resulting product?
"""
prompt_text = "Prompt: " + prompt_text.strip() + "\n"
output_text = """
Solution: Let the rational number between 0 and 1 be $r$. When written as a fraction in lowest terms, let it be $\frac{a}{b}$, where $a$ and $b$ are positive integers, $\gcd(a, b) = 1$, and $0 < a < b$. We are given that the product of the numerator and denominator is $20!$, so $a \times b = 20!$.  We need to find the number of pairs $(a, b)$ such that $a \times b = 20!$, $\gcd(a, b) = 1$, and $a < b$.  Let $N = 20!$. The prime factorization of $N$ is $p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}$, where $p_i$ are distinct prime numbers. The number of distinct prime factors of $20!$ is the number of primes less than or equal to 20. These primes are 2, 3, 5, 7, 11, 13, 17, 19. Thus, there are 8 distinct prime factors, so $k = 8$.  Since $a \times b = N$ and $\gcd(a, b) = 1$, each prime power factor $p_i^{e_i}$ of $N$ must be entirely a factor of $a$ or entirely a factor of $b$. The number of ways to distribute the prime power factors between $a$ and $b$ is $2^k$, where $k$ is the number of distinct prime factors of $N$. Each distribution corresponds to a unique pair $(a, b)$ such that $a \times b = N$ and $\gcd(a, b) = 1$. The number of such pairs is $2^{\omega(N)}$, where $\omega(N)$ is the number of distinct prime factors of $N$.  Since $20!$ is not a perfect square, for every pair $(a, b)$ such that $a \times b = 20!$ and $\gcd(a, b) = 1$, we have $a \neq b$. The pairs can be grouped into $(a, b)$ and $(b, a)$, where $a \neq b$. The number of pairs with $a < b$ is equal to the number of pairs with $b < a$. The total number of pairs is $2^{\omega(20!)}$. The number of pairs with $a < b$ is $\frac{1}{2} \times 2^{\omega(20!)} = 2^{\omega(20!) - 1}$.  The number of distinct prime factors of $20!$ is $\omega(20!) = 8$. The number of pairs $(a, b)$ such that $a \times b = 20!$, $\gcd(a, b) = 1$, and $a < b$ is $2^{8 - 1} = 2^7 = 128$.  Each such pair $(a, b)$ corresponds to a unique rational number $\frac{a}{b}$ between 0 and 1 in lowest terms, with the product of the numerator and denominator equal to $20!$.  Final Answer: The final answer is $\boxed{128}$
"""

# Encode prompt and output separately
prompt_token_ids = tokenizer.encode(prompt_text, return_tensors="pt")[0].tolist()
output_token_ids = tokenizer.encode(output_text, return_tensors="pt")[0].tolist()

# Combine token ids: prompt first, then output
token_ids = prompt_token_ids + output_token_ids

# step_map is only for output tokens: prompt tokens are at step -1 (always visible)
step_map = [-1] * len(prompt_token_ids) + list(range(len(output_token_ids)))

### output trace viewer
pieces = []
prev = ""
for i in range(len(token_ids)):
    cur = tokenizer.decode(token_ids[:i+1], skip_special_tokens=False, clean_up_tokenization_spaces=False)
    piece = cur[len(prev):]
    pieces.append(piece)
    prev = cur

# 2) 标记特殊 token（可在前端开关隐藏）
try:
    special_ids = set(getattr(tokenizer, "all_special_ids", []) or [])
except Exception:
    special_ids = set()
is_special = [tid in special_ids for tid in token_ids]

# 写出自包含 HTML 文件
import json, os

data = {
    "pieces": pieces,
    "step_map": step_map,
    "is_special": is_special,
    "prompt_length": len(prompt_token_ids),
}
SPEED = 100  # milliseconds per step
BLOCK_SIZE = 4
# --- self-contained HTML (auto-play with loop, no controls) ---
html = f"""
<style>
  :root {{
    --fg: #111;
    --bg: #fafafa;
    --muted: #888;
    --new: #0a7f2e;
    --mask: #aaa;
    --border: #ddd;
    --prompt-bg: #f5f9ff;
    --output-bg: #fdfdfd;
    --prompt-border: #a3c4f3;
    --output-border: #c4e3c4;
  }}
  body {{
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    margin: 20px auto;
    max-width: 900px;
    color: var(--fg);
    background: var(--bg);
  }}
  h1 {{
    font-size: 20px;
    margin: 0 0 12px 0;
    font-weight: 600;
    text-align: center;
    color: #333;
  }}
  #meta {{
    color: var(--muted);
    font-size: 13px;
    margin-bottom: 10px;
    text-align: center;
  }}
  .section {{
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 20px;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
    line-height: 1.55;
    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    width: 100%;
    box-sizing: border-box;
  }}
  #prompt {{
    background: var(--prompt-bg);
    border: 1px solid var(--prompt-border);
    min-height: 80px;
  }}
  #output {{
    background: var(--output-bg);
    border: 1px solid var(--output-border);
    min-height: 600px;
    height: 600px;
    overflow-y: auto;
  }}
  .masked {{
    color: transparent;
    text-shadow: 0 0 0 var(--mask);
  }}
  .unmasked {{
    color: inherit;
  }}
  .new {{
    background: #e9f7ee;
    outline: 1px dashed #b7e1c3;
    animation: fadeIn 0.3s ease-out;
  }}
  .prompt {{
    color: #004b9b;
    font-weight: 600;
  }}
  .special {{
    color: var(--muted);
  }}
  .maskToken {{
    display:inline-block;
    width:9ch;
    text-align:center;
    opacity:0.6;
    white-space:nowrap;
  }}
  @keyframes fadeIn {{
    from {{ background:#cdecd8; }}
    to {{ background:#e9f7ee; }}
  }}
</style>

<body>
  <h1>🧩 Token Generation Trace Viewer</h1>
  <div id="meta"></div>
  
  <div id="prompt" class="section"></div>
  <div id="output" class="section"></div>

  <script id="data" type="application/json">{json.dumps(data)}</script>
  <script>
    const DATA = JSON.parse(document.getElementById('data').textContent);
    const pieces = DATA.pieces.map(piece => 
      piece.replace(/\\f/g, '\\\\f').replace(/\\t/g, '\\\\t')
           .replace(/\\r/g, '\\\\r').replace(/\\v/g, '\\\\v')
    );
    const steps  = DATA.step_map;
    const isSpec = DATA.is_special;
    const promptLength = DATA.prompt_length;

    const maxStep = Math.max(...steps);
    const promptEl = document.getElementById('prompt');
    const outputEl = document.getElementById('output');
    const meta = document.getElementById('meta');
    let currentStep = 0;

    function render(t) {{
      const fragPrompt = document.createDocumentFragment();
      const fragOutput = document.createDocumentFragment();

      let revealed = 0;

      for (let i = 0; i < pieces.length; i++) {{
        const span = document.createElement('span');
        const piece = pieces[i];
        const step = steps[i];

        if (step === -1) {{
          // Prompt tokens
          span.className = 'unmasked prompt';
          span.textContent = piece;
          fragPrompt.appendChild(span);
        }} else if (step <= t) {{
          // Output tokens already revealed
          span.className = 'unmasked' + (step === t ? ' new' : '');
          span.textContent = piece;
          fragOutput.appendChild(span);
        }} else {{
          // Masked or hidden tokens
          const tokenIndex = step;
          const blockStart = Math.floor(t / {BLOCK_SIZE}) * {BLOCK_SIZE};
          const blockEnd = blockStart + {BLOCK_SIZE};
          if (tokenIndex >= blockStart && tokenIndex < blockEnd) {{
            span.className = 'masked maskToken' + (isSpec[i] ? ' special' : '');
            span.textContent = '|<MASK>|';
            fragOutput.appendChild(span);
          }}
        }}
      }}

      promptEl.innerHTML = '';
      promptEl.appendChild(fragPrompt);
      outputEl.innerHTML = '';
      outputEl.appendChild(fragOutput);
      meta.textContent = `Generation speed: ${{(t > 0 ? ((revealed - promptLength - 1) / t).toFixed(2) : 0)}} tokens/step`;
    }}

    function autoPlay() {{
      render(currentStep);
      currentStep++;
      if (currentStep > maxStep) {{
        setTimeout(() => {{
          currentStep = 0;
          autoPlay();
        }}, 2000);
      }} else {{
        setTimeout(autoPlay, {SPEED});
      }}
    }}
    autoPlay();
  </script>
</body>
"""


out_path = "trace_viewer.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"[Trace Viewer] Wrote: {os.path.abspath(out_path)}  (open in your browser)")



