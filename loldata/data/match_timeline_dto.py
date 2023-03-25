"""
Dataclass representing a MatchDto.

https://developer.riotgames.com/apis#match-v5/GET_getTimeline
"""

from dataclasses import dataclass
from typing import List


@dataclass
class PositionDto:
    x: int
    y: int


@dataclass
class ChampionStatsDto:
    abilityHaste: int
    abilityPower: int
    armor: int
    armorPen: int
    armorPenPercent: int
    attackDamage: int
    attackSpeed: int
    bonusArmorPenPercent: int
    bonusMagicPenPercent: int
    ccReduction: int
    cooldownReduction: int
    health: int
    healthMax: int
    healthRegen: int
    lifesteal: int
    magicPen: int
    magicPenPercent: int
    magicResist: int
    movementSpeed: int
    omnivamp: int
    physicalVamp: int
    power: int
    powerMax: int
    powerRegen: int
    spellVamp: int


@dataclass
class DamageStatsDto:
    magicDamageDone: int
    magicDamageDoneToChampions: int
    magicDamageTaken: int
    physicalDamageDone: int
    physicalDamageDoneToChampions: int
    physicalDamageTaken: int
    totalDamageDone: int
    totalDamageDoneToChampions: int
    totalDamageTaken: int
    trueDamageDone: int
    trueDamageDoneToChampions: int
    trueDamageTaken: int


@dataclass
class ParticipantFrameDto:
    participantId: int
    position: PositionDto
    currentGold: int
    totalGold: int
    level: int
    xp: int
    minionsKilled: int
    jungleMinionsKilled: int
    championStats: ChampionStatsDto
    damageStats: DamageStatsDto
    goldPerSecond: int
    timeEnemySpentControlled: int
    wardsPlaced: int
    wardsKilled: int
    visionWardsBought: int


@dataclass
class EventDto:
    type: str
    timestamp: int


@dataclass
class ChampionKillEventDto(EventDto):
    killerId: int
    victimId: int
    assistingParticipantIds: List[int]
    position: PositionDto


@dataclass
class WardPlacedEventDto(EventDto):
    wardType: str
    creatorId: int
    position: PositionDto


@dataclass
class WardKillEventDto(EventDto):
    wardType: str
    killerId: int
    position: PositionDto


@dataclass
class BuildingKillEventDto(EventDto):
    killerId: int
    assistingParticipantIds: List[int]
    teamId: int
    buildingType: str
    laneType: str
    position: PositionDto


@dataclass
class EliteMonsterKillEventDto(EventDto):
    killerId: int
    monsterType: str
    position: PositionDto


@dataclass
class ItemPurchasedEventDto(EventDto):
    participantId: int
    itemId: int


@dataclass
class ItemDestroyedEventDto(EventDto):
    participantId: int
    itemId: int


@dataclass
class ItemSoldEventDto(EventDto):
    participantId: int
    itemId: int


@dataclass
class SkillLevelUpEventDto(EventDto):
    participantId: int
    skillSlot: int
    levelUpType: str


@dataclass
class FrameDto:
    events: List[dict]
    participantFrames: List[ParticipantFrameDto]
    timestamp: int


@dataclass
class ParticipantDto:
    participantId: int
    puuid: str


@dataclass
class InfoDto:
    frameInterval: int
    frames: List[FrameDto]
    gameId: int
    participants: List[ParticipantDto]


@dataclass
class MetadataDto:
    dataVersion: str
    matchId: str
    participants: List[str]


@dataclass
class MatchTimelineDto:
    metadata: MetadataDto
    info: InfoDto
