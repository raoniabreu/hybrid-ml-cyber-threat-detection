def static_analysis(sample):
    """
    Simulated static analysis based on simple rules.
    """

    risk_flags = []

    # Example rules (simple demonstration)
    if "write" in str(sample).lower():
        risk_flags.append("Potential write permission abuse")

    if "exec" in str(sample).lower():
        risk_flags.append("Execution behavior detected")

    if len(risk_flags) == 0:
        return "No significant risks detected"
    
    return f"Risk detected: {', '.join(risk_flags)}"