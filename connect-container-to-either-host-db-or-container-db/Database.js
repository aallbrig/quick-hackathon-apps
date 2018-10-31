const MySQL = require('mysql');

class Database {
    constructor() {
        this.connected = false;
        console.log(process.env.DB_HOST, process.env.DB_USER, process.env.DB_PASS);
        this.MySQLConn = MySQL.createConnection({
            host: process.env.DB_HOST,
            user: process.env.DB_USER,
            password: process.env.DB_PASS
        });
        this.MySQLConn.connect((err) => {
            console.log('connection results!');
            if (err) throw err;
            this.connected = true;
        });
    }
    healthCheck() {
        return {
            connected: this.connected,
            state: this.MySQLConn.state,
            host: process.env.DB_HOST,
            user: process.env.DB_USER,
            password: process.env.DB_PASS
        }
    }
}

if (typeof require !== 'undefined' && require.main === module) {
    const db = new Database();
    setTimeout(() => {
        console.log(db.healthCheck());
        process.exit();
    }, 1000);
}


module.exports = Database;