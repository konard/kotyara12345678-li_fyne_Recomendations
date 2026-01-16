#!/usr/bin/env python3
"""
Experiment script to test Typesense vector search functionality.

Usage:
    1. Start Typesense: docker compose up typesense -d
    2. Run this script: python experiments/test_vector_search.py

This script tests the vector_query format for Typesense vector search.
"""
import httpx
import json
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_vector_query_format():
    """Test that vector_query string format works correctly."""

    # Configuration
    host = os.getenv("TYPESENSE_HOST", "localhost")
    port = os.getenv("TYPESENSE_PORT", "8108")
    api_key = os.getenv("TYPESENSE_API_KEY", "dev-key")
    collection = os.getenv("TYPESENSE_COLLECTION", "issues")
    vector_dim = int(os.getenv("TYPESENSE_VECTOR_DIM", "384"))

    base_url = f"http://{host}:{port}"
    headers = {
        "X-TYPESENSE-API-KEY": api_key,
        "Content-Type": "application/json",
    }

    print(f"Testing Typesense at {base_url}")
    print(f"Collection: {collection}, Vector dim: {vector_dim}")
    print("-" * 50)

    # Check if collection exists
    try:
        with httpx.Client(timeout=5.0) as client:
            resp = client.get(f"{base_url}/collections/{collection}", headers=headers)
            if resp.status_code == 404:
                print(f"Collection '{collection}' does not exist. Creating...")
                schema = {
                    "name": collection,
                    "fields": [
                        {"name": "id", "type": "string"},
                        {"name": "title", "type": "string"},
                        {"name": "description", "type": "string"},
                        {"name": "labels", "type": "string[]"},
                        {
                            "name": "embedding",
                            "type": "float[]",
                            "num_dim": vector_dim,
                            "vec_dist": "cosine",
                        },
                    ],
                }
                resp = client.post(f"{base_url}/collections", headers=headers, json=schema)
                resp.raise_for_status()
                print("Collection created successfully!")
            else:
                resp.raise_for_status()
                info = resp.json()
                print(f"Collection exists with {info.get('num_documents', 0)} documents")
    except httpx.ConnectError:
        print(f"ERROR: Cannot connect to Typesense at {base_url}")
        print("Make sure Typesense is running: docker compose up typesense -d")
        return False
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")
        return False

    # Insert test documents if collection is empty
    try:
        with httpx.Client(timeout=10.0) as client:
            resp = client.get(f"{base_url}/collections/{collection}", headers=headers)
            info = resp.json()

            if info.get("num_documents", 0) == 0:
                print("Inserting test documents...")

                # Create simple normalized test vectors
                import math

                def normalize(vec):
                    mag = math.sqrt(sum(x*x for x in vec))
                    return [x/mag for x in vec] if mag > 0 else vec

                # Create test vectors (first 10 dims have values, rest zeros)
                test_docs = []
                for i in range(3):
                    vec = [0.0] * vector_dim
                    vec[i] = 1.0  # Different principal direction for each doc
                    vec = normalize(vec)

                    test_docs.append({
                        "id": f"test-{i}",
                        "title": f"Test Issue {i}",
                        "description": f"This is test description {i}",
                        "labels": ["test"],
                        "embedding": vec,
                    })

                resp = client.post(
                    f"{base_url}/collections/{collection}/documents/import",
                    headers=headers,
                    params={"action": "upsert"},
                    content="\n".join(json.dumps(d) for d in test_docs),
                )
                print(f"Import result: {resp.text}")
    except Exception as e:
        print(f"ERROR inserting documents: {type(e).__name__}: {e}")
        return False

    # Test vector search with correct format
    print("\n" + "=" * 50)
    print("Testing vector search with STRING format (correct):")
    print("=" * 50)

    # Create a query vector similar to test-0
    import math
    query_vec = [0.0] * vector_dim
    query_vec[0] = 1.0
    mag = math.sqrt(sum(x*x for x in query_vec))
    query_vec = [x/mag for x in query_vec]

    vector_str = ",".join(str(v) for v in query_vec)
    search_body = {
        "q": "*",
        "vector_query": f"embedding:([{vector_str}], k:5)",
        "exclude_fields": "embedding",
    }

    print(f"vector_query (truncated): {search_body['vector_query'][:80]}...")

    try:
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{base_url}/collections/{collection}/documents/search",
                headers=headers,
                json=search_body,
            )

            if resp.status_code == 200:
                result = resp.json()
                hits = result.get("hits", [])
                print(f"\nSUCCESS! Found {len(hits)} results:")
                for i, hit in enumerate(hits):
                    doc = hit.get("document", {})
                    dist = hit.get("vector_distance", "N/A")
                    print(f"  {i+1}. {doc.get('id')}: {doc.get('title')} (distance: {dist})")
                return len(hits) > 0
            else:
                print(f"ERROR: HTTP {resp.status_code}: {resp.text}")
                return False

    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")
        return False


def test_wrong_format():
    """Show what happens with the old (wrong) dictionary format."""

    host = os.getenv("TYPESENSE_HOST", "localhost")
    port = os.getenv("TYPESENSE_PORT", "8108")
    api_key = os.getenv("TYPESENSE_API_KEY", "dev-key")
    collection = os.getenv("TYPESENSE_COLLECTION", "issues")
    vector_dim = int(os.getenv("TYPESENSE_VECTOR_DIM", "384"))

    base_url = f"http://{host}:{port}"
    headers = {
        "X-TYPESENSE-API-KEY": api_key,
        "Content-Type": "application/json",
    }

    print("\n" + "=" * 50)
    print("Testing vector search with DICT format (WRONG):")
    print("=" * 50)

    import math
    query_vec = [0.0] * vector_dim
    query_vec[0] = 1.0
    mag = math.sqrt(sum(x*x for x in query_vec))
    query_vec = [x/mag for x in query_vec]

    # This is the OLD/WRONG format that was in the original code
    search_body = {
        "q": "*",
        "vector_query": {
            "embedding": {
                "vector": query_vec,
                "k": 5
            }
        },
        "limit": 5,
        "include_fields": "id,title,description",
    }

    print(f"vector_query type: {type(search_body['vector_query'])}")

    try:
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{base_url}/collections/{collection}/documents/search",
                headers=headers,
                json=search_body,
            )

            if resp.status_code == 200:
                result = resp.json()
                hits = result.get("hits", [])
                print(f"Response: {len(hits)} results (likely 0 because format is wrong)")
            else:
                print(f"ERROR (expected): HTTP {resp.status_code}")
                print(f"Response: {resp.text[:200]}")

    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")


if __name__ == "__main__":
    print("Typesense Vector Search Format Test")
    print("=" * 50)

    success = test_vector_query_format()

    if success:
        test_wrong_format()

    print("\n" + "=" * 50)
    print(f"Test result: {'PASSED' if success else 'FAILED'}")
    print("=" * 50)

    sys.exit(0 if success else 1)
