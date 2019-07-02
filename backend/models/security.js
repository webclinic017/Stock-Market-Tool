const mongoose = require('mongoose');
const uniqueValidator = require("mongoose-unique-validator");

const securitySchema = mongoose.Schema({
    ticker: { type: String, required: true, unique: true},
    PE: { type: Number, required: true},
    EY: { type: Number, required: true},
    ROE: { type: Number, required: true},
    ROIC: { type: Number, required: true},
    RetentionRatio: { type: Number, required: true},
    SGR: { type: Number, required: true},
    ROA: { type: Number, required: true},
    PB: { type: Number, required: true}
});

securitySchema.plugin(uniqueValidator);

module.exports = mongoose.model("Security", securitySchema);