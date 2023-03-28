"""
This dataclass represents a MatchDto.
GET -- /lol/match/v5/matches/{matchId}

Product -- GetGood.GG
https://github.com/Knaeckebrothero/Projekt-GetGood.GG
App ID -- 616160
https://developer.riotgames.com/
"""

from dataclasses import dataclass
from typing import List


@dataclass
class PerkStatsDto:
    defense: int
    flex: int
    offense: int


@dataclass
class PerkStyleSelectionDto:
    perk: int
    var1: int
    var2: int
    var3: int


@dataclass
class PerkStyleDto:
    description: str
    selections: List[PerkStyleSelectionDto]
    style: int


@dataclass
class PerksDto:
    statPerks: PerkStatsDto
    styles: List[PerkStyleDto]


@dataclass
class ObjectiveDto:
    first: bool
    kills: int


@dataclass
class ObjectivesDto:
    baron: ObjectiveDto
    champion: ObjectiveDto
    dragon: ObjectiveDto
    inhibitor: ObjectiveDto
    riftHerald: ObjectiveDto
    tower: ObjectiveDto


@dataclass
class BanDto:
    championId: int
    pickTurn: int


@dataclass
class TeamDto:
    bans: List[BanDto]
    objectives: ObjectivesDto
    teamId: int
    win: bool


@dataclass
class ParticipantDto:
    assists: int
    baronKills: int
    bountyLevel: int
    champExperience: int
    champLevel: int
    championId: int
    championName: str
    championTransform: int
    consumablesPurchased: int
    damageDealtToBuildings: int
    damageDealtToObjectives: int
    damageDealtToTurrets: int
    damageSelfMitigated: int
    deaths: int
    detectorWardsPlaced: int
    doubleKills: int
    dragonKills: int
    firstBloodAssist: bool
    firstBloodKill: bool
    firstTowerAssist: bool
    firstTowerKill: bool
    gameEndedInEarlySurrender: bool
    gameEndedInSurrender: bool
    goldEarned: int
    goldSpent: int
    individualPosition: str
    inhibitorKills: int
    inhibitorTakedowns: int
    inhibitorsLost: int
    item0: int
    item1: int
    item2: int
    item3: int
    item4: int
    item5: int
    item6: int
    itemsPurchased: int
    killingSprees: int
    kills: int
    lane: str
    largestCriticalStrike: int
    largestKillingSpree: int
    largestMultiKill: int
    longestTimeSpentLiving: int
    magicDamageDealt: int
    magicDamageDealtToChampions: int
    magicDamageTaken: int
    neutralMinionsKilled: int
    nexusKills: int
    nexusTakedowns: int
    nexusLost: int
    objectivesStolen: int
    objectivesStolenAssists: int
    participantId: int
    pentaKills: int
    perks: PerksDto
    physicalDamageDealt: int
    physicalDamageDealtToChampions: int
    physicalDamageTaken: int
    profileIcon: int
    puuid: str
    quadraKills: int
    riotIdName: str
    riotIdTagline: str
    role: str
    sightWardsBoughtInGame: int
    spell1Casts: int
    spell2Casts: int
    spell3Casts: int
    spell4Casts: int
    summoner1Casts: int
    summoner1Id: int
    summoner2Casts: int
    summoner2Id: int
    summonerId: str
    summonerLevel: int
    summonerName: str
    teamEarlySurrendered: bool
    teamId: int
    teamPosition: str
    timeCCingOthers: int
    timePlayed: int
    totalDamageDealt: int
    totalDamageDealtToChampions: int
    totalDamageShieldedOnTeammates: int
    totalDamageTaken: int
    totalHeal: int
    totalHealsOnTeammates: int
    totalMinionsKilled: int
    totalTimeCCDealt: int
    totalTimeSpentDead: int
    totalUnitsHealed: int
    tripleKills: int
    trueDamageDealt: int
    trueDamageDealtToChampions: int
    trueDamageTaken: int
    turretKills: int
    turretTakedowns: int
    turretsLost: int
    unrealKills: int
    visionScore: int
    visionWardsBoughtInGame: int
    wardsKilled: int
    wardsPlaced: int
    win: bool


@dataclass
class InfoDto:
    gameCreation: int
    gameDuration: int
    gameEndTimestamp: int
    gameId: int
    gameMode: str
    gameName: str
    gameStartTimestamp: int
    gameType: str
    gameVersion: str
    mapId: int
    participants: List[ParticipantDto]
    platformId: str
    queueId: int
    teams: List[TeamDto]
    tournamentCode: str


@dataclass
class MetadataDto:
    dataVersion: str
    matchId: str
    participants: List[str]


# Main dataclass containing the other classes.
@dataclass
class MatchDto:
    metadata: MetadataDto
    info: InfoDto
