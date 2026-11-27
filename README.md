# Mini-RAG

A minimal Retrieval-Augmented Generation (RAG) system that answers questions
over a small document collection and cites the source passages it used.

## How it works (planned)

1. **Load**: read `.txt` / `.md` documents from a folder
2. **Chunk**: split documents into short passages
3. **Retrieve**: find the passages most relevant to a question (BM25 + embeddings)
4. **Generate**: a small open-source LLM writes the answer and cites passage IDs

## Goals

- Build a clean, reproducible RAG baseline that anyone can run with one command
- Practice good repository habits: branches, pull requests, tests, CI
- Reuse this pipeline as a starting point for retrieval competitions

## Roadmap

- [ ] Document loader
- [ ] Project setup with `uv`
- [ ] BM25 retrieval baseline
- [ ] Tests and linting (`pytest`, `ruff`)
- [ ] GitHub Actions CI
- [ ] Answer generation with citations

## Status

🚧 Work in progress