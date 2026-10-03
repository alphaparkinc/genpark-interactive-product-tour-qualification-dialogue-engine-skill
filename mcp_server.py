"""MCP server for Product Tour Qualification Dialogue Engine."""
import sys
import json
from client import ProductTourDialogueEngine

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "compute_product_tour_path",
                "description": "Calculates tailored product demo tracks from qualification responses",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "user_response": {"type": "object"}
                    },
                    "required": ["user_response"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "compute_product_tour_path":
            resp = params.get("arguments", {}).get("user_response", {})
            res = ProductTourDialogueEngine.compute_tour_path(resp)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
