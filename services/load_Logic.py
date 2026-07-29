import os
from pathlib import Path
from langchain_core.documents import Document

class Repo_Load:

     SUPPORTED_EXTENSIONS = {
        ".py",
        ".js",
        ".ts",
        ".java",
        ".cpp",
        ".c",
        ".go",
        ".md",
        ".txt",
        ".json",
        ".yaml",
        ".yml",
        ".toml",
        ".html",
        ".css",
        ".sql",
        ".sh",
        ".ipynb",
        ".pkl",
        ".joblib",
        ".csv"
        
    }

     IGNORE_DIRS = {
        ".git",
        "__pycache__",
        "venv",
        ".venv",
        "env",
        "node_modules",
        ".idea",
        ".vscode",
        "dist",
        "build",
    }

     @classmethod
     def Load(cls, repo_path : str):
        document = []
        for root,dirs,files in os.walk(repo_path):
              
                dirs[:] = [d for d in dirs if d not in cls.IGNORE_DIRS]
                for file in files:
                    file_path = Path(root)/file
                    if file_path.suffix not in cls.SUPPORTED_EXTENSIONS:
                        continue
                    try:
                         content = file_path.read_text(
                               encoding="utf-8",
                               errors="ignore"
                         )

                         document.append(
                              Document(
                                   page_content = content,
                                   metadata={
                                    "source": str(file_path),
                                    "filename": file,
                                    "extension": file_path.suffix,
                                },
                              )
                         )
                    except Exception:
                         continue
        return document
                
                         
