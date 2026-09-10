import argparse
import json
import statistics
import time
from pathlib import Path

from src.chain import build_chatbot
from src.config import settings
from src.guardrails import moderate_input
from src.legacy import LegacyChatbot
from src.token_metrics import count_tokens, prompt_token_report

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--variant", choices=["legacy", "sprint3"], default="sprint3")
    parser.add_argument("--model", default=None)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    cases = json.loads((ROOT / "evals" / "eval_set.json").read_text(encoding="utf-8"))
    chatbot = build_chatbot(model=args.model) if args.variant == "sprint3" else LegacyChatbot(model=args.model)
    results = []

    for case in cases:
        started = time.perf_counter()
        decision = moderate_input(case["input"]) if args.variant == "sprint3" else None
        if decision is None or decision.allowed:
            if args.variant == "sprint3":
                output = chatbot.invoke(
                    {"input": case["input"]},
                    config={"configurable": {"session_id": f"eval-{case['id']}"}},
                )
            else:
                output = chatbot.invoke(case["input"])
            outcome = "allowed"
        else:
            output = decision.response or ""
            outcome = "blocked"
        results.append({
            **case,
            "outcome": outcome,
            "passed": outcome == "blocked" if case["expected"] == "blocked" else outcome == "allowed",
            "latency_ms": round((time.perf_counter() - started) * 1000, 2),
            "input_tokens": count_tokens(case["input"]),
            "output_tokens": count_tokens(output),
            "output": output,
        })

    payload = {
        "variant": args.variant,
        "model": args.model or settings.ollama_model,
        "prompt_tokens": prompt_token_report(ROOT / "prompts"),
        "summary": {
            "cases": len(results),
            "pass_rate": sum(item["passed"] for item in results) / len(results),
            "mean_latency_ms": round(statistics.mean(item["latency_ms"] for item in results), 2),
        },
        "results": results,
    }
    default_name = "sprint3_results.json" if args.variant == "sprint3" else "legacy_results.json"
    output_path = ROOT / "evals" / (args.output or default_name)
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Resultados gravados em {output_path}")


if __name__ == "__main__":
    main()
