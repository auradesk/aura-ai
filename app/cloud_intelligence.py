from sqlalchemy.orm import Session
from datetime import datetime

from app.engine.memory_engine import memory_engine
from app.engine.knowledge_engine import knowledge_engine
from app.engine.reasoning_engine import reasoning_engine
from app.engine.cognition_engine import cognition_engine
from app.engine.learning_engine import learning_engine


def cloud_intelligence(

    db: Session,

    tenant_id: str,

    domain: str,

    message: str

):

    cognition = cognition_engine.analyze(message)

    knowledge = knowledge_engine.get_knowledge(
        db,
        domain
    )

    memory = memory_engine.get_last_memory(
        db,
        tenant_id,
        domain
    )

    response = reasoning_engine.generate_response(
        tenant_id,
        domain,
        message,
        memory,
        knowledge
    )

    if cognition["intent"] == "learning":

        learning_engine.learn(
            db,
            domain,
            message
        )

    memory_engine.store_memory(
        db,
        tenant_id,
        domain,
        message,
        response
    )

    return {

        "status": "success",

        "tenant_id": tenant_id,

        "domain": domain,

        "intent": cognition["intent"],

        "response": response,

        "timestamp": datetime.utcnow().isoformat()

    }
