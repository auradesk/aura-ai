from fastapi import APIRouter
from datetime import datetime
from typing import Dict, Any, List

router = APIRouter(
    prefix="/metrics",
    tags=["Phase121 Metrics Engine"]
)

class Phase121Engine:
    """
    Phase 121 — Metrics History & Intelligence Tracking Engine
    """

    def __init__(self):
        self.metrics_history: List[Dict[str, Any]] = []

    def record_metric(self, metric_name: str, value: float, metadata: Dict[str, Any] = None):
        entry = {
            "metric": metric_name,
            "value": value,
            "metadata": metadata or {},
            "timestamp": datetime.utcnow().isoformat()
        }

        self.metrics_history.append(entry)
        return entry

    def get_metrics_history(self):
        return self.metrics_history

    def get_metrics_summary(self):
        summary = {}

        for entry in self.metrics_history:
            name = entry["metric"]
            value = entry["value"]

            if name not in summary:
                summary[name] = {
                    "count": 0,
                    "total": 0,
                    "average": 0
                }

            summary[name]["count"] += 1
            summary[name]["total"] += value
            summary[name]["average"] = summary[name]["total"] / summary[name]["count"]

        return summary


# Global engine instance
phase121_engine = Phase121Engine()


# API ROUTES

@router.get("/history")
def get_metrics_history():
    return phase121_engine.get_metrics_history()


@router.get("/summary")
def get_metrics_summary():
    return phase121_engine.get_metrics_summary()


@router.post("/record")
def record_metric(metric_name: str, value: float):
    return phase121_engine.record_metric(metric_name, value)