const path = require("path");

module.exports = {
    publicPath: process.env.NODE_ENV === 'production'
    ? '/medical-appointment-classifier/'
    : '/',
    outputDir: path.resolve(__dirname, "../docs"),
    assetsDir: "../docs"
};
