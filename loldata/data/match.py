"""
Dataclass representing a MatchDto.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class Metadata:
    data_version: str
    match_id: str
    participants: List[str]


@dataclass
class ParticipantIdentity:
    participant_id: int
    player: Dict[str, Any]


@dataclass
class ParticipantStats:
    stats: Dict[str, Any]


@dataclass
class ParticipantTimeline:
    timeline: Dict[str, Any]


@dataclass
class Participant:
    participant_id: int
    team_id: int
    champion_id: int
    spell1_id: int
    spell2_id: int
    stats: ParticipantStats
    timeline: ParticipantTimeline


@dataclass
class Team:
    team_id: int
    win: bool
    objectives: Dict[str, Dict[str, Any]]


@dataclass
class Info:
    game_datetime: int
    game_length: float
    game_id: int
    game_start_timestamp: int
    game_version: str
    map_id: int
    queue_id: int
    season_id: int
    teams: List[Team]
    participants: List[Participant]


@dataclass
class MatchDto:
    metadata: Metadata
    info: Info
