from pinecone import Pinecone
import os
from dotenv import load_dotenv


async def getPinecone():
    load_dotenv()
    PINECONE_API = os.getenv("PINECONE_API")
    pc = Pinecone(api_key=PINECONE_API)

    index_name = "reminder"
    if not pc.has_index(index_name):
        pc.create_index_for_model(
            name=index_name,
            cloud="aws",
            region="us-east-1",
            embed={
                "model":"multilingual-e5-large",
                "field_map":{"text": "chunk_text"}
            }
        )
    return pc

async def upsert(text: str, pc, id, metadata):
    index = pc.Index("reminder")
    index.upsert_records(
        "reminder_namespace",
        [
            {
                "_id": id,
                "chunk_text": text,
                "metadata": metadata
            }
        ]
    )

async def search(query: str, pc, top_k: int = 5):
    index = pc.Index("reminder")
    results = index.query_records(
        namespace="reminder_namespace",
        query={
            "text": query
        },
        top_k=top_k
    )

    matches = [
        {
            "id": match["_id"],
            "score": match["score"],
            "text": match["fields"]["text"]
        }
        for match in results["matches"]
    ]

    return matches