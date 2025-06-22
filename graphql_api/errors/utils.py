def determine_http_status(result):
    for error in result.get("errors", []):
        status = error.get("extensions", {}).get("status")
        if isinstance(status, int):
            return status
    return 200
