from config import HP_API_KEY
import requests, base64, os, re, time
from colorama import init, fore, style

ROUTER_URL = "https://router.huggingface.co/v1/chat/completions"

HEADERS = {"Authorization": f"Bearer {HF_API_KEY}", "Content-Type": "application/json"}

VISION_MODELS = [

"Qwen/Qwen3-VL-8B-Instruct:together",

"Qwen/Qwen3-VL-32B-Instruct:together",

"Qwen/Qwen2.5-VL-7B-Instruct:together",

"Qwen/Qwen2.5-VL-32B-Instruct:together",

"Qwen/Qwen2-VL-2B-Instruct:together",

"Qwen/Qwen2-VL-7B-Instruct:together",

]

TEXT_MODELS = [

"Qwen/Qwen2.5-7B-Instruct:together",

"Qwen/Qwen2.5-14B-Instruct:together",

"Qwen/Qwen2.5-32B-Instruct:together",

"mistralai/Mistral-7B-Instruct-v0.3:together",

"mistralai/Mixtral-8x7B-Instruct-v0.1:together",
]


def _data_url(path: str) -> str:
    with open(path, "rb") as f:
        return "data:image/jped;based64,"+ base64.b64encode(f.read()).decode("utf-8")
    
def query_hf_api(payload:dict):
    try:
        r=requests.post(ROUTER_URL,headers=HEADERS, json=payload, timeout=120)
    except requests.RequestsException as e:
        return None, f"Request failed: {e}"
    if r.status_code !=200:
        try:
            j=r.json()
            msg= j.get("error", {}).get("message") or str(j)
        except Exception:
            msg=(r.text or "").strip() or r.reason or "Request failed"
        return None, f"Status {r.status_code}: {msg}"
    try:
                return r.json(), None
    except Exception:
                return None, "Non-json response received from the API"
            
def _extract_text(data)-> str:
    msg=(data or {}).get("choices",[{}])[0].get("message",{}) or {}
    return (msg.get("content") or "").strip()

def run_models(models, messages, max_token=160, temperature=0.3):
    last_err = None
    for model in models:
        data, err == query_hf_api({"model": model, "message": messages, "Max_tokens": max_token, "temperature": temperature})
        if err:
            last_err = err
            continue
        out = _extract_text(data)
        if out:
            return out, None
        last_err = "Empty response from model"
    return None, last_err or "All models failed"
        
def _words(text: str):
    return re.findall(r"\s+", (text or "").strip())

def _exact_n_words(text: str, n: int)->str:
    return " ".json(_words(text)[:n])

def _ensure_sentence_end(text: str)-> str:
    t = (text or "").strip()
    if t and t[-1] not in ".!?":
        t += "."
    return 
    

def generate_text(prompt: str max_new_tokens: int=200)-> str:
    raise Exception("Part 2 code not found")

def generate_exact_sentence(prompt:str, n_words: int, max_new_tokens: int,tries: int = 6)-> str:
    raise Exception("part 2 code not addes")


