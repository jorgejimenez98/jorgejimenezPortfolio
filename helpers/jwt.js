const expressJwt = require("express-jwt");

// Method to Protect API authentication
function authJWT() {
  const secret = "secret_token_string";
  return expressJwt({
    secret,
    algorithms: ["HS256"],
    isRevoked: isRevoked,
  }).unless({
    path: [{ url: /\/api\/(.*)/, methods: ["GET", "OPTIONS"] }],
  });
}

async function isRevoked(req, payload, done) {
  if (!payload.isAdmin) {
    done(null, true);
  }
  done();
}

module.exports = authJWT;
