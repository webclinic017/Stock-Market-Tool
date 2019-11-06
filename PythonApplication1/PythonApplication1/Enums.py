from enum import Enum

class Recommendation(Enum):
	STRONG_BUY	= 5
	BUY			= 4
	NEUTRAL		= 3
	RISKY		= 2
	AVOID		= 1
	NA			= 0
class Rating(Enum):
    AT_RISK = 1
    QUESTIONABLE = 2
    HEALTHY = 3

class Stats(Enum):
	LOW = 0.25
	MID_LOW = 0.50
	MID_HIGH = 0.75
	HIGH = 1

class StdDev(Enum):
	ONE = 1
	TWO = 2
	THREE = 3

class Sector(Enum):
	ENERGY					= 1
	MATERIALS				= 2
	INDUSTRIALS				= 3
	CONSUMER_DISCRETIONARY	= 4
	CONSUMER_STAPLES		= 5
	HEALTH_CARE				= 6
	FINANCIALS				= 7
	IT						= 8
	TELECOM					= 9
	UTILITIES				= 10
	REAL_ESTATE				= 11
