import importlib

def fetch_block(block_to_fetch):
    fetched_block = block_to_fetch.replace(" ", "_")
    
    return getattr(importlib.import_module(f"src.Block.{fetched_block}"), fetched_block)
