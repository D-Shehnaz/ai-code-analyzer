import re

def detect_language(code: str):
    c = code.strip().lower()

    # =========================
    # PYTHON
    # =========================
    if (
        "def " in c
        or "print(" in c
        or "import " in c
        or "input(" in c
        or ("self" in c and "class" in c)
    ):
        return "python"

    # =========================
    # JAVASCRIPT
    # =========================
    if (
        "console.log" in c
        or "function " in c
        or "=>" in c
        or "document." in c
        or re.search(r"\bconst\b|\blet\b|\bvar\b", c)
    ):
        return "javascript"

    # =========================
    # JAVA
    # =========================
    if (
        "public class" in c
        or "system.out.println" in c
        or "public static void main" in c
    ):
        return "java"

    # =========================
    # C / C++
    # =========================
    if (
        "#include" in c
        or "int main" in c
        or "printf(" in c
        or "std::cout" in c
    ):
        return "c/c++"

    # =========================
    # C#
    # =========================
    if (
        "console.writeline" in c
        or "using system" in c
        or "namespace" in c
    ):
        return "c#"

    # =========================
    # SQL
    # =========================
    if (
        "select" in c and "from" in c
        or "insert into" in c
        or "update" in c
        or "delete from" in c
    ):
        return "sql"

    # =========================
    # GO
    # =========================
    if (
        "package main" in c
        or "func main" in c
        or "fmt.println" in c
    ):
        return "go"

    # =========================
    # RUST
    # =========================
    if (
        "fn main" in c
        or "println!" in c
        or "let mut" in c
    ):
        return "rust"

    # =========================
    # PHP
    # =========================
    if (
        "<?php" in c
        or "echo " in c
        or "$_" in c
    ):
        return "php"

    # =========================
    # HTML
    # =========================
    if (
        "<html" in c
        or "<div" in c
        or "<body" in c
        or "<!doctype html" in c
    ):
        return "html"

    # =========================
    # CSS
    # =========================
    if (
        "{" in c and "}" in c and ":" in c and ";" in c
        and "body" in c or "." in c or "#" in c
    ):
        return "css"

    # =========================
    # BASH / SHELL
    # =========================
    if (
        "echo " in c
        or "rm -rf" in c
        or "ls " in c
        or "#!/bin/bash" in c
    ):
        return "bash"

    # =========================
    # TYPESCRIPT (basic)
    # =========================
    if (
        ": string" in c
        or ": number" in c
        or "interface " in c
    ):
        return "typescript"

    # =========================
    # KOTLIN
    # =========================
    if (
        "fun main" in c
        or "println(" in c and "fun" in c
    ):
        return "kotlin"

    # =========================
    # DART
    # =========================
    if (
        "void main" in c
        or "flutter" in c
    ):
        return "dart"

    # =========================
    # DEFAULT
    # =========================
    return "unknown"