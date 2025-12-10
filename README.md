# LLM Guard Middleware  
### A Defense-in-Depth Security Layer for LLM Applications  

This project implements a robust, modular, and reusable Prompt Injection Defense Middleware designed to protect Large Language Model (LLM) applications from a wide range of adversarial attacks, including:

- Prompt Injection  
- Indirect / RAG Injection  
- Jailbreaking (DAN, persona attacks)  
- System Prompt Leakage  
- Obfuscated attacks  
- Unsafe or harmful content  
- PII & credential leakage  

The middleware can be integrated into any Python LLM-powered service and includes sanitization, semantic detection, output validation, structured logging, and configurable security policies.

---

# Features

### Defense-in-Depth Architecture
Multiple layered detectors including:
- Direct prompt injection detection  
- Indirect RAG/document-based attack detection  
- Jailbreak & DAN-style detection  
- System prompt leakage detection  
- Content safety filtering  
- PII & sensitive information detection  
- Semantic fallback classifier  

### Input Sanitization
- Unicode normalization  
- Lowercasing  
- Whitespace normalization  
- Obfuscation cleanup  

### Policy Engine
Supports three security levels:
- strict  
- balanced  
- permissive  

Each level manages how detected threats are handled.

### Output Validation
- Prevents leakage of PII  
- Blocks unsafe model output  
- Ensures responses comply with security policy  

### Structured Security Logging
Every threat detection is logged as structured JSON:
```json
{
  "timestamp": "...",
  "prompt": "...",
  "threat_type": "...",
  "confidence": 0.95,
  "policy": "balanced",
  "action": "blocked"
}
