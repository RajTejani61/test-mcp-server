from fastmcp import FastMCP
import random
import json

mcp = FastMCP("Test Remote Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers together.
    
    Args:
		a (int): The first number.
		b (int): The second number.

	Returns:
		The sum of a and b.
    """
    return a + b

@mcp.tool
def random_number(min_value: int = 1, max_value: int = 100) -> int:
	"""Generate a random number between min_value and max_value.
	
	Args:
		min_value (int): The minimum value (default : 1).
		max_value (int): The maximum value (default : 100).

	Returns:
		A random integer between min_value and max_value.
	"""
	return random.randint(min_value, max_value)

@mcp.resource("info://server")
def server_info() -> str:
    """get information about this server"""
    info = {
		"name" : "Simple Remote Calculator Server",
		"version" : "1.0.0",
		"description" : "A basic MCP server with math tools",
		"tools" : ["add", "random_number"],
		"author" : "Alice"
	}
    return json.dumps(info, indent=2)

if __name__ == "__main__":
	mcp.run(transport="stdio")
