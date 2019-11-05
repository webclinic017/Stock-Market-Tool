from enum import Enum

class Recommendation(Enum):
	STRONG_BUY
	BUY
	RISKY
	AVOID
	UNKNOWN

class Rating(Enum):
    AT_RISK = 1
    SAFE = 2
    HEALTHY = 3

class Stats(Enum):
	LOW = 0.25
	MID_LOW = 0.50
	MID_HIGH = 0.75
	HIGH = 1

class StdDev(Enum):
	ONE
	TWO
	THREE

class Sector(Enum):
	ENERGY
	MATERIALS
	INDUSTRIALS
	CONSUMER_DISCRETIONARY
	CONSUMER_STAPLES
	HEALTH_CARE
	FINANCIALS
	IT
	TELECOM
	UTILITIES
	REAL_ESTATE
