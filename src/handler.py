"""Request handler for packline-scheduler."""

def handle(event: dict) -> dict:
    kind = event.get("kind", "scan")
    return {"ok": True, "kind": kind, "service": "packline-scheduler"}
