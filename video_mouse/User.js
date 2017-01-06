// much more concise declaration
function User(db) {
    this.db = db;
    console.log(db);
}

// You need to assign a new function here
User.prototype.findOne = function (email, password, fn) {
    // some code here
}

// no need to overwrite `exports` ... since you're replacing `module.exports` itself
module.exports = User;

