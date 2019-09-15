const jwt = require("jsonwebtoken");

module.exports = (req, res, next) => {
    try {
        const token = req.headers.authorization.split(" ")[0];
        jwt.verify(token, 'this_serves_as_a_long_string');
        next();
    }
    catch (error) {
        res.status(401).json({
            message: "Authentication failed!"
        });
    }
};
