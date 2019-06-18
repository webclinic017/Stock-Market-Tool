const express = require("express");
const bcryptjs = require("bcryptjs");
const jwt = require("jsonwebtoken");
const User = require("../models/user");

const router = express.Router();

router.post("/register", (req, res, next) => {
    bcryptjs.hash(req.body.password, 10)
        .then(hash => {
            const user = new User({
                email: req.body.email,
                username: req.body.username,
                password: hash
            });
            user.save()
                .then(result => {
                    res.status(201).json({
                       message: 'User Created!',
                       result: result
                    });
                })
                .catch(err => {
                    res.status(500).json({
                        error: err
                    });
                });
        });
});

router.post("/login", (req, res, next) => {
    let fetchedUser;
    User.findOne( { email: req.body.email})
        .then(user => {
            if(!user)
            {
                return res.status(401).json({
                    message: "User does not exist!"
                });
            }
            fetchedUser = user;
            return bcryptjs.compare(req.body.password, user.password);
        })
        .then(result => {
            if(!result)
            {
                return res.status(401).json({
                    message: "User authentication failed!"
                });
            }
            const token = jwt.sign({ email: fetchedUser.email, userId: fetchedUser._id}, 'this_serves_as_a_long_string', 
            { expiresIn: '1h'});
            res.status(200).json({
                token: token
            });
        })
        .catch(err => {
            return res.status(401).json({
                message: "User authentication failed!"
            });
        });
});

module.exports = router;