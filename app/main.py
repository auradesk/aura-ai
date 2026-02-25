from fastapi import FastAPI

# Phase imports
from app.engine.phase70_engine import router as phase70_router
from app.engine.phase71_engine import router as phase71_router
from app.engine.phase72_engine import router as phase72_router
from app.engine.phase73_engine import router as phase73_router
from app.engine.phase74_engine import router as phase74_router
from app.engine.phase75_engine import router as phase75_router
from app.engine.phase76_engine import router as phase76_router
from app.engine.phase77_engine import router as phase77_router
from app.engine.phase78_engine import router as phase78_router
from app.engine.phase79_engine import router as phase79_router
from app.engine.phase80_engine import router as phase80_router
from app.engine.phase81_engine import router as phase81_router
from app.engine.phase82_engine import router as phase82_router
from app.engine.phase83_engine import router as phase83_router
from app.engine.phase84_engine import router as phase84_router
from app.engine.phase85_engine import router as phase85_router
from app.engine.phase86_engine import router as phase86_router
from app.engine.phase87_engine import router as phase87_router
from app.engine.phase88_engine import router as phase88_router
from app.engine.phase89_engine import router as phase89_router
from app.engine.phase90_engine import router as phase90_router
from app.engine.phase91_engine import router as phase91_router
from app.engine.phase92_engine import router as phase92_router
from app.engine.phase93_engine import router as phase93_router
from app.engine.phase94_engine import router as phase94_router
from app.engine.phase95_engine import router as phase95_router
from app.engine.phase96_engine import router as phase96_router
from app.engine.phase97_engine import router as phase97_router
from app.engine.phase98_engine import router as phase98_router
from app.engine.phase99_engine import router as phase99_router
from app.engine.phase100_engine import router as phase100_router
from app.engine.phase101_engine import router as phase101_router
from app.engine.phase102_engine import router as phase102_router
from app.engine.phase103_engine import router as phase103_router
from app.engine.phase104_engine import router as phase104_router
from app.engine.phase105_engine import router as phase105_router
from app.engine.phase106_engine import router as phase106_router
from app.engine.phase107_engine import router as phase107_router
from app.engine.phase108_engine import router as phase108_router
from app.engine.phase109_engine import router as phase109_router
from app.engine.phase110_engine import router as phase110_router
from app.engine.phase111_engine import router as phase111_router
from app.engine.phase112_engine import router as phase112_router
from app.engine.phase113_engine import router as phase113_router
from app.engine.phase114_engine import router as phase114_router
from app.engine.phase115_engine import router as phase115_router
from app.engine.phase116_engine import router as phase116_router
from app.engine.phase117_engine import router as phase117_router
from app.engine.phase118_engine import router as phase118_router
from app.engine.phase119_engine import router as phase119_router
from app.engine.phase120_engine import router as phase120_router
from app.engine.phase121_engine import router as phase121_router


app = FastAPI(
    title="Aura Distributed AGI Core",
    version="1.0"
)

# Register routers
app.include_router(phase70_router)
app.include_router(phase71_router)
app.include_router(phase72_router)
app.include_router(phase73_router)
app.include_router(phase74_router)
app.include_router(phase75_router)
app.include_router(phase76_router)
app.include_router(phase77_router)
app.include_router(phase78_router)
app.include_router(phase79_router)
app.include_router(phase80_router)
app.include_router(phase81_router)
app.include_router(phase82_router)
app.include_router(phase83_router)
app.include_router(phase84_router)
app.include_router(phase85_router)
app.include_router(phase86_router)
app.include_router(phase87_router)
app.include_router(phase88_router)
app.include_router(phase89_router)
app.include_router(phase90_router)
app.include_router(phase91_router)
app.include_router(phase92_router)
app.include_router(phase93_router)
app.include_router(phase94_router)
app.include_router(phase95_router)
app.include_router(phase96_router)
app.include_router(phase97_router)
app.include_router(phase98_router)
app.include_router(phase99_router)
app.include_router(phase100_router)
app.include_router(phase101_router)
app.include_router(phase102_router)
app.include_router(phase103_router)
app.include_router(phase104_router)
app.include_router(phase105_router)
app.include_router(phase106_router)
app.include_router(phase107_router)
app.include_router(phase108_router)
app.include_router(phase109_router)
app.include_router(phase110_router)
app.include_router(phase111_router)
app.include_router(phase112_router)
app.include_router(phase113_router)
app.include_router(phase114_router)
app.include_router(phase115_router)
app.include_router(phase116_router)
app.include_router(phase117_router)
app.include_router(phase118_router)
app.include_router(phase119_router)
app.include_router(phase120_router)
app.include_router(phase121_router)


@app.get("/")
def root():
    return {
        "message": "Aura Distributed AGI Core Running",
        "active_phases": [
            "Phase 70 — Multi-Instance Intelligence",
            "Phase 71 — Distributed Memory",
            "Phase 72 — Distributed Reasoning"
        ]
    }