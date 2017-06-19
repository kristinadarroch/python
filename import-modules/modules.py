import json

print(json.dumps({'10': 15, '8': 2}, sort_keys=True, indent=5))
{
    "10": 15,
    "8": 2
}
