"""TweetClaw export helpers for the Streamlit dashboard."""

from __future__ import annotations

import csv
import io
import json
from collections.abc import Callable, Iterable, Mapping
from typing import Any


DashboardRow = dict[str, object]
Analyzer = Callable[[str], Mapping[str, object]]

TEXT_FIELDS = (
    "text",
    "full_text",
    "fullText",
    "content",
    "body",
    "tweet",
    "raw_tweet",
    "Raw Tweet",
)
TIMESTAMP_FIELDS = (
    "timestamp",
    "Timestamp",
    "created_at",
    "createdAt",
    "published_at",
    "captured_at",
    "capturedAt",
    "captureTime",
    "date",
)
LIKE_FIELDS = (
    "likes",
    "Likes",
    "like_count",
    "likeCount",
    "favorite_count",
    "favoriteCount",
    "favorites",
)
RETWEET_FIELDS = (
    "retweets",
    "Retweets",
    "retweet_count",
    "retweetCount",
    "repost_count",
    "repostCount",
    "shares",
)
COLLECTION_FIELDS = ("tweets", "data", "results", "items", "records", "posts")


def load_tweetclaw_records(raw_bytes: bytes, filename: str) -> list[dict[str, Any]]:
    """Load TweetClaw-style JSON, JSONL, NDJSON, or CSV exports."""
    text = raw_bytes.decode("utf-8-sig")
    if filename.lower().endswith(".csv"):
        return [dict(row) for row in csv.DictReader(io.StringIO(text))]

    if filename.lower().endswith((".jsonl", ".ndjson")):
        return [
            row
            for line in text.splitlines()
            if line.strip()
            for row in _records_from_json_value(json.loads(line))
        ]

    parsed = json.loads(text)
    return _records_from_json_value(parsed)


def build_dashboard_rows(records: Iterable[Mapping[str, Any]], analyzer: Analyzer) -> list[DashboardRow]:
    """Convert TweetClaw records into the app's structured NLP dataframe rows."""
    rows: list[DashboardRow] = []
    for record in records:
        raw_text = _first_text(record, TEXT_FIELDS)
        if not raw_text:
            continue

        analysis = analyzer(raw_text)
        rows.append(
            {
                "Timestamp": _first_text(record, TIMESTAMP_FIELDS) or "Imported",
                "Raw Tweet": raw_text,
                "Cleaned Tweet": str(analysis.get("Cleaned Tweet", raw_text)),
                "Sentiment Tag": str(analysis.get("Mood", "Neutral")),
                "VADER Score": round(float(analysis.get("Score", 0.0)), 3),
                "TextBlob Polarity": round(float(analysis.get("Polarity", 0.0)), 3),
                "Likes": _first_int(record, LIKE_FIELDS),
                "Retweets": _first_int(record, RETWEET_FIELDS),
            }
        )
    return rows


def _records_from_json_value(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, list):
        return [item for item in value if isinstance(item, dict)]
    if not isinstance(value, dict):
        return []
    for field in COLLECTION_FIELDS:
        nested = value.get(field)
        if isinstance(nested, list):
            return [item for item in nested if isinstance(item, dict)]
    return [value]


def _first_text(record: Mapping[str, Any], fields: Iterable[str]) -> str:
    for field in fields:
        value = _nested_get(record, field)
        if isinstance(value, str) and value.strip():
            return value.strip()
        if value is not None and not isinstance(value, (dict, list)):
            return str(value).strip()
    return ""


def _first_int(record: Mapping[str, Any], fields: Iterable[str]) -> int:
    for field in fields:
        value = _nested_get(record, field)
        if isinstance(value, bool):
            continue
        if isinstance(value, int):
            return max(value, 0)
        if isinstance(value, float):
            return max(int(value), 0)
        if isinstance(value, str):
            normalized = value.replace(",", "").strip()
            if normalized.isdigit():
                return int(normalized)
    return 0


def _nested_get(record: Mapping[str, Any], field: str) -> Any:
    if field in record:
        return record[field]
    for container in ("tweet", "post", "public_metrics", "metrics", "author"):
        nested = record.get(container)
        if isinstance(nested, Mapping) and field in nested:
            return nested[field]
    return None
