from enum import Enum

class Recommendation(Enum):
	STRONG_BUY	= "Strong Buy"
	BUY			= "Buy"
	NEUTRAL		= "Neutral"
	RISKY		= "Risky"
	AVOID		= "Avoid"
	NA			= "No Decision"
class Rating(Enum):
	UNKNOWN = "NA"
	AT_RISK = "At Risk"
	QUESTIONABLE = "Questionable"
	HEALTHY = "Healthy"

class Stats(Enum):
	LOW = 0.25
	MID_LOW = 0.50
	MID_HIGH = 0.75
	HIGH = 1

class StatsMeaning(Enum):
	LOW = "Worst 25%"
	MID_LOW = "Lower 50%"
	MID_HIGH = "Upper 50%"
	HIGH = "Best 25%"

class StdDev(Enum):
	ONE = 1
	TWO = 2
	THREE = 3

class Sector(Enum):
	
	ENRS = 1	# Energy Services
	MATR = 2	# Materials
	INDU = 3	# Industrials
	COND = 4	# Consumer Discretionary
	CONS = 5	# Consumer Staples
	HLTH = 6	# Health Care
	FINL = 7	# Financial Services
	INFT = 8	# Informtation Technology
	UTIL = 9	# Utilities
	REAL = 10	# Real Estate
	TELS = 11	# Communication Services

class SectorName(Enum):
	
	ENRS = "Energy Services"
	MATR = "Materials"
	INDU = "Industrials"
	COND = "Consumer Discretionary"
	CONS = "Consumer Staples"
	HLTH = "Health Care"
	FINL = "Financial Services"
	INFT = "Informtation Technology"
	UTIL = "Utilities"
	REAL = "Real Estate"
	TELS = "Communication Services"





